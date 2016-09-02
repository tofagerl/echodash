import socket
import struct
import binascii
import os
import requests

playing = False
rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW,
                          socket.htons(0x0003))
mac = os.environ['MAC']
url = "https://pitangui.amazon.com/api/np/command"
deviceSerialNumber = os.environ['SERIAL']
deviceType = os.environ['DEVICE']
querystring = {"deviceSerialNumber":deviceSerialNumber,"deviceType":deviceType}
cookie = os.environ['COOKIE']
pausePayload = "{\"type\":\"PauseCommand\"}"
playPayload = "{\"type\":\"PlayCommand\"}"
headers = {
    'origin': "http://alexa.amazon.com",
    'csrf': "-823376386",
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
def send(playing ):
  if playing:
    payload = pausePayload
  else:
    payload = playPayload
  response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
  print(response.text, not playing)
while True:
    packet = rawSocket.recvfrom(2048)
    ethernet_header = packet[0][0:14]
    ethernet_detailed = struct.unpack('!6s6s2s', ethernet_header)
    arp_header = packet[0][14:42]
    arp_detailed = struct.unpack('2s2s1s1s2s6s4s6s4s', arp_header)
    ethertype = ethernet_detailed[2]
    if ethertype != '\x08\x06':
        continue
    source_mac = binascii.hexlify(arp_detailed[5])
    dest_ip = socket.inet_ntoa(arp_detailed[8])
    if source_mac == mac:
        send(playing)
        playing = not playing
