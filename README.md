# UniFi Protect ViewPort Rebooter
A script to automatically reboot all discovered [UniFi Protect ViewPorts (UFP-VIEWPORT)](https://store.ui.com/collections/unifi-protect-accessories/products/unifi-protect-viewport) connected to your NVR (UDM, UDM Pro, UNVR, UNVR Pro, etc..)

## Background

I have a problem with my UniFi Protect ViewPorts where the framerate of all cameras feeds will drop to ~1FPS if the ViewPorts have been up and running for more than about 12 hours.
This script was created as a bandage fix. I call it with cron every 8 hours so that my ViewPorts are always running nice and fast.

Hopefully Ubiquiti will fix [this bug](https://community.ui.com/questions/Viewport-video-becomes-sluggish-after-a-few-days/42cdd58b-0b41-47a8-b385-e91dafd5f144) so this script won't be needed anymore.

## Configuration

Edit the script and include the IP address or FQDN of your NVR.
Replace the credentials in the script with administive credentials for the NVR.

## Cron Job
```
0 */8 * * * /opt/unifi-protect-viewport-restart.py
```
