#!/usr/bin/python3

from hypprchangerlibs.hyprlib import get_activeworkspace
from hypprchangerlibs.hyprlib import get_random_image
from hypprchangerlibs.hyprlib import set_wallpaper_on_activeworkspace
from hypprchangerlibs.hyprlib import unload_all_images
import os

wallpaper_storage = os.path.join(os.environ.get('HOME'),'Pictures/wallpapers')
wallpapers = os.listdir(wallpaper_storage)

unload_all_images()
aws = get_activeworkspace()
image = get_random_image(wallpaper_storage=wallpaper_storage, wallpapers=wallpapers)
set_wallpaper_on_activeworkspace(image=image, workspace=aws)