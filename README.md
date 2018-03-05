# OctoPrint-Physical-Buttons

This plugin allows you to add a physical Pause/Start and Stop button to OctoPrint.

Code is based almost completly on the Octoprint-Filament plugin by ǝuıɥsuooɯ (https://github.com/MoonshineSG/Octoprint-Filament).


## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/netlands/OctoPrint-Physical-Buttons/archive/master.zip

Using this plugin requires a two buttons connected to two of the Raspberry Pi's GPIO pins. The code is set to use the Raspberry Pi's internal Pull-Up resistors, so the switch should be between your detection pin and a ground pin.

This plugin is using the GPIO.BOARD numbering scheme, the pin being used needs to be selected by the physical pin number.