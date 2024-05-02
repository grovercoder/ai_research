#!/usr/bin/env python3

from huggingface_hub import InferenceClient
import random
import argparse

# Setup
#   Pip install the following pacakges:
#       huggingface_hub
#       Pillow
# 
# A HuggingFace access token is required.  
# This code expects the HuggingFace Command Line tool to be previously run and logged in.
#
# ------------------
# usage: get_image.py [-h] [--prompt PROMPT] [--style STYLE] [--model MODEL] [--negative NEGATIVE] [--height HEIGHT] [--width WIDTH]
#                     [--output OUTPUT]
#
# Generate a random image with optional parameters.
#
# options:
#   -h, --help           show this help message and exit
#   --prompt PROMPT      Prompt for the image generation.
#   --style STYLE        Style for the image generation.
#   --model MODEL        Model for the image generation.
#   --negative NEGATIVE  Negative prompt for the image generation. Defaults to 'blurry'
#   --height HEIGHT      Height of the image. Default: 1024
#   --width WIDTH        Width of the image. Default: 1024
#   --output OUTPUT      Output file name/path. Default: 'output.png'


# Configure / parse the script arguments
parser = argparse.ArgumentParser(description="Generate a random image with optional parameters.")
parser.add_argument("--prompt", type=str, help="Prompt for the image generation.")
parser.add_argument("--style", type=str, help="Style for the image generation.")
parser.add_argument("--model", type=str, help="Model for the image generation.")
parser.add_argument("--negative", type=str, help="Negative prompt for the image generation. Defaults to 'blurry'")
parser.add_argument("--height", type=int, help="Height of the image. Default: 1024")
parser.add_argument("--width", type=int, help="Width of the image. Default: 1024")
parser.add_argument("--output", type=str, help="Output file name/path. Default: 'output.png'")
args = parser.parse_args()

# list of random prompts if a prompt is not specified
random_prompts = [
    "A cozy cabin nestled in a snow-covered forest, with smoke curling from the chimney and a warm glow emanating from its windows.",
    "An otherworldly cityscape where skyscrapers reach towards a multi-colored sky, with flying vehicles zipping between them.",
    "A serene lakeside scene at dusk, with a lone rowboat gently drifting on the water and the sky painted in shades of orange and purple.",
    "A bustling marketplace in a vibrant, exotic city, with merchants selling their wares under colorful awnings and crowds of people milling about.",
    "A futuristic space station orbiting a distant planet, with sleek metallic structures and ships coming and going against the backdrop of a star-filled sky.",
    "A whimsical garden filled with oversized flowers and talking animals, bathed in the soft light of a magical sunset.",
    "A hidden cave deep within a jungle, illuminated by bioluminescent plants and home to ancient ruins shrouded in mystery.",
    "A steampunk-inspired cityscape with towering clockwork structures and airships soaring through the smoggy sky.",
    "A fantastical underwater kingdom where mermaids swim among colorful coral reefs and schools of tropical fish.",
    "A post-apocalyptic wasteland dominated by crumbling skyscrapers and twisted metal wreckage, with a lone figure scavenging for resources.",
    "A mystical forest blanketed in mist, with towering trees adorned with glowing runes and ethereal spirits drifting through the air.",
    "A quaint countryside village nestled between rolling hills, with thatched-roof cottages and a meandering river flowing nearby.",
    "A high-tech laboratory buzzing with activity, filled with scientists conducting experiments amidst rows of blinking consoles and futuristic machinery.",
    "A grand castle perched atop a rugged mountain peak, surrounded by swirling clouds and guarded by majestic dragons.",
    "A surreal dreamscape where gravity seems to shift and reality bends, with floating islands and surreal landscapes stretching into infinity.",
    "A beautiful person walking on the beach",
]

# a list of random styles if not specified
image_styles = [
    'Cinematic',
    'Photographic',
    'Anime',
    'Manga',
    'Digital Art',
    'Pixel Art',
    'Fantasy Art',
    'Neonpunk',
    '3D Model',
    "Realistic",
    "Cartoon/Animated",
    "Impressionistic",
    "Surreal/Fantastical",
    "Minimalist",
    "Vintage/Retro",
    "Abstract",
    "Photorealistic",
    "Gothic/Dark",
    "Pop Art",
]

# A list of default models that may be used. 
# Models must support the "text-to-image" capabilities/feature on Hugging Face
models = [
    "stabilityai/stable-diffusion-xl-base-1.0",
    "runwayml/stable-diffusion-v1-5",
    # "prompthero/openjourney-v4",
    "ehristoforu/dalle-3-xl-v2",
]

# Set the values
# Use the specified settings (if any) or the default value
prompt = args.prompt if args.prompt is not None else random.choice(random_prompts)
style = args.style if args.style is not None else random.choice(image_styles)
model = args.model if args.model is not None else random.choice(models)
height = args.height if args.height is not None else 1024
width = args.width if args.width is not None else 1024
negative_prompt = args.negative if args.negative is not None else "blurry"

print('------------------------')
print(f'Prompt   : {prompt}')
print(f'Model    : {model}')
print(f'Negative : {negative_prompt}')
print(f'Style    : {style}')
print(f'Height   : {height}')
print(f'Width    : {width}')
print('------------------------')

# Connect to Hugging Face Inferences API to get the image
final_prompt = f"Style={style}. {prompt}"
client = InferenceClient()
image = client.text_to_image(
    prompt=final_prompt, 
    negative_prompt=negative_prompt, 
    height=height,
    width=width,
    model=model
)

# Save the image to file
outputfile = args.output if args.output is not None else "output.png"
image.save(outputfile)

