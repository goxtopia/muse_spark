"""
Script to add seasonal environment descriptions.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompt_gen.generator import PromptGenerator

gen = PromptGenerator()

# ========== Spring Locations ==========
spring_locations = [
    "cherry blossom park",
    "flower garden in bloom",
    "meadow with wildflowers",
    "riverside with sakura trees",
    "rain-washed street with petals",
    "botanical garden greenhouse",
    "tulip field in Holland",
    "wisteria tunnel",
    "lavender field at dawn",
    "vineyard with new growth",
    "countryside with blooming canola flowers",
    "temple garden with plum blossoms",
    "school entrance ceremony under cherry trees",
    "picnic blanket under flowering tree",
    "umbrella in spring rain with petals falling",
    "cafe terrace surrounded by flowers",
    "wedding venue with spring flowers",
]

# ========== Summer Locations ==========
summer_locations = [
    "beach with crystal blue water",
    "poolside with palm trees",
    "summer festival with lanterns",
    "fireworks display by the river",
    "watermelon on wooden porch",
    "shaved ice stand at matsuri",
    "cicada-filled forest path",
    "sunflower field at noon",
    "ocean pier at sunset",
    "tropical island paradise",
    "outdoor BBQ party",
    "rooftop pool overlooking city",
    "beach bonfire at night",
    "yacht deck on calm sea",
    "waterfall swimming hole",
    "hammock between palm trees",
    "ice cream shop on hot day",
    "air-conditioned convenience store escape",
    "school pool during summer break",
    "countryside river for swimming",
    "cicada shell on tree bark",
    "wind chimes on summer breeze",
    "yukata at summer festival",
    "catching fireflies at dusk",
    "stargazing on summer night",
]

# ========== Autumn Locations ==========  
autumn_locations = [
    "maple forest in full color",
    "fallen leaves covering path",
    "harvest moon viewing spot",
    "pumpkin patch",
    "apple orchard",
    "vineyard during grape harvest",
    "campus with golden ginkgo trees",
    "cafe with autumn window view",
    "train through autumn mountains",
    "hot spring with autumn foliage",
    "shrine with red maple leaves",
    "park bench covered in leaves",
    "corn maze at dusk",
    "cemetery with fall colors",
    "abandoned house with dead garden",
    "rainy street with umbrella and leaves",
    "bookstore on autumn afternoon",
    "kotatsu room with autumn view",
    "temple steps with fallen leaves",
    "hiking trail in autumn forest",
    "farmers market in fall",
    "halloween decorated street",
    "bonfire with friends",
]

# ========== Winter Locations ==========
winter_locations = [
    "snow-covered shrine",
    "frozen lake under grey sky",
    "christmas market with lights",
    "ski resort lodge",
    "hot spring in snow",
    "illumination display",
    "kotatsu with mikan oranges",
    "snowy mountain cabin",
    "ice skating rink",
    "snow-covered city street",
    "warm cafe on cold day",
    "frost on window pane",
    "breath visible in cold air",
    "snowman in quiet garden",
    "icicles hanging from roof",
    "empty playground in snow",
    "train station in snowfall",
    "convenience store warmth at night",
    "new years shrine visit",
    "watching snow fall from window",
    "footprints in fresh snow",
    "bare tree branches against grey sky",
    "frozen pond with dead reeds",
    "deserted beach in winter",
    "lighthouse in winter storm",
]

# ========== Seasonal Weather ==========
weather = [
    # Spring
    "cherry blossom petals dancing in wind",
    "gentle spring rain",
    "warm breeze carrying flower scent",
    "morning dew on petals",
    "soft golden spring sunlight",
    "rainbow after spring shower",
    
    # Summer
    "blazing summer sun",
    "humid tropical heat",
    "afternoon thunderstorm",
    "heat shimmer rising from asphalt",
    "sea breeze cooling hot day",
    "sudden summer downpour",
    "clear starry summer night",
    "cicadas singing in heat",
    
    # Autumn
    "crisp autumn air",
    "golden afternoon light",
    "leaves rustling in wind",
    "morning frost on grass",
    "autumn rain on window",
    "mist rising at dawn",
    "cold wind carrying leaves",
    
    # Winter
    "heavy snowfall",
    "freezing wind",
    "grey overcast sky",
    "diamond dust in air",
    "breath visible in cold",
    "sun dogs in winter sky",
    "ice crystals on everything",
    "warm sunlight through cold air",
]

# ========== Seasonal Time ==========
seasons = [
    # Spring
    "first day of spring",
    "cherry blossom season peak",
    "rainy season beginning",
    "graduation day",
    "new school year",
    
    # Summer  
    "peak of summer heat",
    "obon holiday",
    "summer vacation",
    "last day of summer",
    "meteor shower night",
    "midsummer night",
    
    # Autumn
    "peak autumn colors",
    "harvest festival",
    "sports day",
    "culture festival",
    "thanksgiving",
    "halloween night",
    
    # Winter
    "first snowfall",
    "christmas eve",
    "new years eve",
    "coldest day of year",
    "end of winter exams",
    "valentines day",
]

def main():
    print("Adding seasonal environment data...")
    
    added_count = 0
    
    all_locations = spring_locations + summer_locations + autumn_locations + winter_locations
    for loc in all_locations:
        if gen.add_environment_item('locations', loc):
            print(f"  + Added: {loc}")
            added_count += 1
    
    for w in weather:
        if gen.add_environment_item('weather', w):
            print(f"  + Added: {w}")
            added_count += 1
    
    for s in seasons:
        if gen.add_environment_item('seasons', s):
            print(f"  + Added: {s}")
            added_count += 1
    
    print(f"\nDone! Added {added_count} seasonal items.")

if __name__ == "__main__":
    main()
