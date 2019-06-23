#!/usr/bin/env python3

from glob import glob
from jinja2 import Template
import re
import yaml

# Get All data
can_data = []
frames = []
for raw_file in glob('messages/*.yaml'):
    with open(raw_file, 'r') as content:
        try:
            data = yaml.safe_load(content)
        except yaml.YAMLError as error:
            print(error)
            continue

        # Checks
        if not 'id' in data or not data['id']:
            print('ERROR: No id in {}'.format(raw_file))
            continue
        if not 'bits' in data or not data['bits']:
            print('ERROR: No bits in {}'.format(raw_file))
            continue
        if not 'length' in data or not data['length']:
            print('ERROR: No length in {}'.format(raw_file))
            continue
        print('Doing {:03X}'.format(data.get('id')))
        frames.append('{:03X}'.format(data.get('id')))

        # Create frame data for the template
        frame_data = {}
        frame_data['id'] = data.get('id')
        frame_data['length'] = data.get('length')
        frame_data['period'] = data.get('period', 'Not periodic')
        frame_data['source'] = data.get('source', 'Unknown')
        frame_data['network'] = data.get('network', 'Unknown')
        frame_data['comment'] = data.get('comment')

        # Create frame bit data for the template
        bit_chars = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
        bit_char = 0
        bit_offset = 0
        bits = []
        for bit_name, bit_data in data.get('bits', {}).items():
            bit_def = {}
            if '?' in bit_name:
                bit_def['partial'] = True

            if '-' in bit_name:
                bit_def['multiple'] = True
                bit_def['start'] = int(bit_name.split('-')[0])
                bit_def['end'] = int(bit_name.split('-')[1])
                bit_def['length'] = int(bit_def['end'])-int(bit_def['start'])
            else:
                bit_def['position'] = int(bit_name.replace('?', ''))
                bit_def['length'] = 1

            if bit_data == 'Unused':
                bit_def['unused'] = True

            bit_def['offset'] = bit_offset
            bit_def['char'] = bit_chars[bit_char]
            bit_def['comment'] = bit_data
            bit_char += 1
            if len(bit_data.split('\n')) == 1:
                bit_offset += 1
            else:
                bit_offset += len(bit_data.split('\n'))-1
            bits.append(bit_def)
        frame_data['bits'] = bits

        # Calculate status
        total_bits = 0
        for bit_name, bit_data in data.get('bits', {}).items():
            # Ignore partial bits
            if '?' in bit_name:
                continue
            if '-' in bit_name:
                total_bits = int(bit_name.split('-')[1])-int(bit_name.split('-')[0])+1
            else:
                total_bits += 1
        frame_data['percentage'] = 100 * float(total_bits) / (data.get('length', 8)*8)
        if frame_data['percentage'] == 100.0:
            frame_data['status'] = 'FRE'
        elif frame_data['percentage'] == 0.0:
            frame_data['status'] = 'NRE'
        else:
            frame_data['status'] = 'PRE'

        # Create frame tables for the template
        tables_data = []
        for table_name, table_data in data.get('data', {}).items():
            # Each data table
            table_headers = []
            for row in table_data:
                for table, val in row.items():
                    if not table in table_headers:
                        table_headers.append(table)
            tables_data.append({'name': table_name, 'headers': table_headers, 'data': table_data})
        frame_data['data'] = tables_data

        can_data.append(frame_data)

with open('index.tpl.html', 'r') as source:
    final = Template(source.read()).render(can_data=can_data, frames=frames)
    with open('index.html', 'w') as dest:
        dest.write(final)
