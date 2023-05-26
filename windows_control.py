# import recquired modules
import os
import pyautogui
import time
from time import sleep
from key import username,password

#prompts message on screen and gets the command 
#value of val variable
value= pyautogui.prompt("enter shell command")
#executes the commandand returns
#the output in stream variable
stream=os.popen(value)

#reads output from stream variable
out = stream.read()
pyautogui.alert(out)


def launch_browser(browser='chrome'):
    # Wait for the "Start" menu button to appear
    pyautogui.PAUSE = 1
    pyautogui.hotkey('winleft')
    pyautogui.typewrite('run')
    pyautogui.press('enter')

    #to close the current tab
    pyautogui.hotkey('ctrl+shift+w')

    # Wait for the Run dialog to appear
    time.sleep(1)

    # Type the command to launch the browser and press Enter
    pyautogui.typewrite(browser)
    pyautogui.press('enter')
    
    #to open a new window in incognito mode
    pyautogui.hotkey('ctrl+shift+n')
    
    #Reopens the last tab you've closed.
    pyautogui.hotkey('ctrl+shift+t')
    
    #to open a new tab
    pyautogui.hotkey('ctrl+t')
    
    # Wait for the browser to launch
    time.sleep(5)

    # Optional: Maximize the browser window
    # pyautogui.hotkey('winleft', 'up')

if __name__ == '__main__':
    # Call the function to launch the browser
    launch_browser()

res = pyautogui.locateOnScreen("VLC.png")
print(res)

res = pyautogui.locateCentreOnScreen("VLC.png")

pyautogui.click(res)

#open googgle chrome
pyautogui.write(['f6'])
link ="https://accounts.google.com/signin"
pyautogui.typewrite(link)
pyautogui.typewrite('/n')
print("Typing URL")

#pyautogui.keyDown('enter')
pyautogui.sleep(5)
pyautogui.typewrite(username)
pyautogui.typewrite('/n')
print("Typing Username")   
pyautogui.sleep(5)

pyautogui.typewrite(password)
pyautogui.typewrite('/n')
print("Typing Password")

#opening youtube
pyautogui.write(['f6'])
youtube = "www.youtube.com"
pyautogui.typewrite(youtube)
pyautogui.typewrite('/n')

channel_name = "code with barry"
pyautogui.write(channel_name)



#subscribe a youtube channel
'''
1. Open a new tab on the browser.
2. Search YouTube.
3 Search for the channel you want to subscribe to.
4. Click on the channel
5. Click on the Subscribe button.
'''
# a popupto take input
channel_name= pyautogui.prompt(text="Enter the Channel Name")
print(channel_name)

pyautogui.prompt(text="Enter the Channel Name")
#opens new tab
pyautogui.hotkey("ctrl","t")

#search youtube
pyautogui.write("https://www.youtube.com/")
pyautogui.hotkey("enter")
sleep(2)

#locate the search bar and click
x,y=pyautogui.locateCenterOnScreen("youtube_search.png",confidence=0.9)
pyautogui.moveTo(x,y,1)
pyautogui.click()

sleep(2)
pyautogui.write(channel_name)
pyautogui.hotkey("enter")

def logout(self):
    pyautogui.write(['f6'])
    logout = "https://accounts.google.com/logout"
    pyautogui.typewrite(logout)
    pyautogui.typewrite("/n")
    print("Logged out")
    pyautogui.sleep(5)