from selenium import webdriver
from time import sleep
import csv

from secret import username, password


class KajabiRename:
    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://app.kajabi.com/login")
        sleep(3)
        login_field = self.driver.find_element_by_xpath("//*[@id='user_email']")
        pass_field = self.driver.find_element_by_xpath("//*[@id='user_password']")
        login_field.send_keys(username)
        pass_field.send_keys(password)
        button = self.driver.find_element_by_xpath("//input[@type='submit']")
        button.click()
        # sleep(20)

    def update_name(self, name, user_email):
        search_url = f"https://app.kajabi.com/admin/sites/80467/contacts?search={user_email}"
        self.driver.get(search_url)
        sleep(3)
        name_link = self.driver.find_element_by_xpath("//a[@class='title']")
        name_link_a = name_link.get_attribute("href")
        edit_url = name_link_a + "/edit"
        print (edit_url)
        
        sleep(3)
        # self.driver.get("https://app.kajabi.com/admin/sites/80467/contacts")
        # sleep(3)
        # search_field = self.driver.find_element_by_xpath("//input[@type='search']")
        # search_field.send_keys(user_email)
        # search_field.submit()

        self.driver.get(edit_url)
        greeting_field = self.driver.find_element_by_xpath("//*[@id='contact_custom_20']")
        greeting_field.send_keys(name)
        button = self.driver.find_element_by_xpath("//input[@type='submit']")
        button.click()
        sleep(5)




test_driver = KajabiRename()
# test_driver.update_name("updated_name", "mohan.kst.hp@gmail.com")

with open('people.csv', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        test_driver.update_name(row[1], row[0])
