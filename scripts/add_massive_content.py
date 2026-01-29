"""
Script to add massive amount of outfit items (100 Clothing, 100 Sets, 100 Accessories).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompt_gen.generator import PromptGenerator

gen = PromptGenerator()

# ==========================================
# 1. CLOTHING (100 items: Top, Bottom, Full Body)
# ==========================================

clothing_items = {
    "top": [
        ("striped polo shirt", ["Casual", "Streetwear"]),
        ("linen button-up", ["Casual", "Mature"]),
        ("oversized graphic hoodie", ["Streetwear", "Casual"]),
        ("cropped tank top", ["Streetwear", "Casual", "Cyberpunk"]),
        ("chiffon blouse", ["Lady", "Office Lady"]),
        ("knitted vest", ["School Uniform", "Casual"]),
        ("fleece jacket", ["Casual"]),
        ("puffer coat", ["Streetwear", "Casual"]),
        ("trench coat", ["Mature", "Office Lady"]),
        ("varsity jacket", ["Streetwear", "School Uniform"]),
        ("kimono cardigan", ["Casual", "Fantasy"]),
        ("peplum top", ["Lady", "Office Lady"]),
        ("halter neck top", ["Mature", "Lady"]),
        ("mesh bodysuit", ["Cyberpunk", "Streetwear"]),
        ("velvet blazer", ["Mature", "Gothic Lolita"]),
        ("satin camisole", ["Lady", "Mature"]),
        ("flannel shirt", ["Casual", "Streetwear"]),
        ("corset top", ["Gothic Lolita", "Lady"]),
        ("athletic jersey", ["Streetwear", "Casual"]),
        ("shearling jacket", ["Casual", "Mature"]),
        ("windbreaker", ["Streetwear", "Cyberpunk"]),
        ("poncho", ["Casual", "Fantasy"]),
        ("tweed jacket", ["Lady", "Office Lady"]),
        ("argyle sweater", ["School Uniform", "Casual"]),
        ("mock neck top", ["Mature", "Office Lady"]),
        ("tie-dye tee", ["Casual", "Streetwear"]),
        ("sequin top", ["Lady", "Cyberpunk"]),
        ("wrap blouse", ["Lady", "Office Lady"]),
        ("denim vest", ["Casual", "Streetwear"]),
        ("fur coat", ["Mature", "Lady"]),
        ("capelet", ["Gothic Lolita", "Fantasy"]),
        ("track jacket", ["Streetwear", "Casual"]),
        ("sleeveless hoodie", ["Streetwear", "Cyberpunk"]),
        ("ribbed bodysuit", ["Casual", "Lady"]),
        ("zip-up hoodie", ["Casual", "Streetwear"]),
    ],
    "bottom": [
        ("pleated midi skirt", ["Lady", "Office Lady"]),
        ("distressed jeans", ["Casual", "Streetwear"]),
        ("leather leggings", ["Cyberpunk", "Streetwear", "Mature"]),
        ("pencil skirt", ["Office Lady", "Mature"]),
        ("joggers", ["Streetwear", "Casual"]),
        ("culottes", ["Casual", "Office Lady"]),
        ("skater skirt", ["Casual", "School Uniform"]),
        ("bootcut jeans", ["Casual", "Mature"]),
        ("biker shorts", ["Streetwear", "Casual"]),
        ("maxi skirt", ["Lady", "Fantasy"]),
        ("corduroy pants", ["Casual", "School Uniform"]),
        ("harem pants", ["Casual", "Fantasy"]),
        ("high-waisted shorts", ["Casual", "Lady"]),
        ("cargo skirt", ["Streetwear", "Cyberpunk"]),
        ("plaid trousers", ["School Uniform", "Mature"]),
        ("mermaid skirt", ["Lady", "Mature"]),
        ("slacks", ["Office Lady", "Mature"]),
        ("tiered skirt", ["Bohemian", "Lady"]), # Added Bohemian implicitly or map to Casual
        ("vinyl pants", ["Cyberpunk", "Streetwear"]),
        ("wrap skirt", ["Lady", "Casual"]),
        ("bloomers", ["Gothic Lolita", "Maid"]),
        ("capri pants", ["Casual"]),
        ("parachute pants", ["Streetwear", "Cyberpunk"]),
        ("A-line skirt", ["Lady", "Office Lady", "School Uniform"]),
        ("button-front skirt", ["Casual", "Lady"]),
        ("paperbag waist pants", ["Office Lady", "Casual"]),
        ("drawstring shorts", ["Casual"]),
        ("fishtail skirt", ["Lady", "Mature"]),
        ("overall shorts", ["Casual"]),
        ("bell-bottoms", ["Retro", "Casual"]), # Added Retro implicitly or map to Casual
        ("sarong", ["Casual", "Fantasy"]),
        ("hakama pants", ["Fantasy", "Traditional"]), # Traditional implicitly
        ("kilt", ["School Uniform", "Streetwear"]),
        ("sweatpants", ["Casual", "Streetwear"]),
    ],
    "full_body": [
        ("sundress", ["Casual", "Lady"]),
        ("bodycon dress", ["Mature", "Lady", "Cyberpunk"]),
        ("shirt dress", ["Casual", "Office Lady"]),
        ("maxi dress", ["Lady", "Fantasy"]),
        ("jumpsuit", ["Streetwear", "Casual", "Office Lady"]),
        ("romper", ["Casual", "Lady"]),
        ("qipao", ["Traditional", "Lady"]), # Traditional implicitly
        ("evening gown", ["Lady", "Mature"]),
        ("overall dress", ["Casual", "School Uniform"]),
        ("boho dress", ["Casual", "Lady"]),
        ("slip dress", ["Mature", "Lady"]),
        ("lolita dress", ["Gothic Lolita"]),
        ("maid uniform", ["Maid"]),
        ("yukata", ["Traditional", "Casual"]),
        ("tracksuit", ["Streetwear", "Casual"]),
        ("techwear jumpsuit", ["Cyberpunk", "Streetwear"]),
        ("blazer dress", ["Office Lady", "Mature"]),
        ("sweater dress", ["Casual", "Lady"]),
        ("tea dress", ["Lady"]),
        ("wrap dress", ["Lady", "Mature"]),
        ("denim overalls", ["Casual"]),
        ("cocktail dress", ["Lady", "Mature"]),
        ("t-shirt dress", ["Casual", "Streetwear"]),
        ("pinafore dress", ["School Uniform", "Casual"]),
        ("princess dress", ["Fantasy", "Lady"]),
        ("catsuit", ["Cyberpunk", "Mature"]),
        ("kaftan", ["Casual", "Fantasy"]),
        ("salwar kameez", ["Traditional", "Casual"]),
        ("hanfu", ["Fantasy", "Traditional"]),
        ("dirndl", ["Traditional", "Lady"]),
        ("dungarees", ["Casual"]),
    ]
}

# ==========================================
# 2. ACCESSORIES (100 items)
# ==========================================

accessory_items = {
    "accessories": [ # General accessories
        ("wristwatch", ["Office Lady", "Mature", "Casual"]),
        ("smartwatch", ["Cyberpunk", "Sporty", "Casual"]),
        ("pearl necklace", ["Lady", "Mature"]),
        ("choker with bell", ["Maid", "Gothic Lolita", "Jirai Kei"]),
        ("stud earrings", ["Casual", "Office Lady"]),
        ("nose ring", ["Streetwear", "Cyberpunk"]),
        ("lip ring", ["Punk", "Cyberpunk"]),
        ("navel piercing", ["Casual", "Streetwear"]),
        ("friendship bracelet", ["Casual", "School Uniform"]),
        ("cufflinks", ["Mature", "Office Lady"]),
        ("brooch", ["Lady", "Mature", "Gothic Lolita"]),
        ("hair stick", ["Traditional", "Fantasy"]),
        ("barette", ["Lady", "School Uniform"]),
        ("hair claw", ["Casual", "Lady"]),
        ("headphones", ["Streetwear", "Cyberpunk", "Casual"]),
        ("ear muffs", ["Casual", "Lady"]),
        ("goggles", ["Cyberpunk", "Steampunk", "Streetwear"]),
        ("monocle", ["Mature", "Gothic Lolita"]),
        ("eyepatch", ["Gothic Lolita", "Cyberpunk"]),
        ("waist chain", ["Streetwear", "Lady"]),
        ("fan", ["Traditional", "Lady", "Gothic Lolita"]),
        ("umbrella", ["Lady", "Casual"]),
        ("walking cane", ["Mature", "Gothic Lolita"]),
        ("gloves", ["Lady", "Mature", "Gothic Lolita"]),
        ("fingerless gloves", ["Streetwear", "Cyberpunk"]),
        ("armband", ["Streetwear", "Cyberpunk"]),
        ("tail", ["Cosplay", "Fantasy"]),
        ("wings", ["Fantasy", "Cosplay"]),
        ("mask", ["Cyberpunk", "Traditional", "Streetwear"]),
        ("scarf", ["Casual", "Mature"]),
    ],
    "headwear": [
        ("baseball cap", ["Casual", "Streetwear"]),
        ("beanie", ["Casual", "Streetwear"]),
        ("fedora", ["Mature", "Streetwear"]),
        ("sun hat", ["Lady", "Casual"]),
        ("visor", ["Sporty", "Casual"]),
        ("beret", ["Lady", "School Uniform", "Artistic"]),
        ("turban", ["Casual", "Traditional"]),
        ("hijab", ["Traditional", "Modest"]),
        ("crown", ["Fantasy", "Lady"]),
        ("helmet", ["Cyberpunk", "Sporty"]),
        ("fascinator", ["Lady", "Mature"]),
        ("bonnet", ["Gothic Lolita", "Traditional"]),
        ("cowboy hat", ["Western", "Casual"]),
        ("snapback", ["Streetwear"]),
        ("hair ribbon", ["Lady", "School Uniform", "Jirai Kei"]),
        ("headband", ["Sporty", "Casual"]),
        ("witch hat", ["Fantasy", "Halloween"]),
        ("santa hat", ["Holiday", "Casual"]),
        ("nurse cap", ["Cosplay", "Uniform"]),
        ("police cap", ["Cosplay", "Uniform"]),
    ],
    "bags": [
        ("backpack", ["Casual", "School Uniform"]),
        ("briefcase", ["Office Lady", "Mature"]),
        ("clutch", ["Lady", "Mature"]),
        ("crossbody bag", ["Casual", "Streetwear"]),
        ("duffel bag", ["Sporty", "Casual"]),
        ("messenger bag", ["Casual", "School Uniform"]),
        ("shoulder bag", ["Lady", "Office Lady"]),
        ("waist bag", ["Streetwear", "Casual"]),
        ("suitcase", ["Travel", "Mature"]),
        ("lunch box", ["School Uniform", "Casual"]),
        ("ita bag", ["Jirai Kei", "Otaku"]),
        ("basket", ["Cottagecore", "Lady"]),
        ("drawstring bag", ["Casual", "Sporty"]),
        ("bucket bag", ["Lady", "Casual"]),
        ("camera bag", ["Casual", "Artistic"]),
        ("guitar case", ["Casual", "Musician"]),
        ("violin case", ["School Uniform", "Musician"]),
        ("shopping bag", ["Casual", "Lady"]),
        ("satchel", ["School Uniform", "Casual"]),
        ("coin purse", ["Casual", "Lady"]),
    ],
    "neckwear": [
        ("tie", ["Office Lady", "School Uniform"]),
        ("bolo tie", ["Western", "Casual"]),
        ("ascot", ["Mature", "Lady"]),
        ("pendant", ["Casual", "Lady"]),
        ("locket", ["Mature", "Gothic Lolita"]),
        ("beads", ["Casual", "Bohemian"]),
        ("collar", ["Gothic Lolita", "Punk"]),
        ("infinity scarf", ["Casual", "Mature"]),
        ("boa", ["Lady", "Mature"]),
        ("dog tag", ["Streetwear", "Military"]),
    ],
    "shoes": [
        ("loafers", ["School Uniform", "Office Lady"]),
        ("oxfords", ["Mature", "School Uniform"]),
        ("running shoes", ["Sporty", "Casual"]),
        ("sandals", ["Casual", "Lady"]),
        ("slippers", ["Casual", "Home"]),
        ("rain boots", ["Casual"]),
        ("snow boots", ["Casual", "Winter"]),
        ("stilettos", ["Mature", "Lady"]),
        ("mules", ["Lady", "Casual"]),
        ("clogs", ["Casual"]),
        ("gladiator sandals", ["Lady", "Bohemian"]),
        ("mary janes", ["School Uniform", "Gothic Lolita"]),
        ("thigh high boots", ["Mature", "Cyberpunk"]),
        ("hiking boots", ["Casual", "Sporty"]),
        ("espadrilles", ["Casual", "Lady"]),
    ],
    "legwear": [
        ("knee socks", ["School Uniform", "Casual"]),
        ("fishnets", ["Streetwear", "Cyberpunk", "Gothic Lolita"]),
        ("thigh highs", ["School Uniform", "Mature"]),
        ("leggings", ["Sporty", "Casual"]),
        ("tabi socks", ["Traditional", "Casual"]),
    ]
}

# ==========================================
# 3. SETS (100 new sets)
# ==========================================

# Format: (Style, Set Name, [Top, Bottom, Legwear, Shoes, Accessories])
# Or for Full Body: (Style, Set Name, [Full Body, "", Legwear, Shoes, Accessories])
# The Generator.add_outfit_set logic takes a list of items.
# _generate_outfit maps list items: 0:Top, 1:Bottom, 2:Legwear, 3:Shoes, 4:Accessories
# For full body, we might need a convention or just put it in index 0.
# Wait, looking at generator.py:
# if len(items) >= 1: outfit["top"] = items[0]
# if len(items) >= 2: outfit["bottom"] = items[1]
# So sets currently assume top/bottom split.
# If I want a full body set, I might need to put "None" or something?
# Let's check `_generate_outfit` again.
# items = chosen_set['items']
# if len(items) >= 1: outfit["top"] = items[0]
# It assigns items[0] to "top".
# This means existing sets are likely Top/Bottom based.
# If I want to support full body sets, I'd need to modify the generator or the set structure.
# For now, I will stick to Top/Bottom sets to match the existing logic's assumption, or use the "top" slot for full body descriptions if the model handles it gracefully (but the key will be "top").
# Actually, if I put "Red Dress" in "top", the prompt generator will output `(top: Red Dress)`. The prompt construction likely just concatenates them.
# So I'll stick to Top + Bottom combinations to be safe and consistent.

new_sets = [
    # CASUAL (15)
    ("Casual", "Weekend Comfort", ["Grey Hoodie", "Denim Shorts", "Ankle Socks", "Sneakers", "Cap"]),
    ("Casual", "Coffee Shop", ["Beige Cardigan", "Black Jeans", "None", "Loafers", "Tote Bag"]),
    ("Casual", "Summer Breeze", ["White Tank Top", "Floral Skirt", "None", "Sandals", "Sunglasses"]),
    ("Casual", "Library Study", ["Oversized Sweater", "Leggings", "Wool Socks", "Slippers", "Glasses"]),
    ("Casual", "Park Picnic", ["Gingham Top", "Denim Skirt", "None", "Canvas Shoes", "Straw Hat"]),
    ("Casual", "Rainy Day", ["Yellow Raincoat", "Jeans", "None", "Rain Boots", "Umbrella"]),
    ("Casual", "Movie Night", ["Graphic Tee", "Sweatpants", "None", "Slides", "Popcorn Bucket"]),
    ("Casual", "Road Trip", ["Flannel Shirt", "Cargo Shorts", "None", "Hiking Boots", "Backpack"]),
    ("Casual", "Gardening", ["Overalls", "Striped Tee", "None", "Clogs", "Sun Hat"]),
    ("Casual", "Art Class", ["Paint-splattered Smock", "Black Pants", "None", "Old Sneakers", "Beret"]),
    ("Casual", "Music Festival", ["Crochet Top", "Cutoff Shorts", "None", "Gladiator Sandals", "Flower Crown"]),
    ("Casual", "Yoga Session", ["Sports Bra", "Yoga Pants", "None", "Barefoot", "Yoga Mat"]),
    ("Casual", "Winter Walk", ["Puffer Jacket", "Thermals", "Thick Socks", "Snow Boots", "Scarf"]),
    ("Casual", "Skate Park", ["Baggy T-shirt", "Cargo Pants", "None", "Skate Shoes", "Beanie"]),
    ("Casual", "Beach Day", ["Bikini Top", "Sarong", "None", "Flip Flops", "Beach Bag"]),

    # STREETWEAR (15)
    ("Streetwear", "Urban Ninja", ["Techwear Hoodie", "Joggers with Straps", "None", "High-top Sneakers", "Mask"]),
    ("Streetwear", "Graffiti Artist", ["Oversized Hoodie", "Paint-stained Jeans", "None", "Chunky Sneakers", "Respirator"]),
    ("Streetwear", "Hypebeast", ["Logo Tee", "Designer Track Pants", "Branded Socks", "Limited Edition Kicks", "Fanny Pack"]),
    ("Streetwear", "Skater Boy", ["Thrasher Hoodie", "Dickies Pants", "White Socks", "Vans", "Snapback"]),
    ("Streetwear", "Neon Nights", ["Neon Crop Top", "Reflective Pants", "Net Tights", "Platform Boots", "Glow Sticks"]),
    ("Streetwear", "Utility Core", ["Tactical Vest", "Cargo Pants", "None", "Combat Boots", "Utility Belt"]),
    ("Streetwear", "Retro Sport", ["Vintage Windbreaker", "Track Shorts", "Tube Socks", "Retro Trainers", "Headband"]),
    ("Streetwear", "Grunge Revival", ["Distressed Flannel", "Ripped Jeans", "Fishnets", "Doc Martens", "Choker"]),
    ("Streetwear", "Monochrome", ["Black Turtleneck", "Black Wide Leg Pants", "Black Socks", "Black Boots", "Silver Chain"]),
    ("Streetwear", "Denim on Denim", ["Denim Jacket", "Jeans", "None", "White Sneakers", "Bandana"]),
    ("Streetwear", "Cyber Vibes", ["Holographic Jacket", "Vinyl Skirt", "None", "Platform Shoes", "Visor"]),
    ("Streetwear", "Military Chic", ["Camo Jacket", "Cargo Skirt", "None", "Boots", "Dog Tags"]),
    ("Streetwear", "Varsity", ["Letterman Jacket", "Pleated Skirt", "Knee Socks", "Loafers", "Backpack"]),
    ("Streetwear", "Oversized Fit", ["XXL T-shirt", "Biker Shorts", "None", "Dad Shoes", "Bucket Hat"]),
    ("Streetwear", "Layered Look", ["Hoodie under Jacket", "Sweatpants", "None", "Sneakers", "Beanie"]),

    # LADY (10)
    ("Lady", "Garden Party", ["Floral Blouse", "White Midi Skirt", "Sheer Tights", "Heels", "Wide Brim Hat"]),
    ("Lady", "Tea Time", ["Lace Top", "Pastel Skirt", "White Tights", "Mary Janes", "Gloves"]),
    ("Lady", "Evening Date", ["Silk Camisole", "Satin Skirt", "None", "Stilettos", "Clutch"]),
    ("Lady", "Office Chic", ["Blazer", "Pencil Skirt", "Black Tights", "Pumps", "Tote"]),
    ("Lady", "Sunday Brunch", ["Wrap Top", "Culottes", "None", "Mules", "Sunglasses"]),
    ("Lady", "Gallery Opening", ["Structured Top", "Pleated Trousers", "None", "Pointed Flats", "Statement Earrings"]),
    ("Lady", "Winter Elegance", ["Wool Coat", "Knit Dress", "Warm Tights", "Knee High Boots", "Beret"]),
    ("Lady", "Summer Romance", ["Off-shoulder Top", "Maxi Skirt", "None", "Wedges", "Straw Bag"]),
    ("Lady", "Classic French", ["Striped Shirt", "Capri Pants", "None", "Ballet Flats", "Red Scarf"]),
    ("Lady", "Vintage Glamour", ["Polka Dot Blouse", "Circle Skirt", "Seamed Stockings", "Peep Toe Heels", "Pearl Necklace"]),

    # MATURE (10)
    ("Mature", "Executive", ["Silk Blouse", "Tailored Trousers", "None", "Heels", "Briefcase"]),
    ("Mature", "Cocktail Hour", ["Velvet Top", "Slit Skirt", "Sheer Hose", "Strappy Heels", "Gold Jewelry"]),
    ("Mature", "Country Club", ["Polo Shirt", "Beige Slacks", "None", "Loafers", "Sweater draped over shoulders"]),
    ("Mature", "Wine Tasting", ["Cashmere Sweater", "Dark Jeans", "None", "Ankle Boots", "Leather Bag"]),
    ("Mature", "Night Out", ["Leather Jacket", "Skinny Jeans", "None", "Boots", "Hoop Earrings"]),
    ("Mature", "Resort Wear", ["Tunic Top", "Linen Pants", "None", "Sandals", "Sun Hat"]),
    ("Mature", "Winter Coat", ["Fur Coat", "Leggings", "None", "Tall Boots", "Leather Gloves"]),
    ("Mature", "Formal Dinner", ["Satin Blouse", "Velvet Skirt", "Black Tights", "Pumps", "Diamond Earrings"]),
    ("Mature", "Casual Friday", ["Blazer", "Jeans", "None", "Flats", "Smartwatch"]),
    ("Mature", "Opera Night", ["Lace Bodysuit", "Taffeta Skirt", "None", "Evening Shoes", "Opera Glasses"]),

    # JIRAI KEI (10)
    ("Jirai Kei", "Pink Addiction", ["Pink Ruffle Blouse", "Pink Skirt", "White Knee Socks", "Platform Shoes", "My Melody Plush"]),
    ("Jirai Kei", "Dark Angel", ["Black Lace Top", "Black Frill Skirt", "Fishnet Socks", "Buckle Shoes", "Wings"]),
    ("Jirai Kei", "Hospital Chic", ["Oversized Shirt", "Shorts", "Bandaged Leg", "Slippers", "Eye Patch"]),
    ("Jirai Kei", "Bunny Girl", ["Hoodie with Ears", "Frilly Bloomers", "Patterned Tights", "Sneakers", "Bunny Backpack"]),
    ("Jirai Kei", "Heartbreak", ["T-shirt with Slogan", "Pleated Skirt", "Loose Socks", "Loafers", "Fake Tears"]),
    ("Jirai Kei", "Idol Wannabe", ["Checkered Top", "Suspender Skirt", "Lace Socks", "Heels", "Microphone"]),
    ("Jirai Kei", "Teddy Bear", ["Fuzzy Sweater", "Brown Skirt", "Bear Tights", "Boots", "Bear Ears"]),
    ("Jirai Kei", "Twin Tails", ["Sailor Top", "Ribbon Skirt", "Knee Highs", "Mary Janes", "Hair Ribbons"]),
    ("Jirai Kei", "Gothic Touch", ["Cross Print Top", "Tulle Skirt", "Garter Socks", "Platform Boots", "Choker"]),
    ("Jirai Kei", "Sweet Devil", ["Red & Black Blouse", "Leather Skirt", "Striped Socks", "Demon Horns", "Pitchfork"]),

    # GOTHIC LOLITA (10)
    ("Gothic Lolita", "Vampire Tea", ["Velvet Bodice", "Bat Print Skirt", "Lace Tights", "Bat Wing Shoes", "Parasol"]),
    ("Gothic Lolita", "Doll House", ["High Collar Blouse", "Pinafore Dress", "Doll Joints Tights", "Doll Shoes", "Bonnet"]),
    ("Gothic Lolita", "Cemetery Walk", ["Black Capelet", "Long Ruffle Skirt", "None", "Witch Boots", "Lantern"]),
    ("Gothic Lolita", "Midnight Mass", ["Nun-style Top", "Cross Embroidery Skirt", "Plain Tights", "Modest Shoes", "Rosary"]),
    ("Gothic Lolita", "Clockwork", ["Steampunk Blouse", "Corset Skirt", "Striped Tights", "Gear Boots", "Goggles"]),
    ("Gothic Lolita", "Blue Rose", ["Navy Blouse", "Blue Rose Skirt", "White Tights", "Navy Shoes", "Blue Rose Headdress"]),
    ("Gothic Lolita", "White Mourning", ["White Lace Top", "White Tiered Skirt", "White Lace Tights", "White Shoes", "Veil"]),
    ("Gothic Lolita", "Aristocrat", ["Tailcoat", "Breeches", "Long Socks", "Riding Boots", "Top Hat"]),
    ("Gothic Lolita", "Broken Doll", ["Tattered Blouse", "Patchwork Skirt", "Mismatched Socks", "Old Shoes", "Bandages"]),
    ("Gothic Lolita", "Cathedral", ["Stained Glass Print Top", "High Waist Skirt", "Sheer Tights", "Platform Heels", "Halo"]),

    # CYBERPUNK (10)
    ("Cyberpunk", "Netrunner", ["Neural Link Suit Top", "Data Pants", "Neon Socks", "Hover Boots", "VR Visor"]),
    ("Cyberpunk", "Street Samurai", ["Kimono Jacket", "Hakama Pants", "Tabi Boots", "Cyber Katana", "Oni Mask"]),
    ("Cyberpunk", "Corporate Spy", ["Structured Blazer", "Pencil Skirt with LED", "Smart Tights", "Chrome Heels", "Data Chip"]),
    ("Cyberpunk", "Mechanic", ["Grease-stained Tank", "Utility Overalls", "None", "Mag-lock Boots", "Wrench"]),
    ("Cyberpunk", "Hacker", ["Hoodie with glowing text", "Baggy Shorts", "Leg Warmers", "Sneakers", "Laptop Bag"]),
    ("Cyberpunk", "Android Idol", ["Plastic Chest Piece", "Clear Plastic Skirt", "Circuitry Tights", "Glass Heels", "Antenna"]),
    ("Cyberpunk", "Bounty Hunter", ["Armored Vest", "Leather Pants", "Knee Pads", "Combat Boots", "Blaster"]),
    ("Cyberpunk", "Neon Racer", ["Racing Jacket", "Biker Shorts", "None", "Speed Shoes", "Helmet"]),
    ("Cyberpunk", "Bio-Hacker", ["Lab Coat", "Latex Dress", "None", "Rubber Boots", "Syringe"]),
    ("Cyberpunk", "Wasteland Survivor", ["Rags Layered Top", "Cargo Pants", "Wrapped Legs", "Dusty Boots", "Gas Mask"]),

    # SCHOOL UNIFORM (10)
    ("School Uniform", "Honor Student", ["White Shirt", "Plaid Skirt", "Navy Knee Socks", "Loafers", "Glasses"]),
    ("School Uniform", "Delinquent", ["Long Skirt", "Cropped Shirt", "None", "Sneakers", "Bat"]),
    ("School Uniform", "Winter Uniform", ["Blazer", "Wool Skirt", "Black Tights", "Boots", "Scarf"]),
    ("School Uniform", "Summer Uniform", ["Short Sleeve Shirt", "Light Skirt", "Short Socks", "Shoes", "Sun Hat"]),
    ("School Uniform", "Gym Class", ["PE Shirt", "Gym Shorts", "White Socks", "Trainers", "Whistle"]),
    ("School Uniform", "Cheerleader", ["Cheer Top", "Mini Skirt", "Team Socks", "Cheer Shoes", "Pom Poms"]),
    ("School Uniform", "Kendo Club", ["Kendo Gi", "Hakama", "None", "Barefoot", "Bamboo Sword"]),
    ("School Uniform", "Science Club", ["Lab Coat", "Uniform Skirt", "Socks", "Shoes", "Goggles"]),
    ("School Uniform", "After School", ["Loose Cardigan", "Rolled Skirt", "Loose Socks", "Loafers", "School Bag"]),
    ("School Uniform", "Graduation", ["Uniform with Flower", "Skirt", "Socks", "Shoes", "Diploma"]),

    # MAID (10)
    ("Maid", "Classic French", ["Black Dress Top", "White Apron", "Black Tights", "Heels", "Headband"]),
    ("Maid", "Cafe Style", ["Pastel Blouse", "Short Apron Skirt", "Knee Highs", "Mary Janes", "Tray"]),
    ("Maid", "Battle Maid", ["Armored Apron", "Combat Skirt", "Steel Greaves", "Boots", "Halberd"]),
    ("Maid", "Cat Maid", ["Paw Gloves", "Tail Skirt", "Paw Socks", "Paw Shoes", "Cat Ears"]),
    ("Maid", "Victorian Maid", ["Long Sleeve Dress", "Long Apron", "None", "Button Boots", "Mob Cap"]),
    ("Maid", "Cyber Maid", ["Latex Maid Top", "Neon Apron", "Circuit Tights", "Platform Boots", "Visor"]),
    ("Maid", "Zombie Maid", ["Torn Dress", "Bloodied Apron", "Ripped Tights", "One Shoe", "Cleaver"]),
    ("Maid", "Witch Maid", ["Maid Top", "Starry Apron", "Striped Tights", "Pointy Shoes", "Witch Hat"]),
    ("Maid", "Nurse Maid", ["Nurse Cap", "White Apron", "White Tights", "White Shoes", "Syringe"]),
    ("Maid", "Bunny Maid", ["Bunny Suit Top", "Apron", "Fishnets", "Heels", "Bunny Ears"]),
]


def main():
    print("Adding massive amount of outfit items...")
    added_clothing = 0
    added_accessories = 0
    added_sets = 0

    # 1. Add Clothing
    print("\n== Adding Clothing ==")
    for category, items in clothing_items.items():
        for name, styles in items:
            # Note: add_outfit_item checks for duplicates
            if gen.add_outfit_item(category, name, styles):
                # print(f"  + [{category}] {name}")
                added_clothing += 1

    # 2. Add Accessories
    print("\n== Adding Accessories ==")
    for category, items in accessory_items.items():
        for name, styles in items:
            if gen.add_outfit_item(category, name, styles):
                # print(f"  + [{category}] {name}")
                added_accessories += 1

    # 3. Add Sets
    print("\n== Adding Sets ==")
    for style, name, items in new_sets:
        # items in add_outfit_set is a list of strings
        if gen.add_outfit_set(style, name, items):
            # print(f"  + [Set] {name} ({style})")
            added_sets += 1

    print(f"\nSummary:")
    print(f"  Added Clothing Items: {added_clothing}")
    print(f"  Added Accessory Items: {added_accessories}")
    print(f"  Added Sets: {added_sets}")
    print(f"  Total: {added_clothing + added_accessories + added_sets}")

if __name__ == "__main__":
    main()
