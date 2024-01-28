"""
Provides several functions to dynamically manage wallpapers and monitors in Hyprland

* get_random_image
* get_monitors
* get_activeworkspace
* set_wallpaper_on_activeworkspace
* find_cmd
* check_environment
* process_ipc reads json input to send commands to the hypprserver.  Currently only one command is supported which is halt.
  The json structure for this is 

    "commands": {
        "execute": [
            "halt"
        ]
    }
}
* read_ipc loads the json input for process_ipc
* cleanup_ipc removes the ipc file after processing

"""