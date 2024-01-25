from PIL import Image  # Not used in the visible part of the script
import pyautogui
import sys  # Not used in the visible part
import time
import random
import string
import webbrowser
import re
import pyperclip


def getClip6digit():
    clipboard_content = pyperclip.paste()
    return re.findall(r'(\d{6})', clipboard_content)[0]


def getMail():
    clipboard_content = pyperclip.paste()
    if "@dropmail.me" in clipboard_content or "@10mail.org" in clipboard_content or "@emlpro.com" in clipboard_content or "@emltmp.com" in clipboard_content:
        match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', clipboard_content)
        if match:
            return str(match.group(0))
    return False


webbrowser.open('https://google.com')
time.sleep(2)
pyautogui.keyDown('ctrlleft'); pyautogui.keyDown('shift'); pyautogui.typewrite('p'); pyautogui.keyUp('ctrlleft'); pyautogui.keyUp('shift')
time.sleep(2)
url = 'https://account.proton.me/signup?plan=free'
pyperclip.copy(url)

pyautogui.hotkey('ctrl', 'l')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(2)


def randomize(
        _option_,
        _length_
):
    if _length_ > 0:

        # Options:
        #       -p      for letters, numbers and symbols
        #       -s      for letters and numbers
        #       -l      for letters only
        #       -n      for numbers only
        #       -m      for month selection
        #       -d      for day selection
        #       -y      for year selection

        if _option_ == '-p':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
        elif _option_ == '-s':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        elif _option_ == '-l':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif _option_ == '-n':
            string._characters_ = '1234567890'
        elif _option_ == '-m':
            string._characters_ = 'JFMASOND'

        if _option_ == '-d':
            _generated_info_ = random.randint(1, 28)
        elif _option_ == '-y':
            _generated_info_ = random.randint(1950, 2000)
        else:
            _generated_info_ = ''
            for _counter_ in range(0, _length_):
                _generated_info_ = _generated_info_ + random.choice(string._characters_)

        return _generated_info_

    else:
        return 'error'


# Username
_username_ = randomize('-s', 5) + randomize('-s', 5) + randomize('-s', 5)
time.sleep(5)
pyautogui.typewrite(_username_, interval=0.1)
time.sleep(2)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
print("Username:" + _username_)

# Password
_password_ = randomize('-p', 16)
pyautogui.typewrite(_password_, interval=0.1)
time.sleep(2)
pyautogui.press('tab')
time.sleep(1)
pyautogui.typewrite(_password_, interval=0.1)
time.sleep(10)
print("Password:" + _password_)

pyautogui.typewrite('\n')
time.sleep(10)
pyautogui.typewrite('\t\t\t\n')
time.sleep(10)

url = 'https://dropmail.me/'
pyperclip.copy(url)
pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('t'); pyautogui.keyUp('ctrlleft')

time.sleep(5)
pyautogui.hotkey('ctrl', 'l')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')


pyautogui.keyDown('shift');pyautogui.keyDown('down'); pyautogui.keyUp('down'); pyautogui.keyUp('shift')
time.sleep(5)

newMail = True
while True:
    if not newMail:
        pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('r'); pyautogui.keyUp('ctrlleft')
        time.sleep(2)
    pyautogui.typewrite('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')#28
    pyautogui.keyDown('ctrlleft')
    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown('shiftright')
    pyautogui.press('down')
    pyautogui.keyUp('shiftleft')
    pyautogui.keyUp('shiftright')
    pyautogui.keyUp('ctrlleft')
    pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('c'); pyautogui.keyUp('ctrlleft')
    newMail = getMail()
    if newMail:
        print("10 min mail: " + newMail)
        break

pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
time.sleep(1)
#äpyautogui.typewrite(newMail)
pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('v'); pyautogui.keyUp('ctrlleft')
pyautogui.press('backspace')
pyautogui.typewrite('\n')

time.sleep(5)

pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
time.sleep(1)

#pyautogui.typewrite('\t\t\t\t\t\t\t\t\t\t\t\t\t\n')

#time.sleep(5)


pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('a'); pyautogui.keyUp('ctrlleft')
pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('c'); pyautogui.keyUp('ctrlleft')


pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
time.sleep(5)
pyautogui.typewrite(getClip6digit() + '\n')
print(getClip6digit())


time.sleep(5)
pyautogui.typewrite('\n')
time.sleep(5)
pyautogui.typewrite('\t\t\t\t\n')
time.sleep(1)
pyautogui.typewrite('\t\n')

print(_username_+"@proton.me:" + _password_)

logfile = open("accLog.txt", "a")
logfile.write(_username_ + "@proton.me:" + _password_ + "\n")
logfile.close()


