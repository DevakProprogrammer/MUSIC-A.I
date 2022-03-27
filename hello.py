from re import search
import time
from webbrowser import BaseBrowser, Chrome
import webbrowser
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

def play_song(song_name):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Pdriver = webdriver.Chrome(Path)

    driver.get("https://www.youtube.com")
    print(driver.title)

    search = driver.find_element_by_xpath("/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
    search.send_keys(song_name)
    time.sleep(4)
    search.send_keys(Keys.RETURN)

    time.sleep(10)
    driver.find_element_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string").click()


r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        play_song(text)
    except:
         print("Sorry, I did not get that")