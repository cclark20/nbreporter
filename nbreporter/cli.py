import os
import shutil
import argparse
from pathlib import Path
import warnings
from tqdm import tqdm
import pdb
PARAMS_YAML = '.yaml'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--template', type=str, required=True, help='Template file name (.ipynb).')
    parser.add_argument('--write_filename', type=str, required=False, help='Output name (.ipynb). Input yaml filename used if this arg not provided.')
    parser.add_argument('--nb_write_dir', type=str, required=False, default='notebooks/', help=' Default = notebooks/ Location of executed notebooks.')
    parser.add_argument('--input_file', type=str, required=False, help='Custom input file name (.yaml)')
    parser.add_argument('--input_dir', type=str, required=False, help='Directory with input yamls')
    parser.add_argument('--to', type=str, required=False, default='markdown', help='(Optional) Default: markdown. Output file type (those supported by nbconvert)')
    parser.add_argument('-k', '--kernel', type=str, required=False, help='(Optional) Default: python3. Name of Jupyter kernel (see available kernels by running: jupyter kernelspec list).', default='python3')
    parser.add_argument('--no_input', action='store_true', help='(Optional) Include to hide code cells in exported file.')
    args = parser.parse_args()
    # if no_input flag given, change the arg to a string for nbconvert option
    if args.no_input:
        args.no_input = '--no-input'
    else:
        args.no_input = ''
    return args

def validate_args(args) -> None:
    if not args.input_file and not args.input_dir:
        if not args.write_filename:
            raise Exception('Must provide --write-filename if no custom input yaml is specified.')
    if args.input_dir:
        if not os.path.isdir(args.input_dir):
            raise Exception(f'Could not find --input_dir {args.input_dir} or it does not exist.')
    if args.input_file:
        if not os.path.isfile(args.input_file) or not args.input_file.endswith('.yaml'):
            raise Exception(f'Could not find --input_file {args.input_file} or it does not exist.')
    if args.input_file and args.input_dir:
        raise Exception('Must choose either --input_file or --input_dir')
    if args.write_filename and args.nb_write_dir:
        warnings.warn('WARNING: --nb_write_dir is not used when --write_filename is set.')
    return None

def generate_report(args) -> None:
    TEMPLATE_FILENAME = args.template
    # set WRITE_FILENAME. Pull from yaml file name if not provided
    if args.write_filename:
        WRITE_FILENAME = args.write_filename
    else:
        yaml_name = Path(args.input_file).stem
        WRITE_FILENAME = f'{args.nb_write_dir}/{yaml_name}.ipynb'
    if args.input_file:
        shutil.copyfile(args.input_file, PARAMS_YAML)
    # create write dir if not exist
    write_dir = os.path.dirname(WRITE_FILENAME)
    if write_dir != '':
        if not os.path.exists(write_dir):
            os.makedirs(write_dir)

    # run nbconvert
    os.system(f'jupyter nbconvert --execute {TEMPLATE_FILENAME} --to notebook --ExecutePreprocessor.kernel_name={args.kernel} --output {WRITE_FILENAME} --allow-errors')
    os.system(f'jupyter nbconvert --to {args.to} {WRITE_FILENAME} {args.no_input} --output-dir ./reports')
    os.system(f'rm -rf .yaml')

def main() -> None:
    args = parse_args()
    validate_args(args)
    if args.input_dir:
        input_yamls = sorted([file for file in os.listdir(args.input_dir) if file.endswith('.yaml')])
        if len(input_yamls) == 0:
            raise Exception(f"Could not find input yamls in --input_dir {args.input_dir} or they don't exist.")
        print(input_yamls)
        for file in tqdm(input_yamls):
            args.input_file = f'{args.input_dir}/{file}'
            generate_report(args)
    else:
        generate_report(args)

    return None

if __name__ == '__main__':
    main()