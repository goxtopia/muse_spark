from prompt_gen.generator import PromptGenerator
import json

def test():
    gen = PromptGenerator()
    
    print("--- Test 1: Basic Generation ---")
    res1 = gen.generate()
    print(json.dumps(res1, indent=2))
    assert 'gender' in res1
    
    print("\n--- Test 2: Fixed Style (Jirai Kei) ---")
    res2 = gen.generate({"style": "Jirai Kei"})
    print(json.dumps(res2, indent=2))
    assert res2['style'] == "Jirai Kei"
    
    print("\n--- Test 3: Fixed Items (White Shirt) ---")
    res3 = gen.generate({"fixed_items": {"top": "white shirt"}})
    print(json.dumps(res3, indent=2))
    assert res3['outfit']['top'] == "white shirt"
    assert res3['outfit']['type'] == "mix_and_match"

    print("\n--- Test 4: Full Body Fixed ---")
    res4 = gen.generate({"fixed_items": {"full_body": "kimono"}})
    print(json.dumps(res4, indent=2))
    assert res4['outfit']['full_body'] == "kimono"
    assert 'top' not in res4['outfit']

    print("\nAll tests passed!")

if __name__ == "__main__":
    test()
