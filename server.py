import os
import requests
import datetime
from scapy.all import *
from config import *

state = False
url = "https://pitangui.amazon.com/api/np/command"
querystring = {"deviceSerialNumber":serial,"deviceType":device}
pausePayload = "{\"type\":\"PauseCommand\"}"
playPayload = "{\"type\":\"PlayCommand\"}"
headers = {
    'origin': "http://alexa.amazon.com",
    'csrf': csrf,
    'accept-language': "en-us",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'x-devtools-emulate-network-conditions-client-id': "974a6f17-687f-45c0-afff-b127db38615f",
    'dnt': "1",
    'referer': "http://alexa.amazon.com/spa/index.html",
    'accept-encoding': "gzip, deflate, br",
    'cookie': cookie,
    'x-cookiesok': "I explicitly accept all cookies",
    'cache-control': "no-cache",
    'postman-token': "809faf85-2ea6-d6de-cf2d-0c183f8a76c3"
    }
def send():
  global state
  if state:
    payload = pausePayload
  else:
    payload = playPayload
  response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
  st = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  if response.status_code == 200:
    status = "Paused" if state else "Now Playing"
    state = not state
    print st, status
  else:
    print "error: "+ response
def arp_display(pkt):
   if pkt[ARP].op ==1:
    if pkt[ARP].hwsrc == mac:
      send()
state = False
print "sniff", sniff(prn=arp_display, filter="arp", store=0)
