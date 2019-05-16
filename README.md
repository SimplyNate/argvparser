# argvparser
Parses arguments passed to Python script to a dictionary.

## Instructions  
  
1.  Download the argvparser.py file and import it into your script (or integrate the function into your file)  
2.  Create a variable holding a list of acceptable switches
3.  Call the function with `argv`, Step 2 variable  
  
## Example  
```python
import argvparse
import sys

acceptable = ["-s", "-d", "-a", "-f"]
args = argvparse.check_switches(sys.argv, acceptable, "/")
print(args)
```
