#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# test for python 3.4

def is_ascii(ch):
    return len(ch) == len(ch.encode())


try:
    infile = str(sys.argv[1])
    outfile = str(sys.argv[2])
except:
    print("Usage: sys.argv[0] infile outfile")
    sys.exit()


with open(outfile, "wt") as fout:
    with open(infile, "rt") as fin:
        for line in fin:
            print('line: ' + line)

            # replace '，' to ', ' for english words
            line_out = ''
            for i in range(len(line)):
                if i == 0:
                    line_out = line_out + line[i]
                    #first ch
                else:
                    #middle
                    if is_ascii(line[i-1]) and line[i] == '，':
                        line_out = line_out + ', '
                    else:
                        line_out = line_out + line[i]

            print('    : ' + line_out)

            # add space between english words and chinese words
            line = line_out
            line_out = ''
            for i in range(len(line)):
                if i + 1 == len(line):
                    line_out = line_out + line[i]
                    #last ch
                else:
                    #middle
                    if is_ascii(line[i]) and (not is_ascii(line[i+1])) and line[i] != ' ':
                        line_out = line_out + line[i] + ' '
                    elif (not is_ascii(line[i])) and is_ascii(line[i+1]) and line[i+1] != ' ' and line[i+1] != '\n' and line[i] != '，':
                        line_out = line_out + line[i] + ' '
                    else:
                        line_out = line_out + line[i]

            print('    : ' + line_out)

            # write result to file
            fout.write(line_out)

