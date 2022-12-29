# `nbreporter`
Execute and render custom Jupyter notebook templates to new file formats given one or multiple custom inputs. Wrapper around iPython's `nbconvert` module.

## Installation
```
$ git clone https://github.com/cclark20/nbreporter.git
$ cd nbreporter/
$ pip install .
```

## Example Use Case and Objective
You are tasked with creating a Jupyter notebook template that generates identical reports for multiple, differing inputs. With this package, all you have to do is create your template notebook and your inputs as `yaml` files. The package will execute your template, with the given inputs, and generate a new notebook and whatever output format you desire (based on `nbconvert` options).

The objective was to allow for a user to easily update and modify their notebook template, without having to manually recreate notebooks for every unique input. with `nbreporter`, the template is updated and all reports can be regenerated automatically from the command line.

While it may seem that `nbconvert` already does this, the benefit is in the automtic report generation for many inputs using the same template. 

## Usage
In your notebook template, add the following code to a cell at the top, to access the input yaml.
```python
import os
import yaml
PARAMS_YAML = '.yaml'
if os.path.isfile(PARAMS_YAML):
    with open(PARAMS_YAML, 'r') as f:
        try:
            inputs = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(e)
```
Once a notebook template is generated and an input yaml file is created, the `nbreporter` module can be run, using the following command (from the command line).

### Run for one input yaml.
```
$ nbreporter --template <template notebook>.ipynb --input_file <input file>.yaml
```

Where `<template notebook>` is the name of your template and `<input file>` is the name (and location) of your input yaml. The outputted filenames will match the name of the input file.

#### Example
To run a report using the example template, follow these steps in the command line. 
```
$ cd examples/
$ nbreporter --template example_template.ipynb --input_file inputs/example.yaml
```

This will generate the following outputs in the current directory:
```
example
|___notebooks
|___|___example.ipynb
|___reports
|___|___example.md
```

### Run for multiple input yamls.
```
$ nbreporter --template <tempalte notebook>.ipynb --input_dir <input directory>
```

Where `<template notebook>` is the name of your template and `<input dir>` is the name of the directory with the input yamls. The outputted filenames will match the name of the input file.

#### Example
To run a report using the example template, follow these steps in the command line. 
```
$ cd examples/
$ nbreporter --template example_template.ipynb -input_dir inputs/
```

This will generate the following outputs in the current directory:
```
example
|___notebooks
|___|___example.ipynb
|___|___example2.ipynb
|___|___example3.ipynb
|___reports
|___|___example.md
|___|___example2.md
|___|___example3.md
```
