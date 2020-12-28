#! /usr/bin/env python3

from random import randint
from scapy.all import IP, TCP, send

# Create the skeleton of our packet
template = IP(dst="172.16.20.10")/TCP()
# Start lighting up those bits!
template[TCP].flags = 'UFP'

# Create a list with a large number of packets to send

# Each packet will have a random TCP dest port for attack obfuscation
xmas = []
for pktNum in range(0,100):
  xmas.extend(template)
  xmas[pktNum][TCP].dport = randint(1,65535)

# Send the list of packets
send(xmas)
