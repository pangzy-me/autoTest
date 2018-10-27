print('--------test--------')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys("阿里巴巴")
driver.find_element_by_id('su').click()
# driver.find_element_by_id('su').submit()
driver.quit()

# # 设置时间显示
# import datetime
# timeShow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(timeShow)