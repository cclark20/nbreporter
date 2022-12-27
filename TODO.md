# v1.0.0 mvp
* [x] parse input yaml in template
* [ ] loop through all available yamls to generate multiple reports
    * inputs:
        * path to notebook template
        * path to folder with yamls
            * if `-a`, custom input is dir.
            * if not `-a`, custom input is file path to yaml.
        * path to output locations (currently hard coded)

# Future stuff
* [ ] use subprocess instead of `os.system()`