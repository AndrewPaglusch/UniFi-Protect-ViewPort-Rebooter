#!/usr/bin/env python3
import requests
import json
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

URL = 'https://nvr.mydomain.net'
USERNAME = 'local-admin'
PASSWORD = 'your-password-here'

session = requests.Session()

print(f"Logging into {URL}...")
payload = {"username": USERNAME, "password": PASSWORD, "rememberMe": False}
r = session.post(f"{URL}/api/auth/login", headers={"Accept": "application/json"}, data=payload, verify=False)
r.raise_for_status()

# add the x-csrf-token header we get back to our session headers we send
session.headers.update({'x-csrf-token': r.headers['X-CSRF-Token']})

print("Getting viewport devices...")
s = session.get(f"{URL}/proxy/protect/api/bootstrap")
devices = json.loads(s.text)
viewports = []
for d in devices['viewers']:
  name = d['name']
  id = d['id']
  ip = d['host']
  viewports.append({"name": name, "id": id, "ip": ip})
  print(f"Found \"{name}\" ({id}) at {ip}")

print("Rebooting viewports...")
for vp in viewports:
  print(f"Rebooting \"{vp['name']}\"...")
  v = session.post(f"{URL}/proxy/protect/api/viewers/{vp['id']}/reboot")
  v.raise_for_status()
  reboot_result = json.loads(v.text)['isRebooting']
  print(f"\"{vp['name']}\" confirmed to be rebooting?: {reboot_result}")
