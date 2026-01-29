"""
Script to add more outfit sets for various styles.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompt_gen.generator import PromptGenerator

gen = PromptGenerator()

# Outfit sets organized by style
outfit_sets = {
    "Jirai Kei": [
        {
            "name": "Dark Princess",
            "items": ["black lace blouse", "black tiered skirt", "platform boots", "cross necklace", "black lace stockings"]
        },
        {
            "name": "Pink Doll",
            "items": ["pink frill top with bow", "pink plaid mini skirt", "chunky sneakers", "heart pendant", "over-knee socks"]
        },
        {
            "name": "Broken Heart",
            "items": ["off-shoulder sweater", "suspender skirt", "lace-up boots", "velvet choker", "bandaid on cheek"]
        },
        {
            "name": "Midnight Tears",
            "items": ["mesh top layered", "black tiered skirt", "combat boots", "cross necklace", "fake tears sticker"]
        },
        {
            "name": "Sweet Nightmare",
            "items": ["cropped cardigan with heart buttons", "lace trim bloomers", "platform sneakers", "rabbit ear headband", "arm warmers with ribbons"]
        },
    ],
    
    "Gothic Lolita": [
        {
            "name": "Victorian Mourning",
            "items": ["victorian blouse with jabot", "bell-shaped petticoat skirt", "knee high boots", "cameo brooch", "mini top hat"]
        },
        {
            "name": "Dark Rose",
            "items": ["corseted bodice", "high-low skirt with lace trim", "lace-up boots", "rose hairpin", "lace parasol"]
        },
        {
            "name": "Phantom Doll",
            "items": ["puff sleeve blouse", "bell-shaped petticoat skirt", "ankle boots", "pocket watch", "bonnet"]
        },
        {
            "name": "Midnight Cathedral",
            "items": ["victorian blouse with jabot", "bloomers with lace", "combat boots", "cross necklace", "veil"]
        },
    ],
    
    "Casual": [
        {
            "name": "Weekend Vibes",
            "items": ["white t-shirt", "denim skirt", "canvas shoes", "scrunchie", "canvas tote"]
        },
        {
            "name": "Coffee Date",
            "items": ["cardigan", "tennis skirt", "ballet flats", "earrings", "chain bag"]
        },
        {
            "name": "Lazy Sunday",
            "items": ["off-shoulder sweater", "shorts", "chunky sneakers", "bucket hat", "mini backpack"]
        },
        {
            "name": "Spring Walk",
            "items": ["lace blouse", "flared skirt", "wedge sandals", "straw hat", "basket bag"]
        },
        {
            "name": "City Explorer",
            "items": ["bomber jacket", "high waist pants", "ankle boots", "sunglasses", "fanny pack"]
        },
    ],
    
    "Streetwear": [
        {
            "name": "Tokyo Night",
            "items": ["leather jacket", "cargo pants", "combat boots", "chain necklace", "fanny pack"]
        },
        {
            "name": "Hypebeast",
            "items": ["band t-shirt", "baggy pants", "chunky sneakers", "bucket hat", "clear bag"]
        },
        {
            "name": "Urban Edge",
            "items": ["cropped hoodie", "distressed jeans", "platform sneakers", "hoop earrings", "mini backpack"]
        },
        {
            "name": "Skater Style",
            "items": ["tank top", "cargo pants", "canvas shoes", "bandana headband", "canvas tote"]
        },
    ],
    
    "Lady": [
        {
            "name": "Elegant Tea Party",
            "items": ["lace blouse", "tulle skirt", "strappy heels", "pearl earrings", "envelope clutch"]
        },
        {
            "name": "Garden Romance",
            "items": ["peter pan collar blouse", "circle skirt", "ballet flats", "flower crown", "basket bag"]
        },
        {
            "name": "Parisian Chic",
            "items": ["turtleneck sweater", "wide leg pants", "ankle boots", "silk scarf", "chain bag"]
        },
        {
            "name": "Vintage Dream",
            "items": ["polka dot blouse", "poodle skirt", "wedge sandals", "fascinator", "envelope clutch"]
        },
    ],
    
    "Mature": [
        {
            "name": "Executive Power",
            "items": ["tuxedo jacket", "high waist pants", "strappy heels", "ring collection", "envelope clutch"]
        },
        {
            "name": "Evening Glamour",
            "items": ["slip dress", "strappy heels", "dangle earrings", "fur collar", "chain bag"]
        },
        {
            "name": "Sophisticated Edge",
            "items": ["leather jacket", "leather skirt", "knee high boots", "hoop earrings", "envelope clutch"]
        },
    ],
    
    "Cyberpunk": [
        {
            "name": "Neon Runner",
            "items": ["holographic crop top", "techwear cargo pants", "combat boots", "LED glasses", "holographic wristband"]
        },
        {
            "name": "Tech Noir",
            "items": ["tech vest with LED", "LED strip pants", "combat boots", "cybernetic eye patch", "glowing earpiece"]
        },
        {
            "name": "Digital Ghost",
            "items": ["neon trim jacket", "holographic skirt", "platform sneakers", "VR headset", "body chain"]
        },
    ],
    
    "School Uniform": [
        {
            "name": "Classic Academy",
            "items": ["sailor collar top", "tennis skirt", "canvas shoes", "loose socks", "leather satchel"]
        },
        {
            "name": "Winter Uniform",
            "items": ["cardigan", "tennis skirt", "ankle boots", "over-knee socks", "leather satchel"]
        },
        {
            "name": "Summer Sailor",
            "items": ["sailor collar top", "tennis skirt", "canvas shoes", "scrunchie", "canvas tote"]
        },
    ],
    
    "Maid": [
        {
            "name": "Classic Maid",
            "items": ["classic maid blouse", "frilly apron", "ankle boots", "maid headdress", "feather duster"]
        },
        {
            "name": "French Maid",
            "items": ["puffy sleeve maid top", "frilly apron", "strappy heels", "ruffled headpiece", "serving tray"]
        },
    ],
    
    "Office Lady": [
        {
            "name": "Corporate Chic",
            "items": ["turtleneck sweater", "high waist pants", "strappy heels", "round glasses", "leather satchel"]
        },
        {
            "name": "Meeting Ready",
            "items": ["lace blouse", "pinstripe trousers", "ankle boots", "silk scarf", "envelope clutch"]
        },
    ],
    
    "Fantasy": [
        {
            "name": "Forest Elf",
            "items": ["peasant blouse", "tulle skirt", "ballet flats", "flower crown", "cape"]
        },
        {
            "name": "Dark Sorceress",
            "items": ["corseted bodice", "tulle skirt", "knee high boots", "crown of thorns", "cape"]
        },
        {
            "name": "Celestial Maiden",
            "items": ["slip dress", "sheer stockings", "ballet flats", "tiara", "opera gloves"]
        },
    ],
}

def main():
    print("Adding outfit sets...")
    added_count = 0
    
    for style, sets in outfit_sets.items():
        print(f"\n== {style} ==")
        for outfit_set in sets:
            if gen.add_outfit_set(style, outfit_set['name'], outfit_set['items']):
                print(f"  + Added: {outfit_set['name']}")
                added_count += 1
    
    print(f"\nDone! Added {added_count} new outfit sets.")

if __name__ == "__main__":
    main()
