import os
import sys
import shutil
import argparse
CONFIG_FILENAME = '.config_ipynb'
PARAMS_YAML = '.yaml'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--template', type=str, required=True, help='Template file name (.ipynb).')
    parser.add_argument('-w', '--write_filename', type=str, required=True, help='Output name (.ipynb).')
    parser.add_argument('-k', '--kernel', type=str, required=False, help='Name of Jupyter kernel (see available kernels by running: jupyter kernelspec list).', default='python3')
    parser.add_argument('-c', '--custom_inputs', type=str, required=False, help='Custom input file name (.yaml)')
    parser.add_argument('--to', type=str, required=False, default='html')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    argv = sys.argv
    TEMPLATE_FILENAME = args.template
    WRITE_FILENAME = args.write_filename
    with open(CONFIG_FILENAME, 'w') as f:
        f.write(' '.join(argv))
    if args.custom_inputs:
        shutil.copyfile(args.custom_inputs, PARAMS_YAML)

    # create write dir if not exist
    write_dir = os.path.dirname(WRITE_FILENAME)
    if not os.path.exists(write_dir):
        os.makedirs(write_dir)

    os.system(f'jupyter nbconvert --execute {TEMPLATE_FILENAME} --to notebook --ExecutePreprocessor.kernel_name={args.kernel} --output {WRITE_FILENAME}')
    os.system(f'jupyter nbconvert --to {args.to} {WRITE_FILENAME} --no-input --output-dir ./reports')

if __name__ == '__main__':
    main()