# The Complete HTML Guide: From Basics to Mastery

Welcome to the comprehensive guide on HTML (HyperText Markup Language). This guide is designed to act as a standalone book or tutorial for your GitHub repository. It covers the core concepts of HTML, how the browser processes it, and provides a categorized, detailed reference for all useful HTML tags.

---

## Chapter 1: How HTML Works

HTML is the standard markup language used to create web pages. It describes the structure of a web page semantically. 

1. **The Request:** When you type a URL into your browser, it sends an HTTP request to a web server.
2. **The Response:** The server responds by sending back an HTML document (along with other resources like images, CSS, and JavaScript).
3. **Parsing:** The browser reads the HTML document from top to bottom. It translates the raw HTML text into a structured tree-like format.
4. **The DOM:** This tree structure is called the **Document Object Model (DOM)**. The DOM represents every element on the page as a node that can be interacted with.

---

## Chapter 2: Tags and Rendering

### What is a Tag?
A tag is the building block of HTML. It tells the browser how to format and display the content. Tags are enclosed in angle brackets `< >`. 

Most tags come in pairs:
* **Opening Tag:** `<tagname>` (e.g., `<p>`)
* **Closing Tag:** `</tagname>` (e.g., `</p>`)
* **Content:** The text or other tags nested between the opening and closing tags.
* **Attributes:** Placed in the opening tag to provide additional information (e.g., `<a href="link.html">`).

Some tags are **self-closing** (or "empty" elements) and do not wrap content (e.g., `<img>`, `<br>`, `<input>`).

### How Tags are Rendered
When a browser renders a page, it follows a specific pipeline:
1. **HTML to DOM:** The HTML markup is parsed into the DOM tree.
2. **CSS to CSSOM:** The browser parses all CSS (both user-defined and the browser's default internal stylesheet) into a CSS Object Model (CSSOM).
3. **Render Tree Construction:** The DOM and CSSOM are combined into a **Render Tree**. This tree contains only the nodes that will be visually displayed on the screen (e.g., `<head>` or elements with `display: none` are excluded).
4. **Layout (Reflow):** The browser calculates the exact geometry, size, and position of each node in the Render Tree based on the viewport size.
5. **Painting:** The browser converts the calculated nodes into actual pixels on your screen.

---

## Chapter 3: Categorized Tag Reference

HTML tags can be divided into two main conceptual categories based on how the browser's default stylesheet treats them visually.

### Category A: Tags with Inherent Size and Default Styling
These tags possess default margins, padding, typography styling (like bold text), or "intrinsic dimensions." **Intrinsic dimensions** apply to "replaced elements" like images or inputs, where the size is dictated by the external resource or the browser UI, rather than the surrounding text.

| Tag | Use Case | Description | Example |
| :--- | :--- | :--- | :--- |
| `<h1>` to `<h6>` | Headings | Represents section headings. `<h1>` is the largest and most important, `<h6>` is the smallest. They come with heavy default font weights and margins. | `<h1>Main Title</h1>` |
| `<p>` | Paragraphs | Used for blocks of text. Comes with built-in top and bottom margins to separate paragraphs. | `<p>This is a paragraph.</p>` |
| `<img>` | Images | Embeds an image. It has an intrinsic size based on the actual image file unless constrained by CSS. | `<img src="logo.png" alt="Logo">` |
| `<input>` | Form Input | An interactive control for user input. Its size and shape depend on the `type` attribute (text, radio, checkbox). | `<input type="text" placeholder="Name">` |
| `<button>` | Buttons | A clickable button. Comes with default browser styling (borders, background color, padding). | `<button>Submit</button>` |
| `<ul>` & `<ol>` | Lists | Unordered (bulleted) and Ordered (numbered) lists. They have default left padding and margins. | `<ul><li>Item 1</li></ul>` |
| `<li>` | List Item | Defines an item within a list. Inherits formatting from its parent list. | `<li>Apple</li>` |
| `<table>` | Data Tables | Represents tabular data. Browsers render tables with complex internal sizing rules based on content. | `<table>...</table>` |
| `<hr>` | Thematic Break | A horizontal rule (line) used to separate content. Has a default width (100%) and borders. | `<hr>` |
| `<textarea>` | Multi-line Input | A multi-line text input control. Can usually be resized by the user by default. | `<textarea rows="4"></textarea>` |
| `<select>` | Dropdown List | Creates a dropdown list. Renders with an OS-specific clickable UI box. | `<select><option>A</option></select>` |
| `<audio>` / `<video>` | Media playback | Embeds sound or video content. Has default dimensions and browser-specific media controls. | `<video src="vid.mp4" controls></video>` |
| `<figure>` | Self-contained Content | Represents self-contained content (like an image) with an optional caption (`<figcaption>`). Has default margins. | `<figure>...<figcaption>...</figcaption></figure>` |
| `<blockquote>` | Block Quotations | Indicates that the enclosed text is an extended quotation. Usually rendered with left and right indented margins. | `<blockquote>To be or not to be...</blockquote>` |
| `<pre>` | Preformatted Text | Displays text exactly as written in the HTML file, preserving spaces and line breaks. Uses a monospace font. | `<pre>Code block here</pre>` |
| `<canvas>` | Graphics | Used to draw graphics on the fly via JavaScript. Has default dimensions (300px wide, 150px high). | `<canvas id="myCanvas"></canvas>` |
| `<iframe>` | Inline Frame | Embeds another HTML page into the current one. Has a default width and height. | `<iframe src="https://example.com"></iframe>` |

---

### Category B: Structural, Semantic & Content-Dependent Tags
These tags are primarily used for document structure, semantic meaning, or wrapping text. They **do not have inherent size** beyond the text they contain. Block-level containers in this category will stretch to 100% width of their parent, but their *height* is entirely dependent on the content inside them. If they are empty, they take up 0 pixels of height.

| Tag | Use Case | Description | Example |
| :--- | :--- | :--- | :--- |
| `<div>` | Generic Block Container | A structural, block-level container with no special meaning. Purely used for grouping elements for CSS styling or JS manipulation. | `<div class="card">...</div>` |
| `<span>` | Generic Inline Container | An inline container used to wrap small sections of text or elements for styling without breaking the line flow. | `<span class="highlight">Text</span>` |
| `<header>` | Introductory Content | Represents introductory content or a set of navigational links for its nearest sectioning ancestor. | `<header>Logo and Nav here</header>` |
| `<footer>` | Closing Content | Represents the footer for its nearest section (e.g., copyright, links). | `<footer>© 2026 Company</footer>` |
| `<main>` | Dominant Content | Represents the dominant, main content of the `<body>`. There should only be one visible `<main>` per page. | `<main>Article content...</main>` |
| `<section>` | Thematic Grouping | A standalone section of a document, typically containing its own heading. | `<section id="about-us">...</section>` |
| `<article>` | Independent Content | Represents a self-contained composition that could be independently distributed (like a blog post or news story). | `<article>Blog Post...</article>` |
| `<aside>` | Tangential Content | Represents content indirectly related to the main content, like sidebars or callout boxes. | `<aside>Related Links...</aside>` |
| `<nav>` | Navigation Links | A section containing navigation links (menus, tables of contents). | `<nav><a href="/">Home</a></nav>` |
| `<a>` | Hyperlinks | Defines a hyperlink. Size is entirely dictated by the text or image inside it. | `<a href="link.html">Click Me</a>` |
| `<form>` | Form Wrapper | A semantic wrapper for input controls. Visually invisible unless styled with CSS. | `<form action="/submit">...</form>` |
| `<label>` | Input Labels | Provides a semantic label for a specific form input, improving accessibility. | `<label for="name">Name:</label>` |
| `<strong>` / `<b>` | Bold Text | Renders text strongly/boldly. `<strong>` implies semantic importance, `<b>` is just stylistic. | `<strong>Important!</strong>` |
| `<em>` / `<i>` | Italic Text | Renders text in italics. `<em>` implies emphasis (changes meaning), `<i>` is stylistic (like a foreign word). | `<em>Very</em> good.` |
| `<mark>` | Highlighted Text | Represents text highlighted or marked for reference purposes, like a yellow highlighter. | `Look at <mark>this</mark>.` |
| `<html>` | Root Element | The top-level element that encloses the entire HTML document. | `<html>...</html>` |
| `<head>` | Metadata Container | Contains metadata, titles, and links to scripts/styles. **It is never rendered visually on the screen.** | `<head><title>Page</title></head>` |
| `<body>` | Visible Content Container | Represents the content of an HTML document. Everything visually displayed goes in here. | `<body>...</body>` |
| `<script>` | JavaScript Logic | Used to embed or reference executable code (JavaScript). Has no visual footprint. | `<script>alert('Hi');</script>` |
| `<style>` | Internal CSS | Contains internal CSS styling information. Not rendered visually. | `<style> body { color: red; } </style>` |
| `<title>` | Document Title | Sets the title of the document (shown in the browser tab). Not rendered in the page body. | `<title>My Webpage</title>` |

---

## Summary
Understanding the distinction between elements that take up space by default (Category A) versus those that simply structure your document (Category B) is the key to mastering HTML layout. 

When you write HTML:
1. Use **Category B** tags to define the *meaning* and *skeleton* of your page layout (`<header>`, `<main>`, `<section>`, `<div>`).
2. Use **Category A** tags to populate that skeleton with actual *content* that the user interacts with or reads (`<h1>`, `<p>`, `<img>`, `<input>`).
3. Use **CSS** to override default behaviors and create beautiful, custom designs.
