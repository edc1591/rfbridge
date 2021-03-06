#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import Adafruit_MCP3008
import math
import time

CLK  = 18
MISO = 23
MOSI = 24
CS   = 25

parser = argparse.ArgumentParser(description='Script to read AC current values from ACS712 via MCP3008.',version="0.1")
parser.add_argument('-c', action="store", default="0", dest="channel",help='ADC channel to read. Starting from 0.',type=int)
results = parser.parse_args()
channel = results.channel

mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
interval = 0.00002
num_samples = 5000
sample_time = 0.1
adc_zero = 513
prev_time = time.time() - interval
values = [0]*num_samples
i = 0
accumulated = 0
print "Reading samples"
while i < num_samples:
  change = time.time() - prev_time
  print str(change)
  if change >= interval:
    print "Reading sample " + str(i)
    values[i] = mcp.read_adc(channel)
    accumulated = accumulated + (values[i]-adc_zero)*(values[i]-adc_zero)
    i = i + 1
    prev_time += interval
avg = accumulated / num_samples
current = math.sqrt(avg)
amps = current / (185 / 4.89)
print "Current reading of " + str(amps) + " amps (" + str(current) + ")"