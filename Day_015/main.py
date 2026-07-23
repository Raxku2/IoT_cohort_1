import os
import pygame
from pathlib import Path
from textual.app import App,ComposeResult
from textual.widgets import (
    ListView, Static, 
    Header, Footer, 
    Button, Label, 
    ProgressBar, ListItem)
from textual.containers import Vertical, Horizontal, Grid
from textual.binding import Binding
import mutagen

import io
from rich.text import Text


class AudioEngine:
    def __init__(self):
        try:
            pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=1024)
        except pygame.error:
            pygame.mixer.init()
            
        self.current_track = None
        self.is_paused = False
        self.end_event = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(self.end_event)

    def load_and_play(self, file_path: Path):
        try:
            pygame.mixer.music.load(str(file_path))
            pygame.mixer.music.play()
            self.current_track = file_path
            self.is_paused = False

            try:
                audio = mutagen.File(file_path)
                length = audio.info.length  if audio else 0
            except Exception:
                length = 0

            return True, length
        except pygame.error:
            return False

    def toggle_pause(self):
        if pygame.mixer.music.get_busy() or self.is_paused:
            if self.is_paused:
                pygame.mixer.music.unpause()
                self.is_paused = False
            else:
                pygame.mixer.music.pause()
                self.is_paused = True

    def stop(self):
        pygame.mixer.music.stop()
        self.current_track = None
        self.is_paused = False

class SongItem(ListItem):
    def __init__(self, file_path: Path, index: int):
        self.file_path = file_path
        self.index = index
        super().__init__(Label(f"{file_path.stem}"), id=f"song-{index}")

class MusicPlayer(App):
    CSS="""
    Screen {
        background: #1a1a1a;
        color: #FFFFFF;
    }
    
    Header, Footer {
        background: #101010;
        color: #888888;
    }

    /* Main Container Grid: [Player Panel (45%) | Playlist Panel (55%)] */
    #main-container {
        layout: horizontal;
        height: 100%;
        width: 100%;
    }

    /* LEFT SIDE: Player Controls */
    #player-panel {
        width: 45%;
        height: 100%;
        border-right: solid #00FF00; /* Neon Green Border */
        padding: 1 2;
        align: center middle;
    }

    #artwork {
        width: 100%;
        height: 15;
        background: #101010;
        color: #888888;
        content-align: center middle;
        border: dashed #888888;
        margin-bottom: 1;
    }

    #track-title {
        text-style: bold;
        color: #FFFFFF;
        content-align: center middle;
        width: 100%;
    }

    #track-artist {
        color: #888888;
        content-align: center middle;
        width: 100%;
        margin-bottom: 2;
    }

    #progress-container {
        layout: horizontal;
        height: 3;
        width: 100%;
        margin-bottom: 1;
        content-align: center middle;
    }
    
    ProgressBar {
        width: 1fr;
        color: #FF1493; /* Neon Pink Progress Bar */
        margin: 0 1;
    }
    
    #controls {
        align: center middle;
        height: auto;
        width: 100%;
        margin-top: 1;
    }

    Button {
        margin: 0 1;
        min-width: 8;
        background: #101010;
        color: #00BFFF; /* Neon Blue Text on Controls */
        border: none;
    }
    
    Button:hover {
        background: #00FF00; /* Neon Green Hover */
        color: #000000;
    }
    
    #play-pause {
        text-style: bold;
        background: #00BFFF; /* Bright Neon Blue */
        color: #FFFFFF;
    }
    
    #play-pause:hover {
        background: #00e0ff;
    }

    /* RIGHT SIDE: Playlist */
    #playlist-panel {
        width: 55%;
        height: 100%;
        padding: 1 2;
    }

    #playlist-title {
        text-style: bold;
        color: #00FF00; /* Neon Green playlist title */
        width: 100%;
        content-align: left middle;
        margin-bottom: 1;
    }

    ListView {
        background: #101010;
        border: solid #00FF00; /* Neon Green playlist border */
        color: #FFFFFF;
    }

    SongItem {
        padding: 0 1;
    }
    
    /* Current song being highlighted by the player (Neon Pink) */
    SongItem.now-playing {
        color: #FF1493; /* Neon Pink */
        text-style: bold;
    }
    
    /* Cursor Selection highlight in the list (Neon Orange) */
    ListView:focus > ListItem.--highlight {
        background: #FFA500; /* Neon Orange background */
        color: #000000; /* Black text */
    }
    
    /* Highlight of item under mouse cursor */
    ListItem:hover {
        background: #2a2a2a;
    }
        """

    BINDINGS=[
        Binding("q","quit","Quit", show=True),
        Binding("space","play_pause","Play/Pause", show=True),
        Binding("n","next_track","Next", show=False),
        Binding("p","prev_track","Prev", show=False),
    ]

    def __init__(self):
        super().__init__()
        self.audio = AudioEngine()
        self.track_list = []
        self.current_track_index = -1
        self.track_length = 0
        self.progress_timer = None


    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal(id="main-container"):
            with Vertical(id="player-panel"):
                yield Static("[ ALBUM ART ]\n\n(Coming)", id="artwork")
                yield Label("Welcome", id="track-title")
                yield Label("Unknown Artist", id="track-artist")

                with Horizontal(id="progress-container"):
                    yield Label("00:00",id="time-elapsed")
                    yield ProgressBar(total=100,show_percentage=False,show_eta=False)

                    yield Label("00:00",id="time-total")


                with Horizontal(id="controls"):
                    yield Button("|<<",id="prev")
                    yield Button("|>",id="play-pause")
                    yield Button(">>|",id="next")

            with Vertical(id="playlist-panel"):
                yield Label("TRACKLIST",id="playlist-title")
                yield ListView(id="playlist")

        yield Footer()

    def on_mount(self) -> None:
        self.title = "TUI Music Player"
        self.populate_playlist()

    def populate_playlist(self) -> None:
        current_dir = Path(".")
        mp3_files = sorted(list(current_dir.glob("*.mp3")), key=lambda p: p.stem.lower())
        
        playlist_widget = self.query_one("#playlist", ListView)
        
        # Clear existing
        playlist_widget.clear()
        self.track_list = []
        
        for index, file_path in enumerate(mp3_files):
            self.track_list.append(file_path)
            playlist_widget.append(SongItem(file_path, index))

    def play_track(self, index: int) -> None:
        """Play a track at a specific index and extract metadata."""
        if 0 <= index < len(self.track_list):
            file_to_play = self.track_list[index]
            success, length = self.audio.load_and_play(file_to_play)
            
            if success:
                self.track_length = length
                self.current_track_index = index
                
                # Extract Metadata for UI (Title, Artist)
                title = file_to_play.stem
                artist = "Unknown Artist"
                try:
                    meta = mutagen.File(file_to_play, easy=True)
                    if meta:
                        title = meta.get("title", [title])[0]
                        artist = meta.get("artist", [artist])[0]
                except Exception:
                    pass

                # Update Text UI
                self.query_one("#track-title", Label).update(f"{title}")
                self.query_one("#track-artist", Label).update(f"{artist}")
                self.query_one("#play-pause", Button).label = "PAUSE ||"
                
                # --- ARTWORK CODE ---
                # This explicitly calls the image generator we built!
                artwork_renderable = self.generate_artwork_text(file_to_play)
                self.query_one("#artwork", Static).update(artwork_renderable)
                # --------------------
                
                # Reset and configure Progress Bar
                pb = self.query_one(ProgressBar)
                pb.total = self.track_length
                pb.progress = 0
                
                # Start the UI timer to update progress every 0.5 seconds
                if self.progress_timer is not None:
                    self.progress_timer.stop()
                self.progress_timer = self.set_interval(0.5, self.update_progress)
                
                # Update Highlight in Playlist
                playlist_widget = self.query_one("#playlist", ListView)
                for child in playlist_widget.children:
                    child.remove_class("now-playing")
                
                try:
                    new_item = playlist_widget.query_one(f"#song-{index}")
                    new_item.add_class("now-playing")
                except Exception:
                    pass
        else:
            self.audio.stop()
            self.current_track_index = -1
            self.query_one("#track-title", Label).update("Finished Playlist")
            self.query_one("#play-pause", Button).label = "PLAY >"
            if self.progress_timer is not None:
                self.progress_timer.stop()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        
        if button_id == "play-pause":
            if self.audio.current_track is None and len(self.track_list) > 0:
                self.play_track(0)
            else:
                self.audio.toggle_pause()
                if self.audio.is_paused:
                    event.button.label = "|>"
                else:
                    event.button.label = "||"
        
        elif button_id == "next":
            if len(self.track_list) > 0:
                self.play_track((self.current_track_index + 1) % len(self.track_list))

        elif button_id == "prev":
            if len(self.track_list) > 0:
                self.play_track((self.current_track_index - 1 + len(self.track_list)) % len(self.track_list))

    def on_list_view_selected(self,event: ListView.Selected):
        if isinstance(event.item, SongItem):
            self.play_track(event.item.index)

    def update_progress(self)->None:
        if self.audio.current_track and not self.audio.is_paused and pygame.mixer.music.get_busy():
            current_ms = pygame.mixer.music.get_pos()
            if current_ms >= 0:
                current_sec = current_ms / 1000

                cur_m,cur_s=divmod(int(current_sec),60)
                tol_m,tol_s = divmod(int(self.track_length),60)

                self.query_one("#time-elapsed",Label).update(f"{cur_m:02}:{cur_s:02}")
                self.query_one("#time-total",Label).update(f"{tol_m:02}:{tol_s:02}")

                pb = self.query_one(ProgressBar)
                pb.progress = current_sec

    def generate_artwork_text(self, file_path: Path, width: int = 34, height: int = 14) -> Text | str:
        """Extracts MP3 cover art and converts it to colored terminal blocks using Pygame."""
        try:
            audio = mutagen.File(file_path)
            artwork_data = None
            mime_type = "image/jpeg" # Default fallback
            
            if audio and audio.tags:
                for tag in audio.tags.values():
                    # Look for APIC (Attached Picture) frame in ID3 tags
                    if hasattr(tag, 'data') and hasattr(tag, 'mime'):
                        artwork_data = tag.data
                        mime_type = tag.mime.lower()
                        break
                        
            if not artwork_data:
                return "[ ALBUM ]\n\nNo Cover Art embedded in this MP3 file."

            # Determine the correct hint based on the MP3's metadata
            hint = ".jpg"
            if "png" in mime_type:
                hint = ".png"

            # Pass the correct hint to Pygame so it uses the right decoder
            try:
                img = pygame.image.load(io.BytesIO(artwork_data), hint)
            except Exception as img_err:
                return f"[ ALBUM ]\n\nImage Decode Error:\n{str(img_err)}"
                
            img = pygame.transform.scale(img, (width, height * 2))

            text = Text()
            for y in range(0, height * 2, 2):
                for x in range(width):
                    p1 = img.get_at((x, y))
                    r1, g1, b1 = p1.r, p1.g, p1.b
                    
                    if y + 1 < height * 2:
                        p2 = img.get_at((x, y + 1))
                        r2, g2, b2 = p2.r, p2.g, p2.b
                        text.append("▄", style=f"color:rgb({r2},{g2},{b2}) on rgb({r1},{g1},{b1})")
                    else:
                        text.append(" ", style=f"on rgb({r1},{g1},{b1})")
                text.append("\n")
            return text
        except Exception as e:
            return f"[ ALBUM ]\n\nCrash:\n{str(e)}"

    def action_play_pause(self) -> None:
        """Handle the spacebar to play/pause."""
        if self.audio.current_track is None and len(self.track_list) > 0:
            self.play_track(0)
        else:
            self.audio.toggle_pause()
            button = self.query_one("#play-pause", Button)
            if self.audio.is_paused:
                button.label = "PLAY >"
            else:
                button.label = "PAUSE ||"

    def action_next_track(self) -> None:
        """Handle the 'n' key for next track."""
        if len(self.track_list) > 0:
            self.play_track((self.current_track_index + 1) % len(self.track_list))

    def action_prev_track(self) -> None:
        """Handle the 'p' key for previous track."""
        if len(self.track_list) > 0:
            self.play_track((self.current_track_index - 1 + len(self.track_list)) % len(self.track_list))


app = MusicPlayer()
app.run()
