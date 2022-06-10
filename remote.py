from collections import defaultdict
import argparse


vendors_data = 'data.txt'

def parse_vendors_file(file):
    # Sample text line: 'NEW TECH 379 050 049 152 182 195'
    input_d = {}
    with open(file) as f:
        for line in f:
            key = line.split()[0]
            value = []
            for sub_str in line.split()[1:]:
                if all(char.isdigit() for char in sub_str):
                    value.append(sub_str)
                else:   
                    sub_str_idx = line.split().index(sub_str)
                    key = ' '.join(line.split()[:sub_str_idx+1])                
            input_d[key] = value
    find_matches(input_d)


'''
Sample input_d:

{
  "3M": [
    "053"
  ],
  "A.R. SYSTEMS": [
    "380",
    "049",
    "152",
    "193",
    "234"
  ],
  "ACCENT": [
    "049",
    "152",
    "195"
  ]}
'''

def find_matches(input_d):
    results_d = defaultdict(lambda: 0)

    for vendor in input_d:
        if args.your_vendor.upper() not in vendor:
            for code in input_d[args.your_vendor.upper()]:
                if code in input_d[vendor]:
                    results_d[vendor]+=1

    print(sorted(results_d, key=results_d.get, reverse=True)[:args.matches])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--your_vendor', type=str, required=True, help='Your TV vendor name')
    parser.add_argument('-m', '--matches', default=5, type=int, help='Top matches count')
    global args
    args = parser.parse_args()

    parse_vendors_file(vendors_data)


if __name__ == '__main__':
    main()