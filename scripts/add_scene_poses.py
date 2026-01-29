"""
Script to add scene-bound poses.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompt_gen.generator import PromptGenerator
import json

gen = PromptGenerator()

# Scene-bound poses: keywords -> list of poses
# Keywords are comma-separated and matched against location
scene_poses = {
    # School/Learning environments
    "school, classroom, university, lecture, campus": [
        "sitting at desk studying",
        "reading textbook",
        "writing notes",
        "raising hand",
        "looking at blackboard",
        "sleeping at desk",
        "chatting with classmate",
        "walking in hallway",
        "at locker",
        "eating lunch at desk",
        "packing bag",
        "looking out classroom window",
    ],
    
    # Library/Reading
    "library, bookstore, reading": [
        "reading book",
        "browsing bookshelves",
        "reaching for book on high shelf",
        "sitting and reading",
        "studying at table",
        "flipping through pages",
        "carrying stack of books",
        "quiet contemplation",
    ],
    
    # Cafe/Restaurant
    "cafe, coffee, restaurant, izakaya, bar, kitchen": [
        "sipping drink",
        "holding cup",
        "eating",
        "looking at menu",
        "waiting for order",
        "chatting over table",
        "stirring drink",
        "taking photo of food",
        "wiping table",
    ],
    
    # Shopping
    "shop, store, mall, market": [
        "browsing merchandise",
        "trying on clothes",
        "looking at display",
        "holding shopping bags",
        "checking phone",
        "window shopping",
        "waiting in line",
        "examining product",
    ],
    
    # Street/Urban
    "street, alley, crossing, sidewalk, city": [
        "walking on street",
        "waiting to cross",
        "checking phone while walking",
        "looking at storefront",
        "hailing taxi",
        "waiting at crosswalk",
        "looking at map",
        "taking photo",
    ],
    
    # Train/Station
    "station, train, subway, bus, platform": [
        "waiting for train",
        "sitting on platform bench",
        "reading on train",
        "sleeping on train",
        "holding handrail",
        "looking out train window",
        "checking arrival time",
        "rushing to catch train",
        "standing in crowded train",
    ],
    
    # Beach/Pool/Water
    "beach, pool, sea, ocean, water, swim": [
        "splashing in water",
        "lying on beach towel",
        "building sandcastle",
        "walking along shore",
        "swimming",
        "diving",
        "floating",
        "sunbathing",
        "playing beach volleyball",
        "collecting shells",
    ],
    
    # Park/Nature
    "park, garden, forest, mountain, nature, hike": [
        "sitting on park bench",
        "walking in nature",
        "picking flowers",
        "photographing scenery",
        "having picnic",
        "bird watching",
        "stretching outdoors",
        "jogging",
        "feeding birds",
        "cloud watching",
    ],
    
    # Shrine/Temple/Religious
    "shrine, temple, church, torii": [
        "praying",
        "making offering",
        "ringing bell",
        "drawing fortune",
        "washing hands at fountain",
        "walking through torii",
        "bowing respectfully",
        "looking at architecture",
    ],
    
    # Stage/Performance
    "stage, concert, theater, performance": [
        "performing on stage",
        "singing",
        "dancing",
        "playing instrument",
        "bowing to audience",
        "idol pose",
        "microphone holding",
        "dramatic pose",
    ],
    
    # Bed/Bedroom
    "bed, bedroom, futon": [
        "lying in bed",
        "just waking up",
        "stretching in bed",
        "sitting on bed",
        "hugging pillow",
        "reading in bed",
        "using phone in bed",
        "sleepy expression",
        "under blankets",
    ],
    
    # Bathroom/Mirror
    "bathroom, mirror, bath": [
        "looking in mirror",
        "fixing hair in mirror",
        "applying makeup",
        "brushing teeth",
        "bathing",
        "towel wrapped",
        "self-reflection",
    ],
    
    # Kitchen/Cooking
    "kitchen, cooking": [
        "cooking",
        "chopping vegetables",
        "stirring pot",
        "tasting food",
        "wearing apron",
        "washing dishes",
        "following recipe",
    ],
    
    # Office/Work
    "office, desk, work, meeting": [
        "typing on computer",
        "on phone call",
        "looking at documents",
        "presenting",
        "meeting pose",
        "coffee break",
        "stretching at desk",
        "overtime exhausted",
    ],
    
    # Gym/Exercise
    "gym, exercise, sport, track": [
        "working out",
        "stretching",
        "running on treadmill",
        "lifting weights",
        "yoga pose",
        "drinking water",
        "wiping sweat",
        "resting between sets",
    ],
    
    # Hospital/Medical
    "hospital, clinic, medical": [
        "sitting in waiting room",
        "lying in hospital bed",
        "iv drip attached",
        "wearing patient gown",
        "looking out hospital window",
        "receiving treatment",
    ],
    
    # Rooftop
    "rooftop, roof": [
        "looking at city view",
        "sitting on edge",
        "wind blowing hair",
        "leaning on railing",
        "eating lunch on rooftop",
        "stargazing",
        "contemplative pose",
    ],
    
    # Festival/Event
    "festival, matsuri, carnival, event": [
        "holding festival food",
        "watching fireworks",
        "playing carnival game",
        "wearing yukata",
        "dancing at festival",
        "excited expression",
        "taking festival photos",
    ],
    
    # Arcade/Gaming
    "arcade, game, gaming": [
        "playing arcade game",
        "intense gaming focus",
        "victory celebration",
        "frustration from losing",
        "claw machine attempt",
        "taking purikura photos",
    ],
    
    # Cemetery/Dark Places
    "cemetery, graveyard, morgue, abandoned": [
        "somber mourning",
        "placing flowers",
        "praying for dead",
        "exploring cautiously",
        "frightened pose",
        "looking around nervously",
        "running away scared",
    ],
}

def main():
    print("Adding scene-bound poses...")
    
    # Load current poses data
    poses_path = os.path.join(gen.data_dir, 'poses.json')
    
    with open(poses_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Add scene_poses if not exists
    if 'scene_poses' not in data:
        data['scene_poses'] = {}
    
    added_count = 0
    for scene, poses in scene_poses.items():
        if scene not in data['scene_poses']:
            data['scene_poses'][scene] = []
        
        for pose in poses:
            if pose not in data['scene_poses'][scene]:
                data['scene_poses'][scene].append(pose)
                print(f"  + [{scene[:20]}...] {pose}")
                added_count += 1
    
    # Save back
    with open(poses_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\nDone! Added {added_count} scene-bound poses.")

if __name__ == "__main__":
    main()
