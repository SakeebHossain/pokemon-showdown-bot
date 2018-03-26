from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
    
    
browser = webdriver.Chrome(executable_path=r'C:\Users\Sakeeb Home\Desktop\pokemon-showdown-bot\chromedriver_win32\chromedriver.exe')
browser.get('https://play.pokemonshowdown.com/')

username = "psbot_ash"

def wait_for_element(field, field_name, wait_time):
    WebDriverWait(browser, wait_time).until(EC.presence_of_element_located((field, field_name))) 
    
def login(username, password=None):
    
    # Click "login" button
    wait_for_element(By.NAME, 'login', 5)
    login = browser.find_element_by_name('login')  
    login.click()   
    
    # Enter username
    wait_for_element(By.NAME, 'username', 5)
    login = browser.find_element_by_name('username')
    login.send_keys(username)
    
    # Press 'Choose Name' button
    login = browser.find_element_by_xpath("//button[@type='submit']")
    login.click()   


def wait_for_battle():
    pass


def main():
    login(username)
    
    
if __name__ == '__main__':
    main()