"""
Script to add more outfit sets - batch 3.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompt_gen.generator import PromptGenerator

gen = PromptGenerator()

outfit_sets = {
    "Jirai Kei": [
        {
            "name": "White Angel",
            "items": ["white ruffle blouse", "white tiered skirt", "platform sneakers", "angel wings backpack", "white lace stockings"]
        },
        {
            "name": "Subway Idol",
            "items": ["oversized hoodie", "pleated mini skirt", "leg warmers", "loose socks", "mask", "smartphone"]
        },
    ],
    
    "Gothic Lolita": [
        {
            "name": "Shiro Lolita",
            "items": ["white victorian blouse", "white bell-shaped skirt", "white bonnet", "white tights", "white mary janes"]
        },
        {
            "name": "Military Lolita",
            "items": ["military jacket", "corseted bodice", "layered tutu", "knee high boots", "military hat"]
        },
    ],
    
    "Casual": [
        {
            "name": "Gym Class",
            "items": ["t-shirt", "gymnastics unitard", "running shorts", "sneakers", "wristbands"]
        },
        {
            "name": "Cozy Winter",
            "items": ["knit sweater", "long skirt", "ankle boots", "scarf", "earmuffs"]
        },
        {
            "name": "Summer Festival",
            "items": ["yukata with obi", "geta sandals", "hair pin set", "folding fan", "kinchaku bag"]
        },
    ],
    
    "Streetwear": [
        {
            "name": "Techwear Lite",
            "items": ["windbreaker", "cargo pants", "sneakers", "chest rig", "cap"]
        },
        {
            "name": "Dance Practice",
            "items": ["crop top", "sweatpants", "high-top sneakers", "cap", "duffel bag"]
        },
    ],

    "Lady": [
        {
            "name": "Wedding Guest",
            "items": ["cocktail dress", "heels", "clutch bag", "pearl necklace", "shawl"]
        },
        {
            "name": "Art Gallery",
            "items": ["minimalist dress", "statement necklace", "ankle boots", "tote bag"]
        },
    ],
    
    "Mature": [
        {
            "name": "Red Carpet",
            "items": ["evening gown", "stiletto heels", "diamond earrings", "clutch", "fur stole"]
        },
        {
            "name": "Business Trip",
            "items": ["blazer", "blouse", "pencil skirt", "heels", "carry-on suitcase"]
        },
    ],

    "Cyberpunk": [
        {
            "name": "Street Samurai",
            "items": ["kimono style jacket", "hakama pants", "tabi boots", "katana", "cybernetic arm"]
        },
        {
            "name": "Netrunner",
            "items": ["tight bodysuit", "visored helmet", "data jack cable", "glowing boots"]
        },
    ],

    "School Uniform": [
        {
            "name": "Cheerleader",
            "items": ["cheerleader top", "cheerleader skirt", "sneakers", "pom-poms", "high ponytail"]
        },
        {
            "name": "Kendo Club",
            "items": ["kendo gi", "hakama", "bogu armor", "shinai"]
        },
    ],
    
    "Maid": [
        {
            "name": "Cyber Maid",
            "items": ["latex maid dress", "glowing apron", "cybernetic headset", "platform boots"]
        },
        {
            "name": "Shrine Maiden",
            "items": ["white kimono top", "red hakama", "tabi", "zori", "broom"]
        },
    ],
    
    "Fantasy": [
        {
            "name": "Elven Princess",
            "items": ["elegant gown", "tiara", "cape", "bow and arrow", "leaf accessories"]
        },
        {
            "name": "Dragon Slayer",
            "items": ["plate armor", "cape", "greatsword", "boots", "gauntlets"]
        },
    ],
}

def main():
    print("Adding outfit sets (batch 3)...")
    added_count = 0
    
    for style, sets in outfit_sets.items():
        print(f"\n== {style} ==")
        for outfit_set in sets:
            # We use add_outfit_set which handles adding items if they don't exist too, usually.
            # However, looking at previous scripts, it seems generator.add_outfit_set just adds the set definition.
            # If items are missing from the global items list, they might need to be added separately or the system handles it.
            # Based on previous interactions, the system seems robust.
            if gen.add_outfit_set(style, outfit_set['name'], outfit_set['items']):
                print(f"  + Added: {outfit_set['name']}")
                added_count += 1
    
    print(f"\nDone! Added {added_count} new outfit sets.")

if __name__ == "__main__":
    main()
