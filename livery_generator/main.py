import sys
import os
import argparse
from livery_generator import generate_b78xh_livery
from multi import generate_liveries

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Usage: --clone single --dir <livery directory>')
        print('       --clone multi --dir <liveries directory>')
        sys.exit(1)

    parser = argparse.ArgumentParser(
        prog='Heavy Division | B78XH Livery Generator',
        description='Generate B78XH compatible liveries from the defaults',
        epilog='written by: nakajimayoshi')

    parser.add_argument('--clone', type=str, default='single', help='single for 1 livery, multi for multiple liveries')
    parser.add_argument('--dir', type=str, help='path to livery directory')



    args = parser.parse_args()
    if not os.path.exists(args.dir):
        print(f'The source directory "{args.dir}" does not exist.')
        sys.exit(1)

    if args.clone == 'single':
        generate_b78xh_livery(args.dir)
    elif args.clone == 'multi':
        generate_liveries(args.dir)
    else:
        print("Invalid argument value for --clone. --clone single for single liveries, --clone multi for multiple")
