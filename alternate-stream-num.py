#!/usr/bin/env python3
# coding: utf8

import os
import sys


def parsing_stream(input_stream, num):
    
    names_of_files = {}
    for i in range(num):
        name_of_block = input_stream.split('.')[0] + f'-{i}.stream'
        names_of_files[i] = name_of_block
    
    i = 0
    
    with open(input_stream, 'r') as stream:
        reading_chunk = False
        
        for line in stream:
            if line.strip() == '----- Begin chunk -----':
                reading_chunk = True
                chunk = line
                i += 1

            elif line.strip() == '----- End chunk -----':
                reading_chunk = False
                chunk += line
                out = open(names_of_files[i%num],'a+')
                out.write(chunk)
                out.close()

            elif reading_chunk:
                chunk += line
            else:
                for j in range(num):
                    out = open(names_of_files[j],'a+')
                    out.write(line)
                    out.close()

    print('FINISH')



if __name__ == "__main__":
    
    input_stream = sys.argv[1]
    num = int(sys.argv[2])

    parsing_stream(input_stream, num)
    
