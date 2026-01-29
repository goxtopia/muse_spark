"""
Script to add more unique/niche outfit items.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompt_gen.generator import PromptGenerator

gen = PromptGenerator()

# ========== Traditional/Cultural ==========
traditional_items = {
    "full_body": [
        ("furisode kimono", ["Fantasy", "Lady"]),
        ("yukata with obi", ["Casual", "Lady"]),
        ("hakama and haori", ["Fantasy"]),
        ("hanbok", ["Fantasy", "Lady"]),
        ("qipao/cheongsam", ["Lady", "Mature"]),
        ("ao dai", ["Lady"]),
        ("dirndl", ["Lady", "Fantasy"]),
        ("sari", ["Lady", "Fantasy"]),
        ("hanfu", ["Fantasy", "Lady"]),
        ("viking dress", ["Fantasy"]),
        ("medieval gown", ["Fantasy", "Gothic Lolita"]),
    ],
    "accessories": [
        ("kanzashi hair ornament", ["Fantasy", "Lady"]),
        ("folding fan", ["Lady", "Fantasy", "Gothic Lolita"]),
        ("wagasa Japanese umbrella", ["Fantasy", "Lady"]),
        ("geta sandals", ["Fantasy", "Casual"]),
        ("zori sandals", ["Fantasy", "Lady"]),
        ("jade pendant", ["Lady", "Fantasy"]),
    ],
}

# ========== Sporty/Athletic ==========
sporty_items = {
    "top": [
        ("sports bra", ["Casual", "Streetwear"]),
        ("tennis polo", ["Casual"]),
        ("jersey", ["Casual", "Streetwear"]),
        ("swim top bikini", ["Casual"]),
        ("wetsuit top", ["Casual"]),
        ("cycling jersey", ["Casual"]),
        ("cheerleader top", ["School Uniform", "Casual"]),
    ],
    "bottom": [
        ("yoga pants", ["Casual"]),
        ("running shorts", ["Casual"]),
        ("tennis shorts", ["Casual"]),
        ("swim bottom bikini", ["Casual"]),
        ("cycling shorts", ["Casual"]),
        ("cheerleader skirt", ["School Uniform", "Casual"]),
    ],
    "full_body": [
        ("one-piece swimsuit", ["Casual"]),
        ("school swimsuit", ["School Uniform"]),
        ("competition swimsuit", ["Casual"]),
        ("leotard", ["Casual", "Fantasy"]),
        ("gymnastics unitard", ["Casual"]),
        ("tennis dress", ["Casual", "Lady"]),
    ],
}

# ========== Subculture/Alt Fashion ==========
alt_items = {
    "top": [
        ("band t-shirt", ["Streetwear", "Casual"]),
        ("mesh long sleeve", ["Cyberpunk", "Gothic Lolita"]),
        ("shrug bolero", ["Gothic Lolita", "Lady"]),
        ("tie-dye shirt", ["Casual", "Streetwear"]),
        ("cropped hoodie", ["Streetwear", "Jirai Kei"]),
        ("halter neck top", ["Casual", "Cyberpunk"]),
        ("asymmetric top", ["Cyberpunk", "Streetwear"]),
        ("deconstructed shirt", ["Cyberpunk", "Streetwear"]),
    ],
    "bottom": [
        ("distressed jeans", ["Streetwear", "Casual"]),
        ("baggy pants", ["Streetwear"]),
        ("slit skirt", ["Mature", "Lady"]),
        ("layered tutu", ["Gothic Lolita", "Jirai Kei"]),
        ("asymmetric skirt", ["Cyberpunk", "Gothic Lolita"]),
        ("palazzo pants", ["Lady", "Mature"]),
    ],
    "accessories": [
        ("safety pin earrings", ["Streetwear", "Cyberpunk"]),
        ("spike bracelet", ["Gothic Lolita", "Cyberpunk"]),
        ("collar with chain", ["Gothic Lolita", "Cyberpunk"]),
        ("fingerless gloves", ["Streetwear", "Cyberpunk", "Gothic Lolita"]),
        ("platform sole geta", ["Jirai Kei", "Gothic Lolita"]),
        ("layered necklaces", ["Lady", "Casual"]),
        ("body chain", ["Cyberpunk", "Mature"]),
        ("ear cuff", ["Cyberpunk", "Streetwear"]),
    ],
}

# ========== Vintage/Retro ==========
vintage_items = {
    "top": [
        ("peter pan collar blouse", ["Lady", "Gothic Lolita"]),
        ("polka dot blouse", ["Lady", "Casual"]),
        ("ruffle front blouse", ["Lady", "Gothic Lolita"]),
        ("peasant blouse", ["Fantasy", "Casual"]),
        ("bustier top", ["Mature", "Gothic Lolita"]),
    ],
    "bottom": [
        ("circle skirt", ["Lady", "Casual"]),
        ("poodle skirt", ["Lady"]),
        ("paper bag waist skirt", ["Lady", "Casual"]),
        ("sailor pants", ["Lady", "Casual"]),
        ("pinstripe trousers", ["Office Lady", "Mature"]),
    ],
    "full_body": [
        ("50s swing dress", ["Lady"]),
        ("flapper dress", ["Lady", "Mature"]),
        ("pinafore dress", ["Casual", "School Uniform"]),
        ("wrap dress", ["Lady", "Mature", "Office Lady"]),
        ("shirt dress", ["Casual", "Office Lady"]),
        ("tea dress", ["Lady"]),
    ],
}

# ========== Unconventional/Unique ==========
unique_items = {
    "top": [
        ("cape", ["Fantasy", "Gothic Lolita"]),
        ("capelet", ["Gothic Lolita", "Lady"]),
        ("bolero jacket", ["Lady", "Gothic Lolita"]),
        ("tuxedo jacket", ["Mature", "Lady"]),
        ("military jacket", ["Streetwear", "Gothic Lolita"]),
        ("fur coat", ["Lady", "Mature"]),
        ("trench coat", ["Mature", "Office Lady"]),
        ("vinyl jacket", ["Cyberpunk"]),
    ],
    "bottom": [
        ("harem pants", ["Fantasy", "Casual"]),
        ("culottes", ["Lady", "Casual"]),
        ("hot pants", ["Casual", "Streetwear"]),
        ("overalls shorts", ["Casual"]),
        ("skort", ["Casual", "School Uniform"]),
    ],
    "full_body": [
        ("jumpsuit", ["Casual", "Streetwear"]),
        ("romper", ["Casual"]),
        ("overalls", ["Casual", "Streetwear"]),
        ("catsuit", ["Cyberpunk"]),
        ("bodysuit", ["Cyberpunk", "Mature"]),
        ("tunic dress", ["Casual", "Fantasy"]),
        ("slip dress", ["Mature", "Lady"]),
        ("babydoll dress", ["Jirai Kei", "Lady"]),
    ],
    "accessories": [
        ("monocle", ["Gothic Lolita", "Fantasy"]),
        ("opera gloves", ["Lady", "Gothic Lolita", "Mature"]),
        ("arm sleeves", ["Cyberpunk", "Jirai Kei"]),
        ("leg harness", ["Cyberpunk", "Gothic Lolita"]),
        ("suspenders", ["Casual", "Streetwear"]),
        ("waist chain", ["Casual", "Streetwear"]),
        ("belly chain", ["Casual", "Cyberpunk"]),
        ("face jewels", ["Fantasy", "Cyberpunk"]),
        ("temporary tattoos", ["Casualties", "Streetwear"]),
    ],
    "headwear": [
        ("fascinator", ["Lady"]),
        ("pillbox hat", ["Lady", "Mature"]),
        ("cloche hat", ["Lady"]),
        ("turban", ["Lady", "Mature"]),
        ("bonnet", ["Gothic Lolita", "Fantasy"]),
        ("witch hat", ["Fantasy", "Gothic Lolita"]),
        ("animal hood", ["Casual", "Jirai Kei"]),
        ("crown of thorns", ["Gothic Lolita", "Fantasy"]),
    ],
    "legwear": [
        ("leg wraps", ["Fantasy"]),
        ("thigh harness", ["Cyberpunk", "Gothic Lolita"]),
        ("sock garters", ["Gothic Lolita", "Jirai Kei"]),
        ("calf warmers", ["Casual", "Jirai Kei"]),
        ("shimmer tights", ["Lady", "Fantasy"]),
        ("cable knit socks", ["Casual", "Lady"]),
    ],
    "neckwear": [
        ("bib necklace", ["Lady"]),
        ("collar pins", ["Office Lady", "Gothic Lolita"]),
        ("cravat", ["Gothic Lolita"]),
        ("ascot", ["Lady", "Gothic Lolita"]),
        ("cape collar", ["Gothic Lolita", "Fantasy"]),
        ("fur collar", ["Lady", "Mature"]),
        ("leather collar", ["Cyberpunk", "Gothic Lolita"]),
    ],
    "bags": [
        ("coffin bag", ["Gothic Lolita"]),
        ("bat wing bag", ["Gothic Lolita", "Jirai Kei"]),
        ("book-shaped bag", ["Gothic Lolita", "Lady"]),
        ("violin case bag", ["Gothic Lolita"]),
        ("potion bottle bag", ["Fantasy", "Gothic Lolita"]),
        ("phone bag", ["Casual", "Streetwear"]),
        ("wrist wallet", ["Streetwear", "Casual"]),
    ],
}

def main():
    print("Adding more outfit items...")
    added_count = 0
    
    all_categories = [
        ("Traditional/Cultural", traditional_items),
        ("Sporty/Athletic", sporty_items),
        ("Alt Fashion", alt_items),
        ("Vintage/Retro", vintage_items),
        ("Unique/Unconventional", unique_items),
    ]
    
    for category_name, items_dict in all_categories:
        print(f"\n== {category_name} ==")
        for category, items in items_dict.items():
            for name, styles in items:
                if gen.add_outfit_item(category, name, styles):
                    print(f"  + [{category}] {name}")
                    added_count += 1
    
    print(f"\nDone! Added {added_count} new outfit items.")

if __name__ == "__main__":
    main()
