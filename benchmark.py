#!/usr/bin/env python3

import sys
from test1 import result

MAX_N = 9
SAMPLE_FILE = 'sample3.txt'

if __name__ == '__main__':
    for i in range(1, MAX_N+1):
        out_list, root_cordi, block_list_cordi, result_string = result(f'samples/{SAMPLE_FILE}', i)
        print(result_string)
