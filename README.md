# OctoPrint-Physical-Buttons

This plugin allows you to add a physical Pause/Start and Stop button to OctoPrint.

Code is based almost completly on the Octoprint-Filament plugin by ǝuıɥsuooɯ (https://github.com/MoonshineSG/Octoprint-Filament).


## Setup

Using this plugin requires two push buttons connected to two of the Raspberry Pi's GPIO pins. The code uses the Raspberry Pi's internal Pull-Up resistors. Each button should be connected to a GPIO pin and a ground pin.



=== How to install ===

 1- Edit the Octoprint config file manually 
 
 - `nano ~/.octoprint/config.yaml`
 go down to the plugins section using arrows, and insert the filament settings
 
 inside the
 ```
plugins:
```
section,  

insert this respecting the spaces:
 ```
  buttons:
    pause: XX
    stop: XX
    bounce: 400
```
Where XX is the GPIO pin number on your Raspberry Pi where the buttons are connected.
Note that the plugin uses physical pin numbers, e.g., on a Raspberry Pi 3 GPIO21 equals physical pin 40. See https://pinout.xyz/

Save by typing ctrl-X and then Y (for yes)

 2- Give access to non-root user to the GPIO device
 
  - `sudo chmod a+rw /dev/gpiomem`
 
 3- install the plugin using the [Plugin Manager](http://octopi.local/#settings_plugin_pluginmanager)
 in the Octoprint web interface.
 
Download the install from this URL:
    https://github.com/netlands/OctoPrint-Physical-Buttons/archive/master.zip
Install and then follow the instructions to restart Octoprint.

 4- Once Octoprint is restarted, test your sensor using the web get API.
 
 Simply type the URL in your browser :
 
 http://octopi.local/plugin/buttons/status?apikey=xxxxxxxxxxx
 
 Where octopi.local is the local domain or IP of your octoprint server and the API key is the one found in http://octopi.local/#settings_api
 
 It should return 
 - `{status: "-1"}` the pause button is not setup
- `{status: "1"}` the pause button is pressed (ON)
- `{status: "0"}` the pause button is not pressed (OFF)

### Donate
If you use the plugin please feel free to [tip the original source](https://paypal.me/ovidiuhossu).
