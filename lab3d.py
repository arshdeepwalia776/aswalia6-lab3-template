#!/usr/bin/env python3
'''Lab 3 Inv 3 function free_space'''
# Author ID: aswalia6

import subprocess

def free_space():
    # Execute the df command and capture the output
    result = subprocess.run(['df', '-h'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    
    # Find the line that contains the root directory information
    for line in output.splitlines():
        if line.endswith('/'):
            # Split the line and return the 4th column (free space)
            return line.split()[3]

if __name__ == '__main__':
    print(free_space())

