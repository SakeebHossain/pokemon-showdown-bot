from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import unicodedata
import json
from pokemon import *

username = "psbot_ash"

# enable browser logging
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }

browser = webdriver.Chrome(executable_path=r'C:\Users\Sakeeb Home\Desktop\pokemon-showdown-bot\chromedriver_win32\chromedriver.exe', desired_capabilities=d)

browser.get('https://play.pokemonshowdown.com/')



def wait_for_element(field, field_name, wait_time):
    WebDriverWait(browser, wait_time).until(EC.presence_of_element_located((field, field_name))) 
    
def login(username, password=None):
    
    # Click "login" button
    wait_for_element(By.NAME, 'login', 5)
    login = browser.find_element_by_name('login')  
    login.click()   
    
    # Enter username-
    wait_for_element(By.NAME, 'username', 5)
    login = browser.find_element_by_name('username')
    login.send_keys(username)
    
    # Press 'Choose Name' button
    login = browser.find_element_by_xpath("//button[@type='submit']")
    login.click()   


def wait_for_challenge():
    
    wait_for_element(By.NAME, 'acceptChallenge', 60)
    accept_challenge_button = browser.find_element_by_name('acceptChallenge')
    accept_challenge_button.click()
    

def skip_animation():
    
    wait_for_element(By.NAME, 'goToEnd', 60)
    accept_challenge_button = browser.find_element_by_name('goToEnd')
    accept_challenge_button.click()
    

def capture_team_info():
    time.sleep(5)   # delays for 5 seconds.

    # choose the correct
    raw_team_info_string = [log for log in browser.get_log('browser') if 'baseAbility' in log['message']][0] # NOTE: this seems to fail if I challenge before the client loads
    print(raw_team_info_string)
    team_info_string = (raw_team_info_string['message'].split("request|"))[-1]
    team_info_string = team_info_string.replace("\\", "")
    team_info_string = unicodedata.normalize('NFKD', team_info_string).encode('ascii','ignore')
    team_info_string = team_info_string[:-1]  # remove that random " at the end
    team_info_string.replace('false', "False")  # not actually setting false to False... need to assign variable. but for some reason changing this screw up the json loading?!
    team_info_string.replace('true', "True")   # not actually setting false to False... need to assign variable. but for some reason changing this screw up the json loading?!
    print(team_info_string)
    return json.loads(team_info_string)

def create_team(team_info_json):
    pokemon_json = team_info_json['side']['pokemon']       
    return Team(pokemon_json)

def make_move_DUMB():
    skip_animation()
    wait_for_element(By.NAME, 'chooseMove', 60)
    accept_challenge_button = browser.find_elements_by_name('chooseMove')
    print(accept_challenge_button)
    accept_challenge_button[0].click()    
    
    
def main():
    login(username)
    wait_for_challenge()
    team_info_json = capture_team_info()
    team = create_team(team_info_json)
    team.team_summary()
    make_move_DUMB()

    
if __name__ == '__main__':
    main()