#!/usr/bin/env python3

import argparse
from tabulate import tabulate

def flag_convert(flag):
    bit_wise_flag = f'{int(flag):012b}'
    return bit_wise_flag

def sam_stats(sam_data):
    sam_flags_binary_conv = {
    0: "SUPPLEMENTARY",
    1: "DUP",
    2: "QCFAIL",
    3: "SECONDARY",
    4: "READ2",
    5: "READ1",
    6: "MREVERSE",
    7: "REVERSE",
    8: "MUNMAP",
    9: "UNMAP",
    10: "PROPER_PAIR",
    11: "PAIRED"}
    
    flags_count_dict = {
    "PAIRED": 0,
    "PROPER_PAIR": 0,
    "UNMAP": 0,
    "MUNMAP": 0,
    "REVERSE": 0,
    "MREVERSE": 0,
    "READ1": 0,
    "READ2": 0,
    "SECONDARY": 0,
    "QCFAIL": 0,
    "DUP": 0,
    "SUPPLEMENTARY": 0,
    "SINGLETONS": 0,
    "ITSELF_AND_MATE_MAPPED": 0}
    
    for entry in sam_data:
        # Skips SAM Headers
        if '@' not in entry[0]:
            
            sam_flag = entry.split("\t")[1]
            bit_flag = flag_convert(sam_flag)
            
            if bit_flag[11] == '1' and bit_flag[9] == '0':
                if bit_flag[8] == '1':
                    flags_count_dict["SINGLETONS"] += 1
                elif bit_flag[8] == '0':
                    flags_count_dict["ITSELF_AND_MATE_MAPPED"] += 1
            
            for index, flag in enumerate(bit_flag):
                if flag == '1':
                    flags_count_dict[sam_flags_binary_conv[index]] += 1
    
    data_table = tabulate(flags_count_dict.items(), headers=('FLAG','COUNT'), tablefmt='heavy_grid')
    
    return data_table

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--sam", type=str, help="SAM file.")
    args = parser.parse_args()
    
    with open(args.sam, 'r') as sam:
        sam_data = sam.readlines()
        sam.close()
    
    data_table = sam_stats(sam_data)
    print(data_table)
    
if __name__ == "__main__":
    run()