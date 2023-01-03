import os
import yaml

def load_inputs(file: str = '.yaml') -> dict:
    PARAMS_YAML = file
    if os.path.isfile(PARAMS_YAML):
        with open(PARAMS_YAML, 'r') as f:
            try:
                inputs = yaml.safe_load(f)
            except yaml.YAMLError as e:
                raise Exception(e)
    else:
        raise Exception('No input yaml found.')
    return inputs