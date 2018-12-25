import os
import time
import requests


print('[NOTE] Please make sure you read "Start README" first. IT IS IMPORTANT. \n \n')

# Gets Directory of AF
Dir = os.path.split(os.getcwd())
Dir = Dir[0]
time.sleep(1.5)

# Checks for Game File Updates
# https://github.com/Cscuile/AntiFish/blob/master/AntiFish_Game_Generation


r =  requests.get('https://github.com/Cscuile/AntiFish/blob/master/AntiFish_Game_Generation')
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('td', attrs={'class':'blob-code blob-code-inner js-file-line'})

print(results)


# Concurrency Value Handle
print('What concurrency would you like to use?')
print('Concurrency allows for multiple games to be ran at once. Make sure your CPU/GPU can handle it or else you risk corrupting the games.')
print('Note: You can always test values and check your GPU/CPU usage on task manager. Default Concurrency for Non-FP16 is 1. \n')
print('Example: I (Cscuile) have an i7 7700k and 1080TI and use a concurrency value of 6 for game generation. \n')
Concurrency = input('Enter Concurrency value here (Number): ')
print('Conurrency Value Entered is', Concurrency)


# Threads = input('Test: ')
# print('Number is', Usage)


































