# hypprchanger
This is a tool that changes the hyprpaper wallpaper on all of my monitors automatically.  It can also change the wallpaper on a particular monitor on demand.  It works by randomly selecting a wallpaper from your defined wallpapers directory (currently $HOME/Pictures/wallpapers) and using hypprpaper to set it. 

# Requirements
* Hyprland
* Hyprpaper
* Python

# Installation
1. Copy this repo contents to a place hyprland can see it (I place mine in my ~/.config/hypr directory)
2. Add the following lines to your hyprland.conf:
   ```
   exec-once = $HOME/.config/hypr/hyprpaper_preload.py
   exec-once = $HOME/.config/hypr/hyppyserver.py
   bind = $mainMod, Z, exec, ~/.config/hypr/hyprpaper_set.py
   ```
3. Add desired wallpapers to $HOME/Pictures/wallpapers
4. The bind statement above allows you to update the wallpaper on the active workspace with a keystroke.  I've set mine to CMD-z ... but change to whatever you like.

# Use
Log out then back in.  Logging in will start the hyppyserver process that simply loops every 600 seconds and randomly sets a wallpaper on all of your monitors.  It does unload your wallpapers from memory so it won't glog up your RAM with wallpaper images.  



