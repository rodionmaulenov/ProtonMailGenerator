# ProtonMailGenerator
A E-Mail Generator


## WHAT MAKES THIS BETTER

The mail is ready when the script is done. It will already be VERIFIED and NO further manual VERIFICATION needed not like at other generators

### USAGE
This realization work on Linux systems, Not fit for Windows

It is used to generate a protonmail mail for you which you can fully access

FireFox as standard browser is recommended but not must have. For chrome in scripts generator.py change snippet of code, description will be below 




## Setup project on Linux systems

### Step 1: Create a Directory

Open your terminal and create a new directory for your project:
  ```
mkdir project-name
cd project-name
```
### Step 2: Create a Virtual Environment

Set up a virtual environment to manage your Python dependencies:
```
virtualenv myenv
```
### Step 3: Activate the Virtual Environment

Activate the virtual environment:
```
source myenv/bin/activate
``` 
### Step 4: Clone the Project from GitHub

Copy the project from GitHub:
```
git clone git@github.com:rodionmaulenov/ProtonMailGenerator.git
cd ProtonMailGenerator
```
### Step 5: Create a requirements.txt File

Create a requirements.txt file with the following dependencies:
```
keyboard==0.13.5
MouseInfo==0.1.3
pillow==10.2.0
PyAutoGUI==0.9.54
PyGetWindow==0.0.9
PyMsgBox==1.0.9
pyperclip==1.8.2
PyRect==0.2.0
PyScreeze==0.1.30
python3-xlib==0.15
pytweening==1.0.7
```

### Step 6: Install Dependencies

Install the required dependencies:
```python
pip isntall -r requirements.txt
```


## Let`s launch with browser

-For FireFox simply write 'python generator.py' into command prompt

-For chrome use this row in generator.py:

pyautogui.keyDown('ctrlleft'); pyautogui.keyDown('shift'); pyautogui.typewrite('N'); pyautogui.keyUp('ctrlleft'); pyautogui.keyUp('shift')

to start working execute the same above  'python generator.py' 
