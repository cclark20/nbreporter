import os
import shutil
from pathlib import Path
PARAMS_YAML = '.yaml'

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