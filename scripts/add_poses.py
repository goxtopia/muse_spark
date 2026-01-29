"""
Script to add more universal poses (scene-independent).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompt_gen.generator import PromptGenerator

gen = PromptGenerator()

# Universal poses that work anywhere
poses = [
    # Standing poses
    "standing with arms crossed",
    "standing with hands on hips",
    "standing with one hand on hip",
    "standing with hands behind back",
    "standing with hands in pockets",
    "standing straight looking forward",
    "standing with weight on one leg",
    "standing leaning to one side",
    "casual standing pose",
    "confident standing pose",
    "relaxed standing pose",
    "standing with tilted head",
    "standing looking over shoulder",
    "standing back to viewer",
    "three-quarter standing pose",
    "profile standing pose",
    
    # Sitting poses
    "sitting cross-legged",
    "sitting with legs stretched",
    "sitting hugging knees",
    "sitting with legs to one side",
    "sitting with one leg up",
    "sitting elegantly",
    "sitting casually",
    "sitting leaning forward",
    "sitting leaning back",
    "sitting with chin resting on hand",
    "sitting looking down",
    "sitting looking up",
    
    # Hand/Arm poses
    "hands clasped together",
    "one hand raised",
    "both hands raised",
    "hand near face",
    "hand touching chin",
    "hand touching cheek",
    "hand covering mouth",
    "hand on chest",
    "hand reaching out",
    "hands framing face",
    "finger on lips",
    "peace sign",
    "waving hand",
    "pointing pose",
    "hands making heart shape",
    "adjusting hair",
    "tucking hair behind ear",
    "playing with hair",
    "hand in hair",
    
    # Head/Face poses
    "head tilted to side",
    "looking up",
    "looking down",
    "looking to the side",
    "looking back at viewer",
    "eyes closed",
    "eyes half-closed",
    "winking",
    "smiling softly",
    "serious expression",
    "thoughtful expression",
    "surprised expression",
    "shy expression",
    "confident smile",
    "subtle smirk",
    "neutral expression",
    "melancholic expression",
    "dreamy expression",
    
    # Dynamic poses
    "walking pose",
    "mid-stride",
    "running pose",
    "jumping pose",
    "twirling",
    "spinning",
    "dancing pose",
    "stretching",
    "reaching upward",
    "leaning against invisible wall",
    "catching something",
    "throwing pose",
    
    # Crouching/Kneeling
    "crouching",
    "kneeling",
    "kneeling on one knee",
    "sitting on heels",
    "squatting",
    
    # Lying poses
    "lying on back",
    "lying on side",
    "lying on stomach",
    "lying with head propped on hand",
    "curled up",
    
    # Gesture/Expression poses
    "arms open wide",
    "shrugging",
    "beckoning gesture",
    "defensive pose",
    "contemplative pose",
    "praying pose",
    "meditating pose",
    "reading pose",
    "writing pose",
    "phone holding pose",
    "drinking pose",
    "eating pose",
    
    # Modeling/Fashion poses
    "model pose",
    "fashion pose",
    "elegant pose",
    "cute pose",
    "cool pose",
    "sexy pose",
    "playful pose",
    "mysterious pose",
    "dramatic pose",
    "candid pose",
    "natural pose",
    "relaxed pose",
    
    # Character poses
    "idol pose",
    "magical girl pose",
    "fighting stance",
    "victory pose",
    "thinking pose",
    "shy hiding face",
    "embarrassed pose",
    "proud pose",
    "tired pose",
    "yawning",
    "stretching arms",
]

def main():
    print("Adding universal poses...")
    added_count = 0
    
    for pose in poses:
        if gen.add_to_list('poses', 'poses', pose):
            print(f"  + Added: {pose}")
            added_count += 1
    
    print(f"\nDone! Added {added_count} new poses.")

if __name__ == "__main__":
    main()
