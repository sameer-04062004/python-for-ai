"""
Using packages
Python packages add new functionality to your programs. There are two types:
Built-in: Come with Python (no installation needed)
External: Need to install first with pip
​

Understanding the terminology
Let’s clarify what these terms mean:
Module: A single Python file (like math.py)
Package: A folder containing multiple modules
Function: A reusable block of code (like print() or sqrt())
Class: A blueprint for creating objects (we’ll cover this later)

Think of it like this:
A module is like a toolbox
A package is like a garage with multiple toolboxes
A function is like a specific tool (hammer, screwdriver)
A class is like a blueprint for building tools

"""

# Pattern 1: Import the whole module
import math
# Now use: math.sqrt(16)

math.sqrt(16)

# Pattern 2: Import specific items from a module
from math import sqrt, pi
# Now use: sqrt(16)

sqrt(36)

# import math - brings in the entire math toolbox
# from math import sqrt - takes just the sqrt tool from the math toolbox

# Import entire module
import random

# Use module functions
number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])

# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2026-10-24

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)

# Import entire module
import math
result = math.sqrt(16)

# Import specific functions
from math import sqrt, pi
result = sqrt(16)
circle_area = pi * radius ** 2

# Import with alias
import pandas as pd
df = pd.DataFrame(data)

# Import everything (avoid this!)
from math import *


#--------------------#### Installing pakeges #####----------------------
"""
# Install a package
pip install requests

# Install specific version
pip install requests==2.28.0

# Install multiple packages
pip install pandas numpy matplotlib

Always ensure your virtual environment is activated before installing! 
This is the #1 source of import errors. If you get “ModuleNotFoundError” 
after installing, you probably installed to the wrong environment.

"""

#------------------------#### Requirement.txt #####---------------------
"""
# Sharing your project: requirements.txt
When you share your Python project, 
others need to know which packages to install. 
The standard way is using a requirements.txt file:


# Creating requirements.txt
List all your project’s packages:
pip freeze > requirements.txt

This creates a file like:
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.0


# Installing from requirements.txt
When someone gets your project, they run:
pip install -r requirements.txt

"""
