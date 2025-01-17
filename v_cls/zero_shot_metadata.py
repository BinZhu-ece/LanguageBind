import os

import pandas as pd

OPENAI_IMAGENET_TEMPLATES = (
    lambda c: f'a bad video of a {c}.',
    lambda c: f'a video of many {c}.',
    lambda c: f'a sculpture of a {c}.',
    lambda c: f'a video of the hard to see {c}.',
    lambda c: f'a low resolution video of the {c}.',
    lambda c: f'a rendering of a {c}.',
    lambda c: f'graffiti of a {c}.',
    lambda c: f'a bad video of the {c}.',
    lambda c: f'a cropped video of the {c}.',
    lambda c: f'a tattoo of a {c}.',
    lambda c: f'the embroidered {c}.',
    lambda c: f'a video of a hard to see {c}.',
    lambda c: f'a bright video of a {c}.',
    lambda c: f'a video of a clean {c}.',
    lambda c: f'a video of a dirty {c}.',
    lambda c: f'a dark video of the {c}.',
    lambda c: f'a drawing of a {c}.',
    lambda c: f'a video of my {c}.',
    lambda c: f'the plastic {c}.',
    lambda c: f'a video of the cool {c}.',
    lambda c: f'a close-up video of a {c}.',
    lambda c: f'a black and white video of the {c}.',
    lambda c: f'a painting of the {c}.',
    lambda c: f'a painting of a {c}.',
    lambda c: f'a pixelated video of the {c}.',
    lambda c: f'a sculpture of the {c}.',
    lambda c: f'a bright video of the {c}.',
    lambda c: f'a cropped video of a {c}.',
    lambda c: f'a plastic {c}.',
    lambda c: f'a video of the dirty {c}.',
    lambda c: f'a jpeg corrupted video of a {c}.',
    lambda c: f'a blurry video of the {c}.',
    lambda c: f'a video of the {c}.',
    lambda c: f'a good video of the {c}.',
    lambda c: f'a rendering of the {c}.',
    lambda c: f'a {c} in a video game.',
    lambda c: f'a video of one {c}.',
    lambda c: f'a doodle of a {c}.',
    lambda c: f'a close-up video of the {c}.',
    lambda c: f'a video of a {c}.',
    lambda c: f'the origami {c}.',
    lambda c: f'the {c} in a video game.',
    lambda c: f'a sketch of a {c}.',
    lambda c: f'a doodle of the {c}.',
    lambda c: f'a origami {c}.',
    lambda c: f'a low resolution video of a {c}.',
    lambda c: f'the toy {c}.',
    lambda c: f'a rendition of the {c}.',
    lambda c: f'a video of the clean {c}.',
    lambda c: f'a video of a large {c}.',
    lambda c: f'a rendition of a {c}.',
    lambda c: f'a video of a nice {c}.',
    lambda c: f'a video of a weird {c}.',
    lambda c: f'a blurry video of a {c}.',
    lambda c: f'a cartoon {c}.',
    lambda c: f'art of a {c}.',
    lambda c: f'a sketch of the {c}.',
    lambda c: f'a embroidered {c}.',
    lambda c: f'a pixelated video of a {c}.',
    lambda c: f'itap of the {c}.',
    lambda c: f'a jpeg corrupted video of the {c}.',
    lambda c: f'a good video of a {c}.',
    lambda c: f'a plushie {c}.',
    lambda c: f'a video of the nice {c}.',
    lambda c: f'a video of the small {c}.',
    lambda c: f'a video of the weird {c}.',
    lambda c: f'the cartoon {c}.',
    lambda c: f'art of the {c}.',
    lambda c: f'a drawing of the {c}.',
    lambda c: f'a video of the large {c}.',
    lambda c: f'a black and white video of a {c}.',
    lambda c: f'the plushie {c}.',
    lambda c: f'a dark video of a {c}.',
    lambda c: f'itap of a {c}.',
    lambda c: f'graffiti of the {c}.',
    lambda c: f'a toy {c}.',
    lambda c: f'itap of my {c}.',
    lambda c: f'a video of a cool {c}.',
    lambda c: f'a video of a small {c}.',
    lambda c: f'a tattoo of the {c}.',
)


# a much smaller subset of above prompts
# from https://github.com/openai/CLIP/blob/main/notebooks/Prompt_Engineering_for_ImageNet.ipynb
SIMPLE_IMAGENET_TEMPLATES = (
    lambda c: f'itap of a {c}.',
    lambda c: f'a bad video of the {c}.',
    lambda c: f'a origami {c}.',
    lambda c: f'a video of the large {c}.',
    lambda c: f'a {c} in a video game.',
    lambda c: f'art of the {c}.',
    lambda c: f'a video of the small {c}.',
)

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kinetics_400_labels.csv")
IMAGENET_CLASSNAMES = tuple(pd.read_csv(PATH).values[:, 1])

