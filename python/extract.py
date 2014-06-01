#!/usr/bin/python

import sys, re
from pprint import pprint

# Constants
# Credits to Wicher Minnaard:  http://www.dfrws.org/2014eu/proceedings/DFRWS-EU-2014-13.pdf

BEACON_REGEX = b'\x80\x00\x00\x00(?:\xff){6}(.{6})\\1'
PROBE_REGEX = b'\x40(?:\x00|\x10)\x00\x00(?:\xff){6}(.{6})(?:\xff){6}'

# Arguments

if len(sys.argv) < 2:
	print "Don't forget to supply the memory dump file..."
	sys.exit(1)

dump = open(sys.argv[1]).read()

# Go go go

beacon_pattern  = re.compile(BEACON_REGEX)
probe_pattern = re.compile(PROBE_REGEX)

def as_hex(mac):
	return ":".join("{:02x}".format(ord(c)) for c in mac)

print "[X] Detected beacon MAC addresses:"

for mac in set(re.findall(beacon_pattern, dump)):
	print as_hex(mac)

print
print "[X] Detected probe MAC addresses:"

for mac in set(re.findall(probe_pattern, dump)):
	print as_hex(mac)
