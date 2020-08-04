import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from secret import username, passwd


'''
1. Timer
2. Refresh every 5sec
3. Alternative route
4. Notify sms
5. Set selector
'''

# open chrome
driver = webdriver.Chrome()
driver.get("https://or.ump.edu.my/or/")

# login
element = driver.find_element_by_id("login")
element.send_keys(username)
element = driver.find_element_by_id("password")
element.send_keys(passwd)
element.send_keys(Keys.RETURN)

# register
driver.find_element_by_link_text('Course Registration').click()

# select subject
subject = driver.find_element_by_id('subject')
courses = [x for x in subject.find_elements_by_tag_name("option")]

with open('subject.txt') as f:
    lines = f.readlines()
    
lines = [x.strip() for x in lines]

for line in lines:
    line = line.split(',')
    for course in courses:
        # Select course code
        if line[0] == course.get_attribute("value"):
            course.click()

            # Select section
            section_element = driver.find_element_by_id('section')
            for section in [x for x in section_element.find_elements_by_tag_name("option")]:
                if line[1] == section.get_attribute("value"):
                    section.click()
                    time.sleep(0.5)

                    # Select Lab section
                    if line[2]:          
                        lab_element = driver.find_element_by_id('tutorial')
                        for lab in [x for x in lab_element.find_elements_by_tag_name("option")]:
                            if line[2] == lab.get_attribute("value"):
                                lab.click()
                                driver.execute_script('window.scrollTo(0,3000)')
                                driver.find_element_by_id('Add').click()
   
