Pie an Python Class

DOCS: 
https://generalassemb.ly/education/pie-python/atlanta/67110?utm_campaign=cwe_confirmation&utm_content=instance_confirmation_email&utm_medium=ga_email&utm_name=instance_confirmation_email&utm_source=core_cwe

STEPS:
install Anaconda for Python 3.6 or higher
install Microsoft VsCode when prompted
launch Anaconda Navigator
add anaconda3 to your path in ~/.bashrc
export CONDA_PATH=/Users/johnsexton/anaconda3
export PATH=$M2_HOME/bin$ISTIO_HOME/bin:$CONDA_PATH/bin:$PATH

CLASS:
instructor: Mike Sanders - Pivotal Labs
full stack developer since 2006
all slides are in the PDF in the download, which I stashed into a git repo:
https://github.com/johnasexton/PieAndPython

IDE
Anaconda - Python 3.7 for this class
Atom https://atom.io 
PyCharm https://www.jetbrains.com/pycharm/download 
Sublime Text: https://www.sublimetext.com/3 
Visual Studio Code https://code.visualstudio.com/Download 

Python Interpreter
open a command shell and type ‘python3’
print(‘Hello World’)

Anaconda manages “environments” 
change upper right pane to file explorer
Launch Spyder
type:
print(‘hello world’)
<save>
<hit play button> 

Compiled vs Interpreted languages
java, .Net etc… = compiled
Python = interpreted 

Compiled
only needs to be compiled once
typically executes faster
must be redistributed whenever an update is released

Interpreted
is much more flexible
is inherently slower
must be interpreted every time it runs

both compiled and interpreted have their place, so situation dictates which is preferred

Common Applications of Python
django - web dev 
pygame - game dev toolkit
matplotlib - machine learning
scripted ops task

DEVELOPMENT COMMUNITY
PyPi = Python Package Index
site full of reusable python modules for open use

PIE AND PYTHON BASICS

COMMENTS
use comments! start everything with a comment
# this is a comment
print(‘this is a line of code’) 
comments can be used to help you debug an error

sometimes the best way to solve a problem is to break down a problem into smaller incremental steps
comments can be used for that like: 

# eat cookies 

# 1. go to the store

# 2. buy cookies

# 3. eat cookies while watching Star Wars 

VARIABLES 

used to store a value
names can start with letters or underscores and can contain numbers 
should NOT be a Python KEYWORD 
basic types are numbers, strings, and booleans 

# USE COMMUNITY PACKAGES
pip = pip installs package
# go to “Environments” tab in Anaconda
hit drop down for “not installed” 
check a box and click apply and it will pull it down for you

once a package is installed you can use it in your editor
import <package> [as <alias>]

the biggest difference between Python2 and Python3 is Python3 is fully Object Oriented
Python2 is still just a plain scripting language

# JSON and PYTHON go well together 
see my temp.py where I work through all of the intro examples in this 2 hour class



