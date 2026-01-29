"""
Script to add more outfit items for different styles.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompt_gen.generator import PromptGenerator

gen = PromptGenerator()

# ========== Universal/Multi-style Items ==========
universal_items = {
    "top": [
        ("white t-shirt", ["Casual", "Streetwear", "School Uniform"]),
        ("black t-shirt", ["Casual", "Streetwear", "Gothic Lolita"]),
        ("tank top", ["Casual", "Streetwear", "Cyberpunk"]),
        ("cardigan", ["Casual", "Lady", "School Uniform"]),
        ("denim jacket", ["Casual", "Streetwear"]),
        ("leather jacket", ["Streetwear", "Cyberpunk", "Mature"]),
        ("bomber jacket", ["Streetwear", "Casual"]),
        ("turtleneck sweater", ["Mature", "Lady", "Casual"]),
        ("off-shoulder sweater", ["Jirai Kei", "Lady", "Casual"]),
        ("lace blouse", ["Lady", "Gothic Lolita", "Jirai Kei"]),
        ("sailor collar top", ["School Uniform", "Jirai Kei"]),
        ("tube top", ["Casual", "Streetwear", "Cyberpunk"]),
        ("camisole", ["Casual", "Lady", "Jirai Kei"]),
    ],
    "bottom": [
        ("denim skirt", ["Casual", "Streetwear"]),
        ("tennis skirt", ["Casual", "School Uniform", "Streetwear"]),
        ("cargo pants", ["Streetwear", "Cyberpunk"]),
        ("wide leg pants", ["Mature", "Lady", "Streetwear"]),
        ("shorts", ["Casual", "Streetwear"]),
        ("high waist pants", ["Mature", "Office Lady"]),
        ("suspender skirt", ["Jirai Kei", "Gothic Lolita", "Casual"]),
        ("tulle skirt", ["Lady", "Gothic Lolita", "Fantasy"]),
        ("leather skirt", ["Cyberpunk", "Mature", "Gothic Lolita"]),
        ("flared skirt", ["Lady", "Casual", "Jirai Kei"]),
    ],
    "shoes": [
        ("chunky sneakers", ["Streetwear", "Casual", "Jirai Kei"]),
        ("ankle boots", ["Casual", "Mature", "Gothic Lolita"]),
        ("combat boots", ["Streetwear", "Cyberpunk", "Gothic Lolita"]),
        ("ballet flats", ["Lady", "Casual"]),
        ("strappy heels", ["Lady", "Mature"]),
        ("wedge sandals", ["Casual", "Lady"]),
        ("canvas shoes", ["Casual", "School Uniform"]),
        ("knee high boots", ["Mature", "Gothic Lolita", "Cyberpunk"]),
        ("platform sneakers", ["Jirai Kei", "Streetwear"]),
        ("lace-up boots", ["Gothic Lolita", "Jirai Kei"]),
    ],
    "legwear": [
        ("sheer stockings", ["Lady", "Mature", "Office Lady"]),
        ("patterned tights", ["Jirai Kei", "Gothic Lolita"]),
        ("lace stockings", ["Gothic Lolita", "Lady", "Jirai Kei"]),
        ("over-knee socks", ["Jirai Kei", "School Uniform"]),
        ("loose socks", ["School Uniform", "Jirai Kei"]),
        ("ankle high socks with lace", ["Gothic Lolita", "Lady"]),
        ("colorful striped stockings", ["Jirai Kei", "Gothic Lolita"]),
        ("ripped tights", ["Cyberpunk", "Streetwear"]),
        ("garter stockings", ["Gothic Lolita", "Mature"]),
    ],
    "neckwear": [
        ("silk scarf", ["Lady", "Mature", "Office Lady"]),
        ("bandana", ["Streetwear", "Casual"]),
        ("chain necklace", ["Streetwear", "Cyberpunk"]),
        ("cross necklace", ["Gothic Lolita", "Jirai Kei"]),
        ("heart pendant", ["Jirai Kei", "Casual"]),
        ("velvet choker", ["Gothic Lolita", "Jirai Kei"]),
        ("sailor collar", ["School Uniform", "Casual"]),
        ("bow tie", ["Lady", "Gothic Lolita", "Maid"]),
        ("lace collar", ["Gothic Lolita", "Lady"]),
    ],
    "headwear": [
        ("bucket hat", ["Casual", "Streetwear"]),
        ("straw hat", ["Casual", "Lady"]),
        ("newsboy cap", ["Casual", "Lady"]),
        ("cat ear hairband", ["Jirai Kei", "Cosplay"]),
        ("flower crown", ["Fantasy", "Lady"]),
        ("mini top hat", ["Gothic Lolita"]),
        ("rabbit ear headband", ["Jirai Kei", "Cosplay"]),
        ("bandana headband", ["Streetwear", "Casual"]),
        ("tiara", ["Lady", "Fantasy", "Gothic Lolita"]),
        ("veil", ["Gothic Lolita", "Fantasy"]),
    ],
    "accessories": [
        ("round glasses", ["Casual", "Office Lady"]),
        ("sunglasses", ["Casual", "Streetwear", "Mature"]),
        ("earrings", ["Lady", "Mature", "Casual"]),
        ("hoop earrings", ["Streetwear", "Mature"]),
        ("dangle earrings", ["Lady", "Gothic Lolita"]),
        ("hair pin set", ["Jirai Kei", "Lady"]),
        ("scrunchie", ["Casual", "School Uniform"]),
        ("bracelet stack", ["Casual", "Streetwear"]),
        ("anklet", ["Casual", "Lady"]),
        ("ring collection", ["Mature", "Lady", "Gothic Lolita"]),
        ("face mask", ["Streetwear", "Casual"]),
        ("bandaid on cheek", ["Jirai Kei"]),
        ("fake tears sticker", ["Jirai Kei"]),
    ],
    "bags": [
        ("canvas tote", ["Casual", "School Uniform"]),
        ("leather satchel", ["School Uniform", "Office Lady"]),
        ("chain bag", ["Mature", "Lady"]),
        ("mini backpack", ["Casual", "Streetwear", "Jirai Kei"]),
        ("clear bag", ["Casual", "Streetwear"]),
        ("basket bag", ["Lady", "Casual"]),
        ("envelope clutch", ["Lady", "Mature"]),
        ("plush bag", ["Jirai Kei", "Casual"]),
        ("fanny pack", ["Streetwear", "Casual"]),
    ],
}

# ========== Style-Specific Items ==========
jirai_kei_items = {
    "top": [
        ("black lace blouse with ribbon", ["Jirai Kei"]),
        ("pink frill top with bow", ["Jirai Kei"]),
        ("off-shoulder ruffle blouse", ["Jirai Kei"]),
        ("mesh top layered", ["Jirai Kei"]),
        ("cropped cardigan with heart buttons", ["Jirai Kei"]),
    ],
    "bottom": [
        ("pink plaid mini skirt", ["Jirai Kei"]),
        ("black tiered skirt", ["Jirai Kei"]),
        ("heart print shorts", ["Jirai Kei"]),
        ("lace trim bloomers", ["Jirai Kei"]),
    ],
    "accessories": [
        ("bear plushie keychain", ["Jirai Kei"]),
        ("heart-shaped sunglasses", ["Jirai Kei"]),
        ("star stickers on face", ["Jirai Kei"]),
        ("multiple ear piercings", ["Jirai Kei"]),
        ("arm warmers with ribbons", ["Jirai Kei"]),
    ],
}

gothic_lolita_items = {
    "top": [
        ("victorian blouse with jabot", ["Gothic Lolita"]),
        ("puff sleeve blouse", ["Gothic Lolita"]),
        ("corseted bodice", ["Gothic Lolita"]),
    ],
    "bottom": [
        ("bell-shaped petticoat skirt", ["Gothic Lolita"]),
        ("high-low skirt with lace trim", ["Gothic Lolita"]),
        ("bloomers with lace", ["Gothic Lolita"]),
    ],
    "accessories": [
        ("cameo brooch", ["Gothic Lolita"]),
        ("lace parasol", ["Gothic Lolita"]),
        ("pocket watch", ["Gothic Lolita"]),
        ("rose hairpin", ["Gothic Lolita"]),
        ("cross earrings", ["Gothic Lolita"]),
    ],
}

cyberpunk_items = {
    "top": [
        ("holographic crop top", ["Cyberpunk"]),
        ("tech vest with LED", ["Cyberpunk"]),
        ("cybernetic arm sleeve", ["Cyberpunk"]),
        ("neon trim jacket", ["Cyberpunk"]),
    ],
    "bottom": [
        ("techwear cargo pants", ["Cyberpunk"]),
        ("holographic skirt", ["Cyberpunk"]),
        ("LED strip pants", ["Cyberpunk"]),
    ],
    "accessories": [
        ("VR headset", ["Cyberpunk"]),
        ("glowing earpiece", ["Cyberpunk"]),
        ("LED glasses", ["Cyberpunk"]),
        ("holographic wristband", ["Cyberpunk"]),
        ("cybernetic eye patch", ["Cyberpunk"]),
    ],
}

maid_items = {
    "top": [
        ("classic maid blouse", ["Maid"]),
        ("frilly apron", ["Maid"]),
        ("puffy sleeve maid top", ["Maid"]),
    ],
    "headwear": [
        ("maid headdress", ["Maid"]),
        ("ruffled headpiece", ["Maid"]),
    ],
    "accessories": [
        ("feather duster", ["Maid"]),
        ("serving tray", ["Maid"]),
    ],
}

def main():
    print("Adding outfit items...")
    added_count = 0
    
    # Add universal items
    print("\n== Universal Items ==")
    for category, items in universal_items.items():
        for name, styles in items:
            if gen.add_outfit_item(category, name, styles):
                print(f"  + [{category}] {name}")
                added_count += 1
    
    # Add Jirai Kei items
    print("\n== Jirai Kei Items ==")
    for category, items in jirai_kei_items.items():
        for name, styles in items:
            if gen.add_outfit_item(category, name, styles):
                print(f"  + [{category}] {name}")
                added_count += 1
    
    # Add Gothic Lolita items
    print("\n== Gothic Lolita Items ==")
    for category, items in gothic_lolita_items.items():
        for name, styles in items:
            if gen.add_outfit_item(category, name, styles):
                print(f"  + [{category}] {name}")
                added_count += 1
    
    # Add Cyberpunk items
    print("\n== Cyberpunk Items ==")
    for category, items in cyberpunk_items.items():
        for name, styles in items:
            if gen.add_outfit_item(category, name, styles):
                print(f"  + [{category}] {name}")
                added_count += 1
    
    # Add Maid items
    print("\n== Maid Items ==")
    for category, items in maid_items.items():
        for name, styles in items:
            if gen.add_outfit_item(category, name, styles):
                print(f"  + [{category}] {name}")
                added_count += 1
    
    print(f"\nDone! Added {added_count} new outfit items.")

if __name__ == "__main__":
    main()
