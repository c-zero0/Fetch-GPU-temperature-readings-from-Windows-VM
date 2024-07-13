#!/bin/python

import json
import os
from subprocess import call

def clear_file(filename):
    with open(filename, 'w') as f:
        f.truncate(0)

file1 = "/tmp/gpu_hotspot_temperature.txt"
file2 = "/tmp/gpu_memory_junction_temperature.txt"

call('./get-temp.sh > /tmp/temps.txt', shell=True)

with open('/tmp/temps.txt', 'r') as json_file:
    data = json.load(json_file)

# Clear the contents of the output files if they exist
if os.path.exists(file1):
    clear_file(file1)

if os.path.exists(file2):
    clear_file(file2)

# Write the values to the files
with open(file1, 'w') as f1:
    f1.write(f"{data['GPU Hotspot Temperature']}")

with open(file2, 'w') as f2:
    f2.write(f"{data['GPU Memory Junction Temperature']}")
