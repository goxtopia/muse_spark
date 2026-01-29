import streamlit as st
import json
import os
from prompt_gen.generator import PromptGenerator

# Persist custom tags
TAGS_FILE = os.path.join(os.path.dirname(__file__), 'prompt_gen', 'data', 'custom_tags.json')

def load_custom_tags():
    if os.path.exists(TAGS_FILE):
        with open(TAGS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'prefix': '', 'suffix': ''}

def save_custom_tags(prefix, suffix):
    with open(TAGS_FILE, 'w', encoding='utf-8') as f:
        json.dump({'prefix': prefix, 'suffix': suffix}, f, ensure_ascii=False, indent=2)

st.set_page_config(page_title="Random Prompt Generator", layout="wide")

@st.cache_resource
def get_generator():
    return PromptGenerator()

gen = get_generator()

st.title("🎨 Random Prompt Generator")

with st.sidebar:
    st.header("Configuration")
    
    # Gender
    genders = gen.data['characters']['genders']
    gender = st.selectbox("Gender", genders)
    
    # Style
    styles = gen.data['characters']['styles'].get(gender, [])
    style = st.selectbox("Style", ["Random"] + styles)
    
    # Include Categories
    all_categories = ['outfit', 'atmosphere', 'camera', 'environment', 'pose', 'hairstyle']
    include = st.multiselect("Include Categories", all_categories, default=all_categories)
    
    # Fixed Items for Outfit
    with st.expander("Fixed Outfit Items"):
        st.caption("Random=随机生成, None=不添加, 其他=固定使用")
        outfit_items = gen.data['outfits']['items']
        
        # Helper to get item names from a category
        def get_item_names(category):
            return ["Random", "None"] + [item['name'] for item in outfit_items.get(category, [])]
        
        fixed_full = st.selectbox("Full Body (Overrides Top/Bottom)", get_item_names('full_body'), key="full_body")
        fixed_top = st.selectbox("Top", get_item_names('top'), key="top")
        fixed_bottom = st.selectbox("Bottom", get_item_names('bottom'), key="bottom")
        fixed_shoes = st.selectbox("Shoes", get_item_names('shoes'), key="shoes")
        fixed_legwear = st.selectbox("Legwear (Socks/Stockings)", get_item_names('legwear'), key="legwear")
        fixed_neckwear = st.selectbox("Neckwear", get_item_names('neckwear'), key="neckwear")
        fixed_headwear = st.selectbox("Headwear", get_item_names('headwear'), key="headwear")
        fixed_bags = st.selectbox("Bags", get_item_names('bags'), key="bags")
        fixed_accessories = st.selectbox("Accessories", get_item_names('accessories'), key="accessories")
        
        fixed_items = {}
        # None means explicitly skip, Random means random generation
        if fixed_full not in ["Random", "None"]:
            fixed_items['full_body'] = fixed_full
        elif fixed_full == "None":
            fixed_items['full_body'] = "__NONE__"
        else:
            if fixed_top not in ["Random", "None"]: fixed_items['top'] = fixed_top
            elif fixed_top == "None": fixed_items['top'] = "__NONE__"
            if fixed_bottom not in ["Random", "None"]: fixed_items['bottom'] = fixed_bottom
            elif fixed_bottom == "None": fixed_items['bottom'] = "__NONE__"
        
        if fixed_shoes not in ["Random", "None"]: fixed_items['shoes'] = fixed_shoes
        elif fixed_shoes == "None": fixed_items['shoes'] = "__NONE__"
        if fixed_legwear not in ["Random", "None"]: fixed_items['legwear'] = fixed_legwear
        elif fixed_legwear == "None": fixed_items['legwear'] = "__NONE__"
        if fixed_neckwear not in ["Random", "None"]: fixed_items['neckwear'] = fixed_neckwear
        elif fixed_neckwear == "None": fixed_items['neckwear'] = "__NONE__"
        if fixed_headwear not in ["Random", "None"]: fixed_items['headwear'] = fixed_headwear
        elif fixed_headwear == "None": fixed_items['headwear'] = "__NONE__"
        if fixed_bags not in ["Random", "None"]: fixed_items['bags'] = fixed_bags
        elif fixed_bags == "None": fixed_items['bags'] = "__NONE__"
        if fixed_accessories not in ["Random", "None"]: fixed_items['accessories'] = fixed_accessories
        elif fixed_accessories == "None": fixed_items['accessories'] = "__NONE__"

    # Fixed Atmosphere
    with st.expander("Fixed Atmosphere"):
        moods = gen.data['atmosphere']['moods']
        fixed_atmosphere = st.selectbox("Mood", ["Random"] + moods, key="atmosphere")
    
    # Fixed Pose
    with st.expander("Fixed Pose"):
        poses = gen.data['poses']['poses']
        fixed_pose = st.selectbox("Pose", ["Random"] + poses, key="pose")
    
    # Fixed Environment
    with st.expander("Fixed Environment"):
        env_data = gen.data['environment']
        fixed_location = st.selectbox("Location", ["Random"] + env_data['locations'], key="location")
        fixed_weather = st.selectbox("Weather", ["Random"] + env_data['weather'], key="weather")
        fixed_season = st.selectbox("Season", ["Random"] + env_data['seasons'], key="season")
    
    # Fixed Camera
    with st.expander("Fixed Camera"):
        photo_data = gen.data['photography']
        fixed_angle = st.selectbox("Angle", ["Random"] + photo_data['angles'], key="angle")
        fixed_focal = st.selectbox("Focal Length", ["Random"] + photo_data['focal_length'], key="focal")
        fixed_dof = st.selectbox("Depth of Field", ["Random"] + photo_data['depth_of_field'], key="dof")
    
    # Fixed Hairstyle
    with st.expander("Fixed Hairstyle"):
        hair_data = gen.data.get('hairstyles', {})
        st.caption("Random=随机生成, None=不添加")
        
        fixed_hair_length = st.selectbox("Length", ["Random", "None"] + hair_data.get('lengths', []), key="hair_length")
        fixed_hair_style = st.selectbox("Style", ["Random", "None"] + hair_data.get('styles', []), key="hair_style")
        fixed_hair_color = st.selectbox("Color", ["Random", "None"] + hair_data.get('colors', []), key="hair_color")
        fixed_hair_bangs = st.selectbox("Bangs", ["Random", "None"] + hair_data.get('bangs', []), key="hair_bangs")
        fixed_hair_highlights = st.selectbox("Highlights", ["Random", "None"] + hair_data.get('highlights', []), key="hair_highlights")
        fixed_hair_accessory = st.selectbox("Hair Accessory", ["Random", "None"] + hair_data.get('accessories', []), key="hair_accessory")
    
    # Prefix and Suffix (with persistence)
    st.divider()
    st.subheader("Custom Tags")
    saved_tags = load_custom_tags()
    prefix_text = st.text_input("Prefix (added at start)", value=saved_tags.get('prefix', ''), placeholder="masterpiece, best quality")
    suffix_text = st.text_input("Suffix (added at end)", value=saved_tags.get('suffix', ''), placeholder="4k, detailed")
    
    # Auto-save when changed
    if prefix_text != saved_tags.get('prefix', '') or suffix_text != saved_tags.get('suffix', ''):
        save_custom_tags(prefix_text, suffix_text)

if st.button("Generate Prompt", type="primary"):
    config = {
        "gender": gender,
        "include": include,
        "fixed_items": fixed_items
    }
    if style != "Random":
        config["style"] = style
    
    # Add fixed values if not "Random"
    if fixed_atmosphere != "Random":
        config["atmosphere"] = fixed_atmosphere
    if fixed_pose != "Random":
        config["pose"] = fixed_pose
    
    # Environment
    env_config = {}
    if fixed_location != "Random":
        env_config["location"] = fixed_location
    if fixed_weather != "Random":
        env_config["weather"] = fixed_weather
    if fixed_season != "Random":
        env_config["season"] = fixed_season
    if env_config:
        config["environment"] = env_config
    
    # Camera
    camera_config = {}
    if fixed_angle != "Random":
        camera_config["angle"] = fixed_angle
    if fixed_focal != "Random":
        camera_config["focal_length"] = fixed_focal
    if fixed_dof != "Random":
        camera_config["depth_of_field"] = fixed_dof
    if camera_config:
        config["camera"] = camera_config
    
    # Hairstyle
    hairstyle_config = {}
    if fixed_hair_length not in ["Random", "None"]: hairstyle_config["length"] = fixed_hair_length
    elif fixed_hair_length == "None": hairstyle_config["length"] = "__NONE__"
    if fixed_hair_style not in ["Random", "None"]: hairstyle_config["style"] = fixed_hair_style
    elif fixed_hair_style == "None": hairstyle_config["style"] = "__NONE__"
    if fixed_hair_color not in ["Random", "None"]: hairstyle_config["color"] = fixed_hair_color
    elif fixed_hair_color == "None": hairstyle_config["color"] = "__NONE__"
    if fixed_hair_bangs not in ["Random", "None"]: hairstyle_config["bangs"] = fixed_hair_bangs
    elif fixed_hair_bangs == "None": hairstyle_config["bangs"] = "__NONE__"
    if fixed_hair_highlights not in ["Random", "None"]: hairstyle_config["highlights"] = fixed_hair_highlights
    elif fixed_hair_highlights == "None": hairstyle_config["highlights"] = "__NONE__"
    if fixed_hair_accessory not in ["Random", "None"]: hairstyle_config["accessories"] = fixed_hair_accessory
    elif fixed_hair_accessory == "None": hairstyle_config["accessories"] = "__NONE__"
    if hairstyle_config:
        config["hairstyle"] = hairstyle_config
        
    result = gen.generate(config)
    
    # Add prefix/suffix to result
    if prefix_text:
        result['_prefix'] = prefix_text
    if suffix_text:
        result['_suffix'] = suffix_text
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("JSON Output")
        json_str = json.dumps(result, ensure_ascii=False, indent=2)
        st.code(json_str, language="json")
        st.caption("📌 点击代码块右上角的图标复制")
    
    with col2:
        # Formatted String
        st.subheader("Prompt String")
        
        parts = []
        
        # Prefix
        if prefix_text:
            parts.append(prefix_text)
        
        # Subject & Style
        subject_part = f"{result.get('gender', '')}"
        if result.get('style'):
            subject_part += f", {result['style']} style"
        parts.append(subject_part)
        
        # Hairstyle
        if 'hairstyle' in result:
            hair = result['hairstyle']
            hair_parts = []
            if 'length' in hair: hair_parts.append(hair['length'])
            if 'color' in hair: hair_parts.append(hair['color'])
            if 'style' in hair: hair_parts.append(hair['style'])
            if 'bangs' in hair: hair_parts.append(hair['bangs'])
            if 'highlights' in hair: hair_parts.append(hair['highlights'])
            if 'hair_accessory' in hair: hair_parts.append(hair['hair_accessory'])
            if hair_parts:
                parts.append(f"{' '.join(hair_parts)} hair")
        
        # Outfit
        if 'outfit' in result:
            outfit = result['outfit']
            items = []
            if 'full_body' in outfit: items.append(outfit['full_body'])
            if 'top' in outfit: items.append(outfit['top'])
            if 'bottom' in outfit: items.append(outfit['bottom'])
            if 'shoes' in outfit: items.append(outfit['shoes'])
            if 'legwear' in outfit: items.append(outfit['legwear'])
            if 'neckwear' in outfit: items.append(outfit['neckwear'])
            if 'headwear' in outfit: items.append(outfit['headwear'])
            if 'bags' in outfit: items.append(outfit['bags'])
            if 'accessories' in outfit: items.append(outfit['accessories'])
            if items:
                parts.append(f"wearing {', '.join(items)}")

        # Pose
        if 'pose' in result:
            parts.append(result['pose'])
            
        # Environment
        if 'environment' in result:
            env = result['environment']
            parts.append(f"in {env['location']}, {env['weather']}, {env['season']}")
            
        # Atmosphere
        if 'atmosphere' in result:
            parts.append(f"{result['atmosphere']} atmosphere")
            
        # Camera
        if 'camera' in result:
            cam = result['camera']
            parts.append(f"{cam['angle']}, {cam['focal_length']}, {cam['depth_of_field']}")
        
        # Suffix
        if suffix_text:
            parts.append(suffix_text)
            
        prompt_str = ", ".join(parts)
        st.code(prompt_str, language="text")
        st.caption("📌 点击代码块右上角的图标复制")

# ========== Data Management Section ==========
st.divider()
st.header("📝 Data Management")

tab1, tab2, tab3 = st.tabs(["Simple Lists", "Outfit Items", "Outfit Sets"])

with tab1:
    st.subheader("Add to Simple Lists")
    col1, col2 = st.columns(2)
    
    with col1:
        simple_category = st.selectbox(
            "Category",
            ["atmosphere.moods", "poses.poses", 
             "environment.locations", "environment.weather", "environment.seasons",
             "photography.angles", "photography.focal_length", "photography.depth_of_field"],
            key="simple_cat"
        )
    
    with col2:
        new_value = st.text_input("New Value", key="simple_value")
    
    if st.button("Add to List", key="add_simple"):
        if new_value:
            parts = simple_category.split(".")
            data_key, list_key = parts[0], parts[1]
            success = gen.add_to_list(data_key, list_key, new_value)
            if success:
                st.success(f"Added '{new_value}' to {simple_category}")
                st.cache_resource.clear()
            else:
                st.warning(f"'{new_value}' already exists in {simple_category}")
        else:
            st.error("Please enter a value")

with tab2:
    st.subheader("Add Outfit Item")
    
    col1, col2 = st.columns(2)
    with col1:
        outfit_category = st.selectbox(
            "Category",
            ["top", "bottom", "shoes", "full_body", "legwear", "neckwear", "headwear", "bags", "accessories"],
            key="outfit_cat"
        )
        item_name = st.text_input("Item Name", key="outfit_name")
    
    with col2:
        all_styles = list(set(
            gen.data['characters'].get('styles', {}).get('Female', []) +
            gen.data['characters'].get('styles', {}).get('Male', [])
        ))
        item_styles = st.multiselect("Applicable Styles", all_styles, key="outfit_styles")
    
    if st.button("Add Outfit Item", key="add_outfit"):
        if item_name and item_styles:
            success = gen.add_outfit_item(outfit_category, item_name, item_styles)
            if success:
                st.success(f"Added '{item_name}' to {outfit_category}")
                st.cache_resource.clear()
            else:
                st.warning(f"'{item_name}' already exists in {outfit_category}")
        else:
            st.error("Please enter item name and select at least one style")

with tab3:
    st.subheader("Add Outfit Set")
    
    col1, col2 = st.columns(2)
    with col1:
        all_styles = list(set(
            gen.data['characters'].get('styles', {}).get('Female', []) +
            gen.data['characters'].get('styles', {}).get('Male', [])
        ))
        set_style = st.selectbox("Style", all_styles, key="set_style")
        set_name = st.text_input("Set Name", key="set_name")
    
    with col2:
        set_items_text = st.text_area(
            "Items (one per line)", 
            placeholder="black frilly blouse\npink check mini skirt\nplatform shoes",
            key="set_items"
        )
    
    if st.button("Add Outfit Set", key="add_set"):
        if set_name and set_items_text:
            items = [i.strip() for i in set_items_text.strip().split("\n") if i.strip()]
            if items:
                success = gen.add_outfit_set(set_style, set_name, items)
                if success:
                    st.success(f"Added set '{set_name}' to {set_style}")
                    st.cache_resource.clear()
                else:
                    st.warning(f"Set '{set_name}' already exists in {set_style}")
            else:
                st.error("Please enter at least one item")
        else:
            st.error("Please enter set name and items")
