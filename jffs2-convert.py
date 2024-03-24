#!/usr/bin/python
import re

output_file = 'jffs2_cfg2.img'

binary_data = b''
hex_pattern = re.compile(r'[0-9a-fA-F]{8}')

with open("jffs2_raw.dump", "r") as file:
    for line in file:
        # Check if the line contains "RTL838x# md", if so, skip
        if "RTL838x# md" in line:
            continue
        
        # Find the index of ":" to locate the end of the memory address
        address_end = line.find(":")
        if address_end == -1:
            continue
        
        # Skip any lines that are too short to contain data
        if len(line) < 45:
            continue
            
        # Extract the part of the line after the memory address
        hex_data = line[address_end+1:]
        
        # Extract hexadecimal numbers from the line
        hex_values = re.findall(hex_pattern, hex_data)
        
        # Convert to binary and concatenate
        for hex_value in hex_values:
            binary_data += bytes.fromhex(hex_value)
        
with open(output_file, 'wb') as file:
    file.write(binary_data)
