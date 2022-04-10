import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#bot tries to everything

path_to_file = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(path_to_file)

driver.get("https://wwv.mp3juices.icu")

#searching for search bar
search = driver.find_element_by_name("buscar")
search.send_keys("Flo Rida - Low")
search.send_keys(Keys.RETURN)
print("Founded the song")

print("Trying to stop stupid automated  music ")
time.sleep(2)
#stoping automated music
link = driver.find_element_by_class_name("play")
link.click()
print("Thankfully it worked")

#presing download button
print("Pressing download button")
link2 = driver.find_element_by_class_name("d")
link2.click()

#closing ads that get open in new tab
print("lets close those ads")
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[-1])

#clicking_download
print("lets click that download button")
time.sleep(8)
driver.switch_to.frame(2)
time.sleep(10)
link3 = driver.find_element_by_xpath("//button[@type='b_down tbe item_ico_download descargar']")
#link3 = driver.find_element_by_class_name("bg_button")
#link3.click()


print("gonna shutdown in 3 secs")
time.sleep(3)

driver.quit()