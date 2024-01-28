import os
import random
import subprocess
import sys


def get_random_image(wallpapers: list, wallpaper_storage) -> str:
    sizeof = len(wallpapers)
    f_name = os.path.join(wallpaper_storage, wallpapers[random.randint(0,sizeof -1)])
    return f_name

def get_monitors() -> list:
    monitors = []
    output = subprocess.check_output('hyprctl monitors|grep Monitor', shell=True).decode().split('\n')
    output = [x for x in output if x != '']   #removes empty list item
    [monitors.append(m.split()[1]) for m in output]
    return monitors

def get_activeworkspace() -> str:
    output = subprocess.check_output('hyprctl activeworkspace|head -1', shell=True).decode().split()
    return output[len(output)-1].replace(':','')

def set_wallpaper_on_activeworkspace(image: str, workspace: str): 
    subprocess.run(f'hyprctl hyprpaper preload "{image}"', shell=True)
    subprocess.run(f'hyprctl hyprpaper wallpaper "{workspace},{image}"', shell=True)

def unload_all_images():
    subprocess.run('hyprctl hyprpaper unload all', shell=True)

def find_cmd(cmd) -> bool:
    try:
      subprocess.check_output(cmd, shell=True)
      return True
    except subprocess.CalledProcessError as e:
      return False

def check_environment():
    if not find_cmd('which hyprctl'):
        print("Check your Hyprland installation")
        sys.exit(1)

    if not find_cmd('which hyprpaper'):
        print("Check your Hyprpaper installation")
        sys.exit(1)