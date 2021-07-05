from selenium import webdriver
from time import sleep
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

def headless_driver():       
    """
    Αυτή η συνάρτηση θέτει τον driver
    σε λειτουργία ορατού ή αόρατου παραθύρου.
    """                                              
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("--headless")
    options.add_argument("disable-gpu")
    return options

def init_driver(headless = False):                                          #από προεπιλογή False
    """
    Αυτή η συνάρτηση
    αρχικοποιεί τον driver.
    """
    option = headless_driver() if headless == True else None                  #ternary-like operator
    return Edge(executable_path="driver\msedgedriver.exe",options=option)

def login(driver, usernameText, passwordText):
    """
    Σύνδεση στον λογαριασμό
    φοιτητή στο myprotia.
    """
    usernameField = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table[5]/tbody/tr/td/table[2]/tbody/tr/td[5]/table[1]/tbody/tr[2]/td/form/table/tbody/tr/td/span[1]/input[2]")
    passwordField = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table[5]/tbody/tr/td/table[2]/tbody/tr/td[5]/table[1]/tbody/tr[2]/td/form/table/tbody/tr/td/span[1]/input[3]")
    
    usernameField.send_keys(usernameText)
    passwordField.send_keys(passwordText)

    loginButton = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table[5]/tbody/tr/td/table[2]/tbody/tr/td[5]/table[1]/tbody/tr[2]/td/form/table/tbody/tr/td/input")
    loginButton.click()

def lessonsDB(driver):
    """
    Μετάβαση στη βάση δεδομένων
    των μαθημάτων.
    """
    lessonsDB = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table[5]/tbody/tr/td/table[2]/tbody/tr/td[1]/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/span/a")
    lessonsDB.click()

def main():
    driver = init_driver(False)
    driver.get("http://www.myprotia.gr")

    sleep(1)
    login(driver, "USERNAME", "PASSWORD")
    sleep(1)
    lessonsDB(driver)

    sleep(60)

if __name__ == "__main__":
    main()