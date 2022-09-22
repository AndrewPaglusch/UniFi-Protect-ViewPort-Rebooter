# UniFi-Protect-Viewport-Rebooter
A script to automatically reboot all discovered UniFi Protect Viewports connected to your NVR (UDM, UDM Pro, UNVR, UNVR Pro, etc..)

## Background

I have a problem with my UniFi Protect Viewports where the framerate of all cameras feeds will drop to ~1FPS if the Viewports have been up and running for more than about 12 hours.
This script was created as a bandage fix. I call it with cron every 8 hours so that my Viewports are always running nice and fast.

Hopefully Ubiquiti will fix this bug so this script won't be needed anymore.

## Configuration

Edit the script and include the IP address or FQDN of your NVR.
Replace the credentials in the script with administive credentials for the NVR.

## Cron Job
```
0 */8 * * * /opt/unifi-protect-viewport-restart.py
```
