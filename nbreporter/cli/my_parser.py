import argparse
import warnings

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