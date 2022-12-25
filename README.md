# `nbtemplate`
Execute and render Jupyter notebook templates to new file formats. Wrapper around iPython's `nbconvert` module.

## Installation
```
$ git clone https://github.com/cclark20/nbtemplate.git
$ cd nbtemplate/
$ pip install .
```

## Example Use Case and Objective
You are tasked with creating a Jupyter notebook template that generates identical reports for multipalte, differing inputs. With this package, all you have to do is create your template notebook and your inputs as `yaml` files. The package will execute your template, with the given inputs, and generate a new notebook and whatever output format you desire (based on `nbconvert` options).

The objective was to allow for a user to easily update and modify their notebook template, without having to recreate notebooks for every unique input. This ways the template is updated, and all reports are regenerated automatically from the command line.

## Usage

```
$ nbtemplate --template <your notebook>.ipynb --write_filename <output filename>.ipynb --custom_inputs <custom input file>.yaml
```

Where `<your notebook>` is the name of your template, `<output filename>` is the name of the output `.ipynb` (sending to subdirectory is supported), and `<custom input file>` is the name (and location) of your input yaml.

### Example
To run a report using the example template, follow these steps in the command line.

```
$ cd examples/
$ nbtemplate --template example_template.ipynb --write_filename notebooks/example.ipynb
```