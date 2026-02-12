from selenium import webdriver


driver = webdriver.Chrome("www.facbook.com")
driver.maximize_window()
driver.close()


driver = webdriver.Edge("www.srsdistribution.com")
driver.maximize_window()
driver.close()