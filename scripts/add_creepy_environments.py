"""
Script to add creepy/eerie environment descriptions.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompt_gen.generator import PromptGenerator

gen = PromptGenerator()

# ========== Creepy/Eerie Locations ==========
locations = [
    # Short
    "morgue",
    "crematorium", 
    "mass grave",
    "execution ground",
    "torture chamber",
    "asylum cell",
    "padded room",
    "isolation ward",
    "quarantine zone",
    "autopsy room",
    "embalming room",
    "crypt",
    "catacomb",
    "ossuary",
    "mausoleum",
    "columbarium",
    "gallows",
    "dungeon",
    "oubliette",
    "plague pit",
    "cursed well",
    "haunted mirror",
    "séance room",
    "occult altar",
    "sacrificial chamber",
    "bone throne room",
    "flesh garden",
    
    # Detailed Indoor
    "abandoned mental asylum with scratched walls",
    "hospital morgue with flickering lights",
    "decaying Victorian mansion at midnight",
    "basement filled with old dolls",
    "room with walls covered in handprints",
    "empty operating theater with rusty tools",
    "children's ward with scattered toys",
    "psychiatric observation room behind one-way glass",
    "meat locker with hanging hooks",
    "taxidermy workshop with glass eyes watching",
    "antique shop filled with cursed objects",
    "abandoned orphanage nursery",
    "cult ritual room with blood stains",
    "forgotten bomb shelter with scratched door",
    "elevator stuck between floors in darkness",
    "hotel room 217 with peeling wallpaper",
    "attic with covered mirrors and whispers",
    "cellar with bricked-up doorway",
    "bathroom with bloody handprints on tiles",
    "kitchen with meat hooks and drain in floor",
    
    # Detailed Outdoor
    "foggy cemetery at midnight",
    "abandoned carnival with rusted rides",
    "dead forest with twisted black trees",
    "swamp with floating corpse lights",
    "battlefield littered with bones",
    "suicide forest with no birds singing",
    "crossroads at witching hour",
    "graveyard during solar eclipse",
    "ghost town main street at dusk",
    "abandoned mining town in thick fog",
    "plague village with boarded windows",
    "burning field under blood red sky",
    "dried lake bed with dead fish",
    "nuclear wasteland with shadows burned on walls",
    "island of abandoned dolls",
    "road that leads nowhere in darkness",
    "bridge where people jump",
    "train tracks where children died",
    "well that whispers names",
    "scarecrow field at harvest moon",
    
    # Supernatural/Liminal
    "endless hotel corridor",
    "staircase that never ends",
    "room with too many doors",
    "hallway that gets narrower",
    "space between walls",
    "reflection that moves wrong",
    "photograph you are trapped in",
    "memory of a room that never existed",
    "dream that knows you are watching",
    "static between TV channels",
    "0AM - the hour that does not exist",
    "backroom of a store that has no back",
    "poolroom with no way out",
    "parking garage level -2",
    "subway station not on any map",
]

# ========== Creepy Weather/Atmosphere ==========
weather = [
    "blood moon rising",
    "unnatural stillness",
    "sky wrong color",
    "air thick with whispers",
    "shadows moving wrong",
    "lights flickering",
    "temperature suddenly dropping",
    "smell of decay",
    "static electricity before something happens",
    "fog that follows you",
    "rain that falls upward",
    "snow that is warm",
    "wind that sounds like screaming",
    "silence so complete it hurts",
    "darkness that light cannot pierce",
]

# ========== Creepy Time ==========
seasons = [
    "3:33 AM",
    "hour before dawn",
    "moment before death",
    "time stopped",
    "wrong season",
    "day that repeats",
    "night that never ends",
    "moment you realize you are not alone",
    "instant before the scream",
    "after everyone left",
    "when the music box stops",
    "between heartbeats",
]

def main():
    print("Adding creepy environment data...")
    
    added_count = 0
    
    for loc in locations:
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
    
    print(f"\nDone! Added {added_count} creepy items.")

if __name__ == "__main__":
    main()
