import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#bot tries to everything

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://wwv.mp3juices.icu")

#path to file for songs
list_of_songs = open("/home/tickatus/my_python_programs/song_downloader/songs", "r")
number_of_all_songs = open("/home/tickatus/my_python_programs/song_downloader/songs", "r")


all_music = list_of_songs.read().splitlines()

number_of_songs = sum(1 for line in number_of_all_songs)

counter = 0

print("I'm starting to download your stuff")

def song_download_process():
        for i in range(number_of_songs):
                global counter
                #searching for search bar
                search = driver.find_element(By.NAME, "buscar")
                search.send_keys(all_music[counter])
                search.send_keys(Keys.RETURN)

                #stopping automated music
                time.sleep(2)
                link = driver.find_element(By.CLASS_NAME, "play")
                link.click()

                #presing first download button
                link2 = driver.find_element(By.CLASS_NAME, "d")
                link2.click()

                #closing ads that get open in new tab
                driver.switch_to.window(driver.window_handles[1])
                driver.close()
                driver.switch_to.window(driver.window_handles[-1])

                #clicking second download button
                time.sleep(8)
                driver.switch_to.default_content()
                driver.switch_to.frame(1)
                driver.find_element_by_tag_name("iframe").click()

                #closing those extra ads that open after pressing second download
                driver.switch_to.window(driver.window_handles[1])
                driver.close()
                driver.switch_to.window(driver.window_handles[-1])

                #switching song
                counter = counter + 1

                #just waiting for download to start
                time.sleep(6)

song_download_process()

print("""\

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


                    """)


print("I'm going to run for more 10mins in case you have a lot of songs to download so I don't interupt any downloads")
print("When everything downloades you can just close chrome and program will shutdown")
time.sleep(600)

driver.quit()
