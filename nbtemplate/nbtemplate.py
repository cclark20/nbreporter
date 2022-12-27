import os
import sys
import shutil
import argparse
from pathlib import Path
import pdb
CONFIG_FILENAME = '.config_ipynb'
PARAMS_YAML = '.yaml'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--template', type=str, required=True, help='Template file name (.ipynb).')
    parser.add_argument('-w', '--write_filename', type=str, required=False, help='Output name (.ipynb).')
    parser.add_argument('-k', '--kernel', type=str, required=False, help='Name of Jupyter kernel (see available kernels by running: jupyter kernelspec list).', default='python3')
    parser.add_argument('-c', '--custom_inputs', type=str, required=False, help='Custom input file name (.yaml)')
    parser.add_argument('--to', type=str, required=False, default='html')
    parser.add_argument('-a', '--all', action='store_true', help='(flag) include to run for all yamls in --custom_inputs' )
    args = parser.parse_args()
    if not args.custom_inputs:
        if not args.write_filename:
            raise Exception('Must provide --write-filename if no custom input yaml is specified.')
    if args.all:
        if not os.path.isdir(args.custom_inputs):
            raise Exception('If running on multiple yamls, --custom-inputs must be a directory (not a file).')
    if not args.all:
        if args.custom_inputs:
            if not os.path.isfile(args.custom_inputs) or not args.custom_inputs.endswith('.yaml'):
                raise Exception('If running for one yaml, --custom_inputs must be a path to the input yaml.')
    return args

def main() -> None:
    args = parse_args()
    TEMPLATE_FILENAME = args.template
    if args.write_filename:
        WRITE_FILENAME = args.write_filename
    else:
        yaml_name = Path(args.custom_inputs).stem
        WRITE_FILENAME = f'notebooks/{yaml_name}.ipynb'
    # pdb.set_trace()
    if args.custom_inputs:
        shutil.copyfile(args.custom_inputs, PARAMS_YAML)

    # create write dir if not exist
    write_dir = os.path.dirname(WRITE_FILENAME)
    if not os.path.exists(write_dir):
        os.makedirs(write_dir)

    os.system(f'jupyter nbconvert --execute {TEMPLATE_FILENAME} --to notebook --ExecutePreprocessor.kernel_name={args.kernel} --output {WRITE_FILENAME} --allow-errors')
    os.system(f'jupyter nbconvert --to {args.to} {WRITE_FILENAME} --no-input --output-dir ./reports')
    os.system(f'rm -rf .yaml')

if __name__ == '__main__':
    main()