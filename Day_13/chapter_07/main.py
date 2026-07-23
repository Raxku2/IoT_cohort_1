from rich import console, print
from rich.columns import Columns
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
 

console = Console()
input = Prompt.ask

INVENTORY = [
    # --- PRODUCE ---
    {
        "item_name": "Honeycrisp Apples",
        "rate": 3.99,
        "unit": "lb",
        "description": "Sweet, crisp, and organically grown apples.",
        "category": "Produce"
    },
    {
        "item_name": "Cavendish Bananas",
        "rate": 0.59,
        "unit": "lb",
        "description": "Yellow, perfectly ripe bananas.",
        "category": "Produce"
    },
    {
        "item_name": "Baby Spinach",
        "rate": 4.50,
        "unit": "box",
        "description": "Pre-washed organic baby spinach leaves.",
        "category": "Produce"
    },
    {
        "item_name": "Garlic Bulbs",
        "rate": 0.75,
        "unit": "piece",
        "description": "Fresh, whole garlic bulbs.",
        "category": "Produce"
    },

    # --- DAIRY & EGGS ---
    {
        "item_name": "Whole Milk",
        "rate": 3.20,
        "unit": "gallon",
        "description": "Vitamin D fortified whole cow's milk.",
        "category": "Dairy"
    },
    {
        "item_name": "Large Grade A Eggs",
        "rate": 4.10,
        "unit": "dozen",
        "description": "Free-range brown eggs.",
        "category": "Dairy"
    },
    {
        "item_name": "Sharp Cheddar Cheese",
        "rate": 5.50,
        "unit": "block",
        "description": "Aged for 12 months, sharp and crumbly.",
        "category": "Dairy"
    },
    {
        "item_name": "Unsalted Butter",
        "rate": 4.80,
        "unit": "lb",
        "description": "Sweet cream unsalted butter, 4 sticks.",
        "category": "Dairy"
    },

    # --- MEAT & SEAFOOD ---
    {
        "item_name": "Boneless Chicken Breast",
        "rate": 5.99,
        "unit": "lb",
        "description": "Air-chilled, skinless chicken breast.",
        "category": "Meat"
    },
    {
        "item_name": "Ground Beef (80/20)",
        "rate": 4.99,
        "unit": "lb",
        "description": "80% lean ground chuck beef.",
        "category": "Meat"
    },
    {
        "item_name": "Atlantic Salmon Fillet",
        "rate": 12.99,
        "unit": "lb",
        "description": "Fresh, farm-raised Atlantic salmon.",
        "category": "Seafood"
    },

    # --- PANTRY ---
    {
        "item_name": "Extra Virgin Olive Oil",
        "rate": 14.50,
        "unit": "bottle (750ml)",
        "description": "Cold-pressed, unrefined olive oil.",
        "category": "Pantry"
    },
    {
        "item_name": "Jasmine Rice",
        "rate": 8.00,
        "unit": "bag (5 lb)",
        "description": "Aromatic long-grain white rice.",
        "category": "Pantry"
    },
    {
        "item_name": "Spaghetti Pasta",
        "rate": 1.99,
        "unit": "box (16 oz)",
        "description": "Enriched macaroni product made with durum wheat.",
        "category": "Pantry"
    },
    {
        "item_name": "Canned Black Beans",
        "rate": 1.25,
        "unit": "can (15 oz)",
        "description": "Low-sodium black beans in water.",
        "category": "Pantry"
    },
    {
        "item_name": "All-Purpose Flour",
        "rate": 3.50,
        "unit": "bag (5 lb)",
        "description": "Unbleached all-purpose baking flour.",
        "category": "Pantry"
    },

    # --- SNACKS & BEVERAGES ---
    {
        "item_name": "Whole Bean Coffee",
        "rate": 11.99,
        "unit": "bag (12 oz)",
        "description": "Dark roast Colombian whole bean coffee.",
        "category": "Beverages"
    },
    {
        "item_name": "Dark Chocolate Bar",
        "rate": 3.00,
        "unit": "bar",
        "description": "72% cacao dark chocolate with sea salt.",
        "category": "Snacks"
    },

    # --- HOUSEHOLD ---
    {
        "item_name": "Paper Towels",
        "rate": 18.50,
        "unit": "pack (8 rolls)",
        "description": "Ultra-absorbent 2-ply paper towels.",
        "category": "Household"
    },
    {
        "item_name": "Liquid Dish Soap",
        "rate": 4.25,
        "unit": "bottle (24 oz)",
        "description": "Grease-fighting citrus-scented dish soap.",
        "category": "Household"
    }
]


APP_LOGO = """
██████╗ ██╗██╗     ██╗     ██╗███╗   ██╗ ██████╗      █████╗ ██████╗ ██████╗ 
██╔══██╗██║██║     ██║     ██║████╗  ██║██╔════╝     ██╔══██╗██╔══██╗██╔══██╗
██████╔╝██║██║     ██║     ██║██╔██╗ ██║██║  ███╗    ███████║██████╔╝██████╔╝
██╔══██╗██║██║     ██║     ██║██║╚██╗██║██║   ██║    ██╔══██║██╔═══╝ ██╔═══╝ 
██████╔╝██║███████╗███████╗██║██║ ╚████║╚██████╔╝    ██║  ██║██║     ██║     
╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═╝╚═╝     ╚═╝     
"""

def showInvoice():
    print("[yellow]Feature Not Available[/yellow]")


def showItems():
    for index,item in enumerate(INVENTORY):
        print(f"{index+1} >> [green]{item.get('item_name')}[/green]")

def makeInvoice() -> list[int]:
    showItems()
    busket = []
    while True:
        userChoice = input("Enter Product ID (q:quit|d:Done) ")
        if userChoice.lower() == 'q':
            exit()
        if userChoice.lower() == 'd':
            break
        if userChoice.isnumeric() and int(userChoice) <= len(INVENTORY):
            busket.append(int(userChoice))
        else:
            print("[yellow]Invalid Product ID!![/yellow]")
    return busket




console.clear()
print(f"[green]{APP_LOGO}[/]")    
while True:
    userChoice = input("Select a option", choices=['1','2','q'], default='1' )
    if userChoice == '1':
        busket = makeInvoice()
        # print(busket)
        bill:float = 0
        for i in busket:
            print(f"{INVENTORY[i-1].get('item_name')}\t {INVENTORY[i-1].get('rate')}")
            bill += float(INVENTORY[i-1].get('rate'))
        print(f"Total {bill}")
            


    elif userChoice == '2':
        showInvoice()
    elif userChoice == 'q':
        exit()
    else:
        print("[red]Invalid Input[/red]")
        continue
    
    
    
