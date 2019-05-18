# argvparser
Parses arguments passed to Python script to a dictionary. Arguments passed to switches can be called via their switch name or letter. Switches used without an argument get a boolean value `True` assigned to it in the dictionary.

## Instructions  
  
1.  Download the argvparser.py file and import it into your script (or integrate the function into your file)  
2.  Create a variable holding a list of acceptable switches
3.  Call the function with `argv`, Step 2 variable, and a delimiter of your choice for denoting switches (default "-")  
  
## Example  
```python
import argvparse
import sys

acceptable = ["-s", "-d", "-a", "-f"]
args = argvparse.check_switches(sys.argv, acceptable, "-")
print(args)
print(args["-s"])
```  
  
```cmd  
py example.py -s C:\Users\Admin -d C:\bk\ -a -f

{"-s": "C:\Users\Admin", "-d": "C:\bk\", "-a": True, "-f": True}
C:\Users\Admin
```
