# AI Research

I decided to put my AI research efforts under version control.

Most of my AI research projects are simple scripts aimed at helping me understand a concept, technique, or library.  Most of one-off type projects that do not need version control, but some are becoming more robust and useful.  Therefore, this repository was created.

## Setup

1. Notes will appear at the top of each of the scripts indicating any special setup for that script.  Typically this will be the "pip install's" that are needed.
2. Any work with the HuggingFace resources will likely need to have a HuggingFace account and access token.  Please [Sign Up](https://huggingface.co/join) or [Login](https://huggingface.co/login) when using the HugginfFace based scripts.
   1. It is also suggested you set up the [HuggingFace CLI](https://huggingface.co/docs/huggingface_hub/guides/cli) and do a command line login.  This avoids needing to put your access token into the scripts and reduces the inadvertent publication of those tokens.
3. If you want all scripts that become part of this repo, it is suggested you clone this repository and set up a virtual environment in the project folder:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

## get_image.py

The `get_image.py` script is exploring the use of the HuggingFace library to perform tasks for generating images based on a prompt.  i.e. "text-to-image".

If no options are specified, the script selects a random prompt, style, and model, and uses a default height/width of 1024px X 1024px.  These are all settings that can be overridden by passing a commandline argument.

The "style" parameter gets prefixed to the prompt to help identify what kind of output is desired - i.e. photographic vs anime.  This is an arbitrary string and can be set to anything if desired "green rose" would work, though the results may be rather creative.

The "model" parameter must be a text-to-image capable model from HuggingFace.  Even then a number of models will not work or may take much longer than another.  The selected list of "random models" have been tested and have worked in most of the test cases.  Your mileage may vary in this regard.

The "height" and "width" paramters are integers.  Some (but not all) of the models require these values to be divisible by 8 and will throw an error when this is not the case.

The "output" parameter indicates where to store the generated image.  It defaults to "output.png".

At the moment, I use this script to generate random images to fit specific parts of my web development efforts.  It is working well enough for that, though I will also fall back to [PixArt Sigma](https://huggingface.co/spaces/PixArt-alpha/PixArt-Sigma) when I need a little more control.  PixArt Sigma was the inspiration for my `get_image.py` script

Examples:

```bash
# Most basic, with random prompt, style, and model, generating a 1024x1024 image
./get_image.py
# OR: python3 get_image.py

# Specifying the prompt:
./get_image.py --prompt "I am a teapot short and stout"

# specifying the prompt and style
./get_image.py --prompt "I am a teapot short and stout" --style "Abstract"

# specifying the prompt, style, and model
./get_image.py \
    --prompt "I am a teapot short and stout" \
    --style "Abstract" \
    --model "ehristoforu/dalle-3-xl-v2"

# specifying prompt, style, model, and image size, with a negative prompt requesting no background
./get_image.py \
    --prompt "I am a teapot short and stout" \
    --negative "blurry, background" \
    --style "Abstract" \
    --model "ehristoforu/dalle-3-xl-v2" \
    --height 128 \
    --width 128
```

