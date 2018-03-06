---


---

<h1 id="octoprint-physical-buttons">OctoPrint-Physical-Buttons</h1>
<p>This plugin allows you to add a physical Pause (Resume) and a Stop (Start) to OctoPrint.</p>
<p>Code is based almost completely on the <strong>Octoprint-Filament plugin</strong> by <strong>ǝuıɥsuooɯ</strong> (<a href="https://github.com/MoonshineSG/Octoprint-Filament">https://github.com/MoonshineSG/Octoprint-Filament</a>).</p>
<h2 id="setup">Setup</h2>
<p>Using this plugin requires two push buttons connected to two of the Raspberry Pi’s GPIO pins. The code uses the Raspberry Pi’s internal Pull-Up resistors so each button should be connected to a GPIO pin and a ground pin.</p>
<h4 id="open-a-terminal-connection-to-your-raspberry-pi-and-edit-the-octoprint-config-file">1. Open a terminal connection to your Raspberry Pi and edit the Octoprint config file</h4>
<p><code>nano ~/.octoprint/config.yaml</code></p>
<p>Scroll down to the <strong>plugins</strong> section using the arrow keys.</p>
<pre><code>plugins:
</code></pre>
<p>Insert the below inside the plugins section keeping the spaces:</p>
<pre><code> buttons:
   pause: XX
   stop: XX
   bounce: 400
</code></pre>
<p>XX are the GPIO pin numbers on your Raspberry Pi to which the buttons are connected.<br>
Note that the current version of the plugin uses <em>physical pin numbers</em>, e.g., on a Raspberry Pi 3 GPIO21 equals physical pin 40. See also <a href="https://pinout.xyz/">https://pinout.xyz/</a></p>
<p>Save the changes with <strong>Ctrl-X</strong> and then <strong>Y</strong> (for yes).</p>
<h4 id="give-gpio-device-access-to-non-root-users">2. Give GPIO device access to non-root users</h4>
<p><code>sudo chmod a+rw /dev/gpiomem</code></p>
<h4 id="install-the-plugin-in-octoprint-using-the-plugin-manager">3. Install the plugin in OctoPrint using the <strong>Plugin Manager</strong></h4>
<p>Download the latest  install from the below URL:  <a href="https://github.com/netlands/OctoPrint-Physical-Buttons/archive/master.zip">https://github.com/netlands/OctoPrint-Physical-Buttons/archive/master.zip</a></p>
<p>Click <strong>Settings</strong> (the Tool icon at the top) &gt; <strong>Plugin Manager</strong></p>
<p>Click the <strong>Get More</strong> button, and under <strong>… from an uploaded archive</strong> click <strong>Browse</strong>. Browse to the downloaded .zip file and click <strong>Install</strong>.</p>
<p>Restart OctoPrint to complete the installation.</p>
<h4 id="once-octoprint-is-restarted-test-the-installation-using-the-web-get-api">4. Once Octoprint is restarted, test the installation using the web <strong>get</strong> API</h4>
<p>Simply type the URL in your browser :</p>
<p><a href="http://octopi.local/plugin/buttons/status?apikey=xxxxxxxxxxx">http://octopi.local/plugin/buttons/status?apikey=xxxxxxxxxxx</a></p>
<p>Where octopi.local is the local domain or IP of your OctoPrint server and the API key is the one found under  <strong>Settings</strong> (the Tool icon at the top) &gt; <strong>API</strong></p>
<p>It should return something like below</p>
<ul>
<li><code>{pause: "-1"}</code> the pause button is not setup</li>
<li><code>{pause: "1"}</code> the pause button is being pressed (ON)</li>
<li><code>{pause: "0"}</code> the pause button is not pressed (OFF)</li>
</ul>
<h2 id="note">Note</h2>
<p>If you use the plugin please feel free to <a href="https://paypal.me/ovidiuhossu">tip the original source</a>.</p>

