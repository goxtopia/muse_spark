"""
Script to add more environment descriptions to the data.
Run this script to populate the environment data with interesting descriptions.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompt_gen.generator import PromptGenerator

gen = PromptGenerator()

# ========== Locations ==========
locations = [
    # Indoor - Short
    "cozy apartment",
    "dark basement",
    "attic room",
    "bathroom mirror",
    "hotel lobby",
    "subway station",
    "elevator",
    "shopping mall",
    "convenience store",
    "laundromat",
    "arcade",
    "karaoke room",
    "hospital corridor",
    "school hallway",
    "university lecture hall",
    "art gallery",
    "museum",
    "theater stage",
    "backstage dressing room",
    "recording studio",
    "photography studio",
    
    # Indoor - Detailed
    "dimly lit izakaya with paper lanterns",
    "abandoned hospital with peeling paint",
    "old Japanese mansion with tatami floors",
    "cluttered otaku room with anime posters",
    "minimalist white room with single window",
    "underground nightclub with neon lights",
    "vintage record shop filled with vinyl",
    "dusty antique bookstore",
    "steamy public bathhouse",
    "cramped capsule hotel pod",
    "luxury penthouse with city view",
    "abandoned warehouse with graffiti walls",
    "traditional tea ceremony room",
    "retro kissaten coffee shop",
    "internet cafe with blue screen glow",
    
    # Outdoor - Short
    "shrine entrance",
    "temple grounds",
    "cemetery",
    "riverbank",
    "bridge at sunset",
    "train tracks",
    "bus stop",
    "parking lot",
    "alleyway",
    "shopping district",
    "night market",
    "amusement park",
    "ferris wheel",
    "playground",
    "school courtyard",
    "university campus",
    "construction site",
    "industrial zone",
    "harbor",
    "pier",
    "lighthouse",
    "cliff edge",
    "countryside road",
    "rice paddy field",
    "bamboo grove",
    "cherry blossom tunnel",
    
    # Outdoor - Detailed
    "rain-soaked Tokyo street at night",
    "neon-lit Kabukicho alley",
    "quiet residential street at dusk",
    "crowded Shibuya crossing",
    "empty Shinjuku station platform at 3am",
    "cherry blossom lined river path",
    "misty mountain shrine at dawn",
    "seaside promenade at golden hour",
    "abandoned amusement park overgrown with vines",
    "graffiti-covered underpass",
    "rooftop overlooking city skyline",
    "fire escape with hanging laundry",
    "narrow street with vending machines",
    "old wooden bridge over koi pond",
    "moonlit bamboo forest",
    "snow-covered torii gate path",
    "autumn leaves falling in temple garden",
    "foggy lakeside dock",
    "sunset beach with tetrapods",
    "starlit countryside with fireflies",
    
    # Fantasy/Surreal
    "floating islands in pink sky",
    "crystal cave with bioluminescent fungi",
    "underwater ruins with ancient columns",
    "dreamscape with melting clocks",
    "mirror dimension with inverted gravity",
    "void space with scattered memories",
    "digital glitch realm",
    "eternal twilight forest",
    "celestial library with endless stairs",
    "garden of glass flowers",
]

# ========== Weather ==========
weather = [
    # Simple
    "misty",
    "humid",
    "drizzling",
    "thunderstorm",
    "hazy",
    "clear sky",
    "aurora borealis",
    "meteor shower",
    "eclipse",
    
    # Detailed
    "light rain with sun breaking through",
    "heavy downpour with lightning flashes",
    "thick fog rolling in",
    "gentle snow falling",
    "blizzard with howling wind",
    "golden sunlight through clouds",
    "dramatic storm clouds gathering",
    "rainbow after rain",
    "cherry blossom petals in wind",
    "autumn leaves swirling",
]

# ========== Seasons/Time ==========
seasons = [
    # Time of day
    "dawn",
    "early morning",
    "midday",
    "afternoon",
    "dusk",
    "twilight", 
    "night",
    "midnight",
    "witching hour",
    "blue hour",
    "golden hour",
    
    # Detailed time
    "3am quiet city",
    "last train of the night",
    "first light of dawn",
    "lazy Sunday afternoon",
    "Friday night energy",
    "monday morning gloom",
]

def main():
    print("Adding environment data...")
    
    added_count = 0
    
    # Add locations
    for loc in locations:
        if gen.add_environment_item('locations', loc):
            print(f"  + Added location: {loc}")
            added_count += 1
    
    # Add weather
    for w in weather:
        if gen.add_environment_item('weather', w):
            print(f"  + Added weather: {w}")
            added_count += 1
    
    # Add seasons/time
    for s in seasons:
        if gen.add_environment_item('seasons', s):
            print(f"  + Added season/time: {s}")
            added_count += 1
    
    print(f"\nDone! Added {added_count} new items.")
    print("Data has been saved to environment.json")

if __name__ == "__main__":
    main()
