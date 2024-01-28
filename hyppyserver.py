#!/usr/bin/python3

import time
import os
from hypprchangerlibs.hyprlib import check_environment
from hypprchangerlibs.hyprlib import unload_all_images
from hypprchangerlibs.hypprchangerlibs import check_ipc_file
from hypprchangerlibs.hyprlib import get_monitors
from hypprchangerlibs.hyprlib import get_random_image
from hypprchangerlibs.hyprlib import set_wallpaper_on_activeworkspace




if __name__ == '__main__':
    wallpaper_storage = os.path.join(os.environ.get('HOME'),'Pictures/wallpapers')
    
    # check environment
    check_environment()

    print("Starting server")
    ipc_file = '/tmp/ipc.json'
    while True:
        wallpapers = os.listdir(wallpaper_storage)
        check_ipc_file(ipc_file=ipc_file)
        # do the things
        print('Changing the wallpapers')
        unload_all_images()
        for monitor in get_monitors():
            img = get_random_image(wallpaper_storage=wallpaper_storage, wallpapers=wallpapers)
            set_wallpaper_on_activeworkspace(image=img, workspace=monitor)
            
        time.sleep(600)