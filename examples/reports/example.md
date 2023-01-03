```python
import nbreporter as nbr
inputs = nbr.load_inputs()
```

# Example Template Notebook


```python
print(f"Title: {inputs['title']}")
print(f"input1: {inputs['inputs']['input1']}")
print(f"input2: {inputs['inputs']['input2']}")
```

    Title: Hello World!
    input1: this is input 1
    input2: this is input 2
    
