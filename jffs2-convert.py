#!/usr/bin/python
import re

output_file = 'jffs2_cfg.img'

loops = 0
binary_data = b''
escape_sequence_pattern = re.compile(r'\x1b[^m]*m')

def remove_escape_sequences(input_string):
	clean_string = escape_sequence_pattern.sub('', input_string)
	clean_string = clean_string.replace("[23;120H [24;1H", "")
	return clean_string
	
def remove_non_english(input_string):
	return re.sub(r'[^\x00-\x7F]+', '', input_string)



with open("jffs2_raw.dump", "r") as file:
	for line in file:
		line = remove_escape_sequences(line)
		line = line.strip()
		
		if len(line) < 45:
			continue
			
		# Remove the address portion of the response
		line = line[10:]
		
		# Remove everything except for the hex for the data
		line = line[:35]
		
		# Remove the spaces in the hex data
		line = line.replace(" ", "")
		
		# Convert to binary
		binary_data += bytes.fromhex(line)
		
		loops += 1
		print(line.strip())
		
		
		#if loops >= 50:
		#	break
			

with open(output_file, 'wb') as file:
	file.write(binary_data)
		

		
