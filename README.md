# OctoPrint-Physical-Buttons

This plugin allows you to add a physical Pause (Resume) button and an emergency Stop button to OctoPrint.

Code is based almost completely on the **Octoprint-Filament plugin** by **ǝuıɥsuooɯ** (https://github.com/MoonshineSG/Octoprint-Filament).

## Setup

Using this plugin requires two push buttons connected to two of the Raspberry Pi's GPIO pins. The code uses the Raspberry Pi's internal Pull-Up resistors so each button should be connected to a GPIO pin and a ground pin.

  #### 1. Open a terminal connection to your Raspberry Pi and edit the Octoprint config file 
 
   `nano ~/.octoprint/config.yaml`
 
Scroll down to the **plugins** section using the arrow keys.
 
 ```
plugins:
```
Insert the below inside the plugins section keeping the spaces:
 ```
  buttons:
    pause: XX
    stop: XX
    bounce: 400
```
XX are the GPIO pin numbers on your Raspberry Pi to which the buttons are connected.
Note that the current version of the plugin uses *physical pin numbers*, e.g., on a Raspberry Pi 3 GPIO21 equals physical pin 40. See also https://pinout.xyz/

Save the changes with **Ctrl-X** and then **Y** (for yes).

 #### 2. Give GPIO device access to non-root users 
 
   `sudo chmod a+rw /dev/gpiomem`
 
 #### 3. Install the plugin in OctoPrint using the **Plugin Manager** 
Download the latest version, or install directly using the URL:  

https://github.com/netlands/OctoPrint-Physical-Buttons/archive/master.zip
 
Click **Settings** (the Tool icon at the top) > **Plugin Manager**

Click the **Get More** button, and under **... from URL** enter the above URL and click install **Install**. 
 
 OR alternatively
 
Click the **Get More** button, and under **... from an uploaded archive** click **Browse**. Browse to the downloaded .zip file and click **Install**. 

Restart OctoPrint to complete the installation.

  #### 4. Once Octoprint is restarted, test the installation using the web **get** API
 
 Simply type the URL in your browser :
 
 http://octopi.local/plugin/buttons/status?apikey=xxxxxxxxxxx
 
 Where octopi.local is the local domain or IP of your OctoPrint server and the API key is the one found under  **Settings** (the Tool icon at the top) > **API**
 
 It should return something like below 
 - `{pause: "-1"}` the pause button is not setup
- `{pause: "1"}` the pause button is being pressed (ON)
- `{pause: "0"}` the pause button is not pressed (OFF)

## Note
If you use the plugin please feel free to [tip the original source](https://paypal.me/ovidiuhossu).
