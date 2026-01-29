import json
import os
import random

class PromptGenerator:
    def __init__(self, data_dir=None):
        if data_dir is None:
            data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.data_dir = data_dir
        self.data = {}
        self._load_data()

    def _load_data(self):
        files = [
            'characters.json', 'outfits.json', 'environment.json',
            'photography.json', 'poses.json', 'atmosphere.json', 'hairstyles.json'
        ]
        for f in files:
            key = f.replace('.json', '')
            path = os.path.join(self.data_dir, f)
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as file:
                    self.data[key] = json.load(file)

    def generate(self, config=None):
        if config is None:
            config = {}

        result = {}

        # 1. Gender and Style
        gender = config.get('gender')
        if not gender:
            gender = random.choice(self.data['characters']['genders'])
        result['gender'] = gender

        style = config.get('style')
        if not style:
            styles = self.data['characters']['styles'].get(gender, [])
            style = random.choice(styles) if styles else None
        result['style'] = style

        # Categories to include
        include = config.get('include', [
            'outfit', 'atmosphere', 'camera', 'environment', 'pose', 'hairstyle'
        ])

        if 'outfit' in include:
            result['outfit'] = self._generate_outfit(style, config.get('fixed_items', {}))
        
        if 'atmosphere' in include:
            if config.get('atmosphere'):
                result['atmosphere'] = config['atmosphere']
            else:
                result['atmosphere'] = random.choice(self.data['atmosphere']['moods'])
        
        # Generate environment FIRST (so pose can use location)
        if 'environment' in include:
            env_data = self.data['environment']
            env_config = config.get('environment', {})
            result['environment'] = {
                'location': env_config.get('location') or random.choice(env_data['locations']),
                'weather': env_config.get('weather') or random.choice(env_data['weather']),
                'season': env_config.get('season') or random.choice(env_data['seasons'])
            }
        
        # Generate pose (with scene awareness)
        if 'pose' in include:
            if config.get('pose'):
                result['pose'] = config['pose']
            else:
                location = result.get('environment', {}).get('location', '')
                result['pose'] = self._generate_pose(location)

        if 'camera' in include:
            photo_data = self.data['photography']
            camera_config = config.get('camera', {})
            result['camera'] = {
                'angle': camera_config.get('angle') or random.choice(photo_data['angles']),
                'focal_length': camera_config.get('focal_length') or random.choice(photo_data['focal_length']),
                'depth_of_field': camera_config.get('depth_of_field') or random.choice(photo_data['depth_of_field'])
            }

        if 'hairstyle' in include:
            result['hairstyle'] = self._generate_hairstyle(config.get('hairstyle', {}))

        return result

    def _generate_outfit(self, style, fixed_items):
        outfits_data = self.data['outfits']
        sets = outfits_data.get('sets', {}).get(style, [])
        items_data = outfits_data.get('items', {})

        # Decision: Set vs Mix-and-Match
        # If any item is fixed, we must use mix-and-match (simplification)
        use_set = False
        if not fixed_items and sets:
            # 50% chance to use a set if available
            use_set = random.random() < 0.5
        
        if use_set:
            chosen_set = random.choice(sets)
            # Convert set items to consistent format
            outfit = {"type": "set", "set_name": chosen_set['name']}
            items = chosen_set['items']
            # Parse items into categories (heuristic based on position/content)
            if len(items) >= 1: outfit["top"] = items[0]
            if len(items) >= 2: outfit["bottom"] = items[1]
            if len(items) >= 3: outfit["legwear"] = items[2]
            if len(items) >= 4: outfit["shoes"] = items[3]
            if len(items) >= 5: outfit["accessories"] = items[4]
            return outfit
        
        # Mix and Match
        outfit = {"type": "mix_and_match"}
        
        # Determine base structure: Full Body vs Top/Bottom
        mode = "random"
        if "full_body" in fixed_items:
            mode = "full_body"
        elif "top" in fixed_items or "bottom" in fixed_items:
            mode = "two_piece"
        
        if mode == "random":
            # Check if full_body items exist for this style
            full_body_candidates = [i for i in items_data.get("full_body", []) if style in i.get('styles', [])]
            # If no full body candidates for style, prefer two_piece, but still give it a small chance if generic items exist
            if full_body_candidates:
                 mode = random.choice(["full_body", "two_piece"])
            else:
                 mode = "two_piece"

        if mode == "full_body":
            if "full_body" in fixed_items:
                if fixed_items["full_body"] != "__NONE__":
                    outfit["full_body"] = fixed_items["full_body"]
            else:
                outfit["full_body"] = self._get_random_item(items_data, "full_body", style)
        else:
            # Top
            if "top" in fixed_items:
                if fixed_items["top"] != "__NONE__":
                    outfit["top"] = fixed_items["top"]
            else:
                outfit["top"] = self._get_random_item(items_data, "top", style)
            
            # Bottom
            if "bottom" in fixed_items:
                if fixed_items["bottom"] != "__NONE__":
                    outfit["bottom"] = fixed_items["bottom"]
            else:
                outfit["bottom"] = self._get_random_item(items_data, "bottom", style)

        # Shoes
        if "shoes" in fixed_items:
            if fixed_items["shoes"] != "__NONE__":
                outfit["shoes"] = fixed_items["shoes"]
        else:
            outfit["shoes"] = self._get_random_item(items_data, "shoes", style)

        # Legwear (socks/stockings) - 60% chance
        if "legwear" in fixed_items:
            if fixed_items["legwear"] != "__NONE__":
                outfit["legwear"] = fixed_items["legwear"]
        elif random.random() < 0.6:
            outfit["legwear"] = self._get_random_item(items_data, "legwear", style)

        # Neckwear - 50% chance
        if "neckwear" in fixed_items:
            if fixed_items["neckwear"] != "__NONE__":
                outfit["neckwear"] = fixed_items["neckwear"]
        elif random.random() < 0.5:
            outfit["neckwear"] = self._get_random_item(items_data, "neckwear", style)

        # Headwear - 40% chance
        if "headwear" in fixed_items:
            if fixed_items["headwear"] != "__NONE__":
                outfit["headwear"] = fixed_items["headwear"]
        elif random.random() < 0.4:
            outfit["headwear"] = self._get_random_item(items_data, "headwear", style)

        # Bags - 40% chance
        if "bags" in fixed_items:
            if fixed_items["bags"] != "__NONE__":
                outfit["bags"] = fixed_items["bags"]
        elif random.random() < 0.4:
            outfit["bags"] = self._get_random_item(items_data, "bags", style)

        # Accessories - 70% chance
        if "accessories" in fixed_items:
            if fixed_items["accessories"] != "__NONE__":
                outfit["accessories"] = fixed_items["accessories"]
        elif random.random() < 0.7:
            outfit["accessories"] = self._get_random_item(items_data, "accessories", style)

        return outfit

    def _generate_hairstyle(self, config):
        """Generate hairstyle with optional fixed values"""
        hair_data = self.data.get('hairstyles', {})
        result = {}
        
        # Helper to get value - supports fixed, __NONE__, or random
        def get_value(key, data_key):
            if key in config:
                if config[key] == "__NONE__":
                    return None
                return config[key]
            items = hair_data.get(data_key, [])
            return random.choice(items) if items else None
        
        # Required fields
        length = get_value('length', 'lengths')
        if length:
            result['length'] = length
            
        style = get_value('style', 'styles')
        if style:
            result['style'] = style
            
        color = get_value('color', 'colors')
        if color:
            result['color'] = color
            
        bangs = get_value('bangs', 'bangs')
        if bangs:
            result['bangs'] = bangs
        
        # Optional fields (50% chance if not specified)
        if 'highlights' in config:
            if config['highlights'] != "__NONE__":
                result['highlights'] = config['highlights']
        elif random.random() < 0.3:
            highlights = hair_data.get('highlights', [])
            if highlights:
                result['highlights'] = random.choice(highlights)
        
        if 'accessories' in config:
            if config['accessories'] != "__NONE__":
                result['hair_accessory'] = config['accessories']
        elif random.random() < 0.4:
            accessories = hair_data.get('accessories', [])
            if accessories:
                result['hair_accessory'] = random.choice(accessories)
        
        return result

    def _generate_pose(self, location):
        """Generate pose with location awareness.
        Scene-bound poses have 60% chance when location matches.
        """
        poses_data = self.data.get('poses', {})
        universal_poses = poses_data.get('poses', [])
        scene_poses = poses_data.get('scene_poses', {})
        
        # Find matching scene poses
        matching_poses = []
        location_lower = location.lower()
        
        for scene_keywords, poses in scene_poses.items():
            # scene_keywords is comma-separated keywords
            keywords = [k.strip().lower() for k in scene_keywords.split(',')]
            if any(keyword in location_lower for keyword in keywords):
                matching_poses.extend(poses)
        
        # If we have matching scene poses, 60% chance to use them
        if matching_poses and random.random() < 0.6:
            return random.choice(matching_poses)
        
        # Otherwise use universal pose
        if universal_poses:
            return random.choice(universal_poses)
        
        return "standing"

    def _get_random_item(self, items_data, category, style):
        items = items_data.get(category, [])
        if not items:
            return None
        
        # Try to find style match
        candidates = [i for i in items if style in i.get('styles', [])]
        if not candidates:
            # Fallback: pick any
            candidates = items
        
        return random.choice(candidates)['name']

    # ========== Data Management Methods ==========
    
    def _save_data(self, key):
        """Save a specific data file"""
        file_map = {
            'characters': 'characters.json',
            'outfits': 'outfits.json', 
            'environment': 'environment.json',
            'photography': 'photography.json',
            'poses': 'poses.json',
            'atmosphere': 'atmosphere.json'
        }
        if key not in file_map:
            raise ValueError(f"Unknown data key: {key}")
        
        path = os.path.join(self.data_dir, file_map[key])
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.data[key], f, ensure_ascii=False, indent=2)
    
    def add_to_list(self, data_key, list_key, value):
        """Add a value to a simple list (e.g., atmosphere.moods, poses.poses)"""
        if data_key not in self.data:
            raise ValueError(f"Unknown data key: {data_key}")
        
        data = self.data[data_key]
        if list_key not in data:
            data[list_key] = []
        
        if value not in data[list_key]:
            data[list_key].append(value)
            self._save_data(data_key)
            return True
        return False
    
    def add_outfit_item(self, category, name, styles):
        """Add a new outfit item (e.g., top, bottom, shoes)"""
        items_data = self.data['outfits'].get('items', {})
        if category not in items_data:
            items_data[category] = []
            self.data['outfits']['items'] = items_data
        
        # Check if already exists
        for item in items_data[category]:
            if item['name'] == name:
                return False
        
        items_data[category].append({
            'name': name,
            'styles': styles
        })
        self._save_data('outfits')
        return True
    
    def add_outfit_set(self, style, name, items):
        """Add a new outfit set"""
        sets_data = self.data['outfits'].get('sets', {})
        if style not in sets_data:
            sets_data[style] = []
            self.data['outfits']['sets'] = sets_data
        
        # Check if already exists
        for s in sets_data[style]:
            if s['name'] == name:
                return False
        
        sets_data[style].append({
            'name': name,
            'items': items
        })
        self._save_data('outfits')
        return True
    
    def add_environment_item(self, category, value):
        """Add environment item (location, weather, season)"""
        return self.add_to_list('environment', category, value)
    
    def add_photography_item(self, category, value):
        """Add photography item (angles, focal_length, depth_of_field)"""
        return self.add_to_list('photography', category, value)
    
    def get_data_categories(self):
        """Get all available data categories for UI"""
        return {
            'simple_lists': {
                'atmosphere': ['moods'],
                'poses': ['poses'],
                'environment': ['locations', 'weather', 'seasons'],
                'photography': ['angles', 'focal_length', 'depth_of_field']
            },
            'outfit_categories': list(self.data['outfits'].get('items', {}).keys()),
            'outfit_styles': list(self.data['outfits'].get('sets', {}).keys()) + 
                           list(self.data['characters'].get('styles', {}).get('Female', [])) +
                           list(self.data['characters'].get('styles', {}).get('Male', []))
        }
