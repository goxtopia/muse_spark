"""
Script to add more outfit sets - batch 2.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompt_gen.generator import PromptGenerator

gen = PromptGenerator()

# More outfit sets
outfit_sets = {
    "Jirai Kei": [
        {
            "name": "Hospital Doll",
            "items": ["white off-shoulder top", "pink plaid mini skirt", "platform boots", "bandaid on cheek", "mini backpack"]
        },
        {
            "name": "Starry Night",
            "items": ["black lace blouse with ribbon", "suspender skirt", "lace-up boots", "star stickers on face", "plush bag"]
        },
        {
            "name": "Yami Kawaii",
            "items": ["pink frill top with bow", "heart print shorts", "chunky sneakers", "multiple ear piercings", "bear plushie keychain"]
        },
        {
            "name": "Melty Heart",
            "items": ["off-shoulder ruffle blouse", "black tiered skirt", "platform sneakers", "heart-shaped sunglasses", "chain bag"]
        },
    ],
    
    "Gothic Lolita": [
        {
            "name": "Vampire Bride",
            "items": ["corseted bodice", "bell-shaped petticoat skirt", "knee high boots", "veil", "cross earrings"]
        },
        {
            "name": "Clockwork Doll",
            "items": ["puff sleeve blouse", "high-low skirt with lace trim", "lace-up boots", "pocket watch", "monocle"]
        },
        {
            "name": "Noir Butterfly",
            "items": ["victorian blouse with jabot", "bloomers with lace", "ankle boots", "butterfly clips", "lace parasol"]
        },
    ],
    
    "Casual": [
        {
            "name": "Picnic Day",
            "items": ["polka dot blouse", "denim skirt", "wedge sandals", "straw hat", "basket bag"]
        },
        {
            "name": "Library Mouse",
            "items": ["turtleneck sweater", "wide leg pants", "ballet flats", "round glasses", "canvas tote"]
        },
        {
            "name": "Beach Ready",
            "items": ["tank top", "shorts", "wedge sandals", "sunglasses", "clear bag"]
        },
        {
            "name": "Rainy Day",
            "items": ["cardigan", "high waist pants", "ankle boots", "bucket hat", "mini backpack"]
        },
        {
            "name": "Night Out",
            "items": ["camisole", "flared skirt", "strappy heels", "earrings", "envelope clutch"]
        },
    ],
    
    "Streetwear": [
        {
            "name": "Graffiti Artist",
            "items": ["tie-dye shirt", "cargo pants", "chunky sneakers", "bandana headband", "fanny pack"]
        },
        {
            "name": "Midnight Rider",
            "items": ["leather jacket", "distressed jeans", "combat boots", "spike bracelet", "chain bag"]
        },
        {
            "name": "Neon Dreams",
            "items": ["cropped hoodie", "baggy pants", "platform sneakers", "face mask", "clear bag"]
        },
        {
            "name": "Vintage Mix",
            "items": ["band t-shirt", "tennis skirt", "canvas shoes", "safety pin earrings", "mini backpack"]
        },
    ],
    
    "Lady": [
        {
            "name": "Rose Garden",
            "items": ["ruffle front blouse", "tulle skirt", "ballet flats", "rose hairpin", "basket bag"]
        },
        {
            "name": "Opera Night",
            "items": ["slip dress", "strappy heels", "dangle earrings", "opera gloves", "envelope clutch"]
        },
        {
            "name": "Sunday Brunch",
            "items": ["peter pan collar blouse", "circle skirt", "wedge sandals", "pearl earrings", "chain bag"]
        },
        {
            "name": "Autumn Elegance",
            "items": ["turtleneck sweater", "paper bag waist skirt", "ankle boots", "silk scarf", "leather satchel"]
        },
    ],
    
    "Mature": [
        {
            "name": "Noir Femme",
            "items": ["bustier top", "slit skirt", "strappy heels", "ring collection", "envelope clutch"]
        },
        {
            "name": "Power Meeting",
            "items": ["trench coat", "pinstripe trousers", "strappy heels", "round glasses", "leather satchel"]
        },
        {
            "name": "Cocktail Hour",
            "items": ["halter neck top", "palazzo pants", "strappy heels", "layered necklaces", "chain bag"]
        },
    ],
    
    "Cyberpunk": [
        {
            "name": "Data Runner",
            "items": ["cybernetic arm sleeve", "techwear cargo pants", "combat boots", "ear cuff", "fanny pack"]
        },
        {
            "name": "Hologram Girl",
            "items": ["holographic crop top", "holographic skirt", "platform sneakers", "LED glasses", "wrist wallet"]
        },
        {
            "name": "Neural Link",
            "items": ["mesh long sleeve", "LED strip pants", "combat boots", "glowing earpiece", "body chain"]
        },
    ],
    
    "School Uniform": [
        {
            "name": "Art Club",
            "items": ["sailor collar top", "suspender skirt", "canvas shoes", "hair pin set", "canvas tote"]
        },
        {
            "name": "Library Committee",
            "items": ["cardigan", "tennis skirt", "ballet flats", "round glasses", "leather satchel"]
        },
        {
            "name": "After School",
            "items": ["sailor collar top", "tennis skirt", "chunky sneakers", "loose socks", "mini backpack"]
        },
    ],
    
    "Maid": [
        {
            "name": "Cafe Maid",
            "items": ["puffy sleeve maid top", "frilly apron", "ballet flats", "maid headdress", "serving tray"]
        },
        {
            "name": "Gothic Maid",
            "items": ["classic maid blouse", "frilly apron", "combat boots", "ruffled headpiece", "cross necklace"]
        },
    ],
    
    "Office Lady": [
        {
            "name": "First Day",
            "items": ["white t-shirt", "high waist pants", "ankle boots", "earrings", "leather satchel"]
        },
        {
            "name": "Casual Friday",
            "items": ["cardigan", "wide leg pants", "ballet flats", "round glasses", "canvas tote"]
        },
        {
            "name": "After Work Drinks",
            "items": ["lace blouse", "leather skirt", "strappy heels", "hoop earrings", "chain bag"]
        },
    ],
    
    "Fantasy": [
        {
            "name": "Moon Priestess",
            "items": ["peasant blouse", "tulle skirt", "ballet flats", "tiara", "wagasa Japanese umbrella"]
        },
        {
            "name": "Witch's Apprentice",
            "items": ["capelet", "suspender skirt", "lace-up boots", "witch hat", "book-shaped bag"]
        },
        {
            "name": "Fairy Queen",
            "items": ["slip dress", "shimmer tights", "ballet flats", "flower crown", "cape"]
        },
        {
            "name": "Dark Knight",
            "items": ["military jacket", "leather skirt", "combat boots", "crown of thorns", "leg harness"]
        },
    ],
}

def main():
    print("Adding more outfit sets (batch 2)...")
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
