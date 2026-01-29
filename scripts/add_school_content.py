"""
Script to add more School Uniform items.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompt_gen.generator import PromptGenerator

gen = PromptGenerator()

school_items = {
    "top": [
        ("navy blazer with gold buttons", ["School Uniform", "Traditional"]),
        ("beige cable knit cardigan", ["School Uniform", "Casual", "Jirai Kei"]),
        ("grey v-neck sweater", ["School Uniform", "Casual"]),
        ("sailor top with red scarf", ["School Uniform", "Cosplay"]),
        ("sailor top with blue scarf", ["School Uniform"]),
        ("white button-down shirt short sleeve", ["School Uniform", "Casual"]),
        ("cream vest", ["School Uniform", "Casual"]),
        ("gym t-shirt with name tag", ["School Uniform", "Sporty"]),
        ("track jacket jersey", ["School Uniform", "Sporty", "Streetwear"]),
        ("black gakuran jacket", ["School Uniform", "Traditional"]),
        ("hoodie under blazer", ["School Uniform", "Streetwear"]),
        ("oversized school cardigan", ["School Uniform", "Casual", "Jirai Kei"]),
        ("polo shirt with emblem", ["School Uniform", "Casual"]),
        ("double-breasted blazer", ["School Uniform", "Mature"]),
        ("cropped sailor top", ["School Uniform", "Casual"]),
    ],
    "bottom": [
        ("navy pleated skirt", ["School Uniform", "Traditional"]),
        ("grey check skirt", ["School Uniform", "Casual"]),
        ("red plaid mini skirt", ["School Uniform", "Punk", "Jirai Kei"]),
        ("beige pleated skirt", ["School Uniform", "Casual"]),
        ("long sailor skirt", ["School Uniform", "Traditional"]),
        ("gym bloomers", ["School Uniform", "Sporty"]),
        ("navy track pants", ["School Uniform", "Sporty"]),
        ("burberry pattern skirt", ["School Uniform", "Casual"]),
        ("green plaid skirt", ["School Uniform", "Traditional"]),
        ("high-waisted suspender skirt", ["School Uniform", "Casual"]),
        ("micro mini pleated skirt", ["School Uniform", "Jirai Kei"]),
        ("slacks", ["School Uniform", "Traditional"]), # Boy style but worn by girls too
        ("culottes uniform", ["School Uniform"]),
    ],
    "neckwear": [
        ("red ribbon tie", ["School Uniform", "Jirai Kei"]),
        ("blue ribbon tie", ["School Uniform"]),
        ("striped necktie", ["School Uniform", "Casual"]),
        ("string tie", ["School Uniform"]),
        ("bolo tie school", ["School Uniform"]),
        ("loose necktie", ["School Uniform", "Casual"]),
    ],
    "shoes": [
        ("brown leather loafers", ["School Uniform", "Casual"]),
        ("black leather loafers", ["School Uniform", "Formal"]),
        ("haruta loafers", ["School Uniform"]),
        ("uwabaki (indoor shoes)", ["School Uniform"]),
        ("white sneakers", ["School Uniform", "Sporty"]),
        ("enamel shoes", ["School Uniform", "Jirai Kei"]),
    ],
    "legwear": [
        ("navy high socks", ["School Uniform"]),
        ("white crew socks", ["School Uniform", "Sporty"]),
        ("slouch socks (loose socks)", ["School Uniform", "Jirai Kei"]),
        ("black pantyhose", ["School Uniform", "Formal"]),
        ("socks with logo", ["School Uniform", "Casual"]),
    ],
    "bags": [
        ("leather school bag (randoseru style)", ["School Uniform"]),
        ("nylon shoulder bag", ["School Uniform", "Sporty"]),
        ("enamel sports bag", ["School Uniform", "Sporty"]),
        ("sub-bag (tote)", ["School Uniform", "Casual"]),
        ("brown leather satchel", ["School Uniform", "Traditional"]),
    ],
    "headwear": [
        ("school cap", ["School Uniform"]),
        ("helmet (bicycle commuting)", ["School Uniform"]),
    ],
    "accessories": [
        ("student council armband", ["School Uniform"]),
        ("safety pin", ["School Uniform", "Punk"]),
        ("bicycle key wristband", ["School Uniform"]),
        ("whistle", ["School Uniform", "Sporty"]),
        ("pass case", ["School Uniform", "Casual"]),
    ]
}

def main():
    print("Adding School Uniform items...")
    added_count = 0

    for category, items in school_items.items():
        for name, styles in items:
            if gen.add_outfit_item(category, name, styles):
                # print(f"  + [{category}] {name}")
                added_count += 1

    print(f"\nDone! Added {added_count} new School Uniform items.")

if __name__ == "__main__":
    main()
