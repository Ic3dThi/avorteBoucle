from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import random

#Program runs for this long (60s * 15) = 15 minutes
t_end = time.time() + 60*15
while time.time() < t_end:
    web = webdriver.Chrome()
    web.get('https://forms.gle/35A9Z6rCHsCz58qv7')
    # web.get('https://prolifewhistleblower.com/anonymous-form/')
    time.sleep(6)
    """
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
        """
    with open('texasZip.csv') as file1:
        reader1 = csv.reader(file1)
        location = random.choice(list(reader1))
    with open('fakeName.csv') as file2:
        reader2 = csv.reader(file2)
        fakeName1 = random.choice(list(reader2))
    with open('fakeName.csv') as file4:
        reader4 = csv.reader(file4)
        fakeName2 = random.choice(list(reader4))
    with open('vioHow.csv') as file3:
        reader3 = csv.reader(file3)
        vioHow = random.choice(list(reader3))
    vio = vioHow[0]
    vioField = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    vioField.send_keys(vio)
    how = vioHow[1]
    howField = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    howField.send_keys(how)
    clinic = "Dr. " + fakeName1[0]
    clinicField = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    clinicField.send_keys(clinic)
    cityField = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    cityField.send_keys(location[1])
    stateField = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    stateField.send_keys(location[2])
    zipField = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    zipField.send_keys(location[0])
    name = fakeName2[0]
    nameField = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    nameField.send_keys(name)
    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
    get_confirm = web.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
    if(get_confirm.text == 'Your response has been recorded.'):
        web.quit()
        continue
    else:
        break

