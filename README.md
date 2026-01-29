# Prompt Generator

This project provides a flexible and extensible random prompt generator for character illustrations. It allows for detailed configuration of characters, outfits, environments, poses, and photography settings.

## Overview

The core of the system is the `PromptGenerator` class, which loads data from JSON configuration files and generates structured dictionaries describing a scene.

## Components

### 1. Generator (`prompt_gen/generator.py`)
The main class `PromptGenerator` handles the loading of data and the logic for randomization. It supports generating:
- **Character**: Gender and Style.
- **Outfit**: Either a pre-defined set or a mix-and-match combination of items.
- **Environment**: Location, weather, and season.
- **Pose**: Context-aware poses based on the environment.
- **Camera**: Photography settings like angle, focal length, and depth of field.
- **Hairstyle**: Detailed hairstyle configuration.

### 2. Data Files (`prompt_gen/data/`)
The content is stored in JSON files:
- `characters.json`: Genders and styles.
- `outfits.json`: Clothing items, accessories, and pre-defined outfit sets.
- `environment.json`: Locations, weather conditions, and seasons.
- `poses.json`: Universal poses and scene-specific poses.
- `photography.json`: Camera settings.
- `atmosphere.json`: Moods and atmospheres.
- `hairstyles.json`: Hair lengths, styles, colors, etc.

## Interfaces

The `PromptGenerator` class exposes several methods:

### `generate(config=None)`
Generates a random prompt configuration.
- **config**: An optional dictionary to override or fix specific values (e.g., `{'gender': 'Female', 'style': 'Cyberpunk'}`).
- **Returns**: A dictionary containing the generated attributes.

### Data Management Methods
- `add_outfit_item(category, name, styles)`: Adds a new clothing or accessory item.
    - `category`: e.g., "top", "shoes", "accessories".
    - `name`: The description of the item.
    - `styles`: A list of styles this item fits (e.g., `["Casual", "Streetwear"]`).
- `add_outfit_set(style, name, items)`: Adds a new pre-defined outfit set.
    - `style`: The style category of the set.
    - `name`: Name of the set.
    - `items`: A list of strings describing the items (Top, Bottom, Legwear, Shoes, Accessories).
- `add_environment_item(category, value)`: Adds location, weather, or season.
- `add_photography_item(category, value)`: Adds camera settings.

## Random Generation Logic

### Outfit Selection
When generating an outfit, the system decides between using a **Pre-defined Set** or a **Mix-and-Match** combination.

**Probability Logic:**
The probability of choosing a set is dynamically calculated to ensure balance as more items or sets are added.
$$ P(\text{use\_set}) = \frac{N_{sets}}{N_{max\_category} + N_{sets}} $$
Where:
- $N_{sets}$ is the number of defined sets for the chosen style.
- $N_{max\_category}$ is the count of the most populous item category (e.g., tops, bottoms) available for that style.

This means if there are many individual items and few sets, the system prefers mix-and-match. If sets are abundant relative to individual items, the chance of picking a set increases.

### Context-Aware Poses
Poses are selected based on the generated environment.
- If the environment matches a key in `scene_poses`, there is a 60% chance to pick a pose specific to that scene.
- Otherwise, a universal pose is selected.

## Usage Example

```python
from prompt_gen.generator import PromptGenerator

gen = PromptGenerator()

# Generate a completely random prompt
prompt = gen.generate()
print(prompt)

# Generate with constraints
config = {
    'gender': 'Female',
    'style': 'Cyberpunk',
    'environment': {'location': 'Neon City Street'}
}
prompt = gen.generate(config)
print(prompt)
```
