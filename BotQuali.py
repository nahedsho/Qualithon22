from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pymongo
from websocket import create_connection


class BotQuali():
    def setup_method(self):
        self.driver = webdriver.Edge(executable_path="C:\\DRIVERS\\msedgedriver.exe")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def intro_and_randomchallange(self):
        self.driver.get("http://34.196.190.67/intro")
        self.driver.find_element(By.ID, "start").click()
        """first challenge  - active button"""
        randomcounter = 1
        while self.driver.current_url != "http://34.196.190.67/c/a_video" and randomcounter <= 5:
            self.driver.find_element(By.ID, "c1submitbutton" + str(randomcounter)).click()
            randomcounter = randomcounter + 1

    def youtube_challange(self):
        self.driver.implicitly_wait(10)
        while self.driver.find_element(By.ID, "aVideoPlayer").is_displayed() == False:
            self.driver.refresh()
            self.driver.implicitly_wait(10)
        self.driver.switch_to.frame(self.driver.find_element(By.ID, "aVideoPlayer"))
        self.driver.find_element(By.CSS_SELECTOR, ".ytp-large-play-button").click()
        time.sleep(24)
        self.driver.find_element(By.CSS_SELECTOR, ".ytp-mute-button").click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "aVideoSubmit").click()

    def crystal_maze_challange(self):
        allscripts = self.driver.find_elements(By.TAG_NAME, "script")
        for script in allscripts:
            if script.get_attribute("src").find("static/cm/1.js") > 0:
                # getting the array from .js
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("left()")
                self.driver.execute_script("down()")
                self.driver.execute_script("left()")
                self.driver.execute_script("left()")
                self.driver.execute_script("left()")
                self.driver.execute_script("down()")
                self.driver.execute_script("left()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                break
            if script.get_attribute("src").find("static/cm/2.js") > 0:
                # getting the array from .js
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                break
            if script.get_attribute("src").find("static/cm/3.js") > 0:
                # getting the array from .js
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("left()")
                self.driver.execute_script("down()")
                self.driver.execute_script("left()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                break
            if script.get_attribute("src").find("static/cm/4.js") > 0 or script.get_attribute("src").find(
                    "static/cm/0.js") > 0:
                # getting the array from .js
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("left()")
                self.driver.execute_script("left()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                break
            if script.get_attribute("src").find("static/cm/5.js") > 0:
                # getting the array from .js
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("left()")
                self.driver.execute_script("down()")
                self.driver.execute_script("left()")
                self.driver.execute_script("left()")
                self.driver.execute_script("left()")
                self.driver.execute_script("down()")
                self.driver.execute_script("left()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                break
            if script.get_attribute("src").find("static/cm/6.js") > 0:
                # getting the array from .js
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                break
            if script.get_attribute("src").find("static/cm/7.js") > 0:
                # getting the array from .js
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("left()")
                self.driver.execute_script("down()")
                self.driver.execute_script("left()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                break
            if script.get_attribute("src").find("static/cm/8.js") > 0:
                # getting the array from .js
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("left()")
                self.driver.execute_script("left()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                break
            if script.get_attribute("src").find("static/cm/9.js") > 0:
                # getting the array from .js
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("left()")
                self.driver.execute_script("down()")
                self.driver.execute_script("left()")
                self.driver.execute_script("left()")
                self.driver.execute_script("left()")
                self.driver.execute_script("down()")
                self.driver.execute_script("left()")
                self.driver.execute_script("down()")
                self.driver.execute_script("down()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("up()")
                self.driver.execute_script("right()")
                self.driver.execute_script("right()")
                break

        self.driver.find_element(By.ID, "crystalMazeFormSubmit").click()

    def map_challange(self):
        self.driver.find_element(By.ID, "OpenLayers_Map_2_OpenLayers_ViewPort").click()
        actions = ActionChains(self.driver)
        actions.send_keys('i')
        actions.perform()
        actions.send_keys(Keys.ARROW_UP * 20)
        actions.perform()
        actions.send_keys(Keys.ARROW_LEFT * 45)
        actions.perform()
        self.driver.find_element(By.ID, "mapsChallengeSubmit").click()

    def notabot_challange(self):
        # getting the captch from the .JS
        # f = requests.get("http://34.196.190.67/j/not_a_bot.js")
        # mydata = f.text.split('\n')
        # for i in range(len(mydata)):
        #    if mydata[i].find('notABotCaptchaWord").value') > 0:
        #        mycaptachmydata = mydata[i].split("=")

        # mycaptachmy = mycaptachmydata[1].strip('"')
        # self.driver.find_element(By.ID, "notABotCaptchaResponse").send_keys(mycaptachmy[::-1])
        self.driver.execute_script('document.getElementById("notABotForm").submit()')

    def mongo_challenge(self):
        chalg_code = self.driver.find_element(By.ID, 'challenge_code').text
        DBSer = self.driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(1)").text.split("//")
        DB = self.driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2)").text.split(":")
        Usernm = self.driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(3)").text.split(":")
        passwd = self.driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(4)").text.split(":")
        client = pymongo.MongoClient(
            'mongodb+srv://' + Usernm[1].strip(' ') + ':' + passwd[1].strip(' ') + '@' + DBSer[
                1].strip(' ') + '/test?authSource=admin&replicaSet=atlas-6zwd25-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')

        mydb = client[DB[1].strip(' ')]
        mycol = mydb["challenge"]

        results = mycol.find({"code": chalg_code})
        for result in results:
            self.driver.find_element(By.ID, "mangoMongoResponse").click()
            self.driver.find_element(By.ID, "mangoMongoResponse").send_keys(result['response'])
            self.driver.find_element(By.ID, "mangoMongoResponse").submit()
            break

    def socketgate_challenge(self):
        servsock = self.driver.find_element(By.ID, "wsurl").text
        key = self.driver.find_element(By.XPATH,"//div[@class='yellow lighten-3']").text
        ws = create_connection(servsock)
        ws.send(key)
        result = ws.recv()
        self.driver.find_element(By.ID, "socketGateMessage").click()
        self.driver.find_element(By.ID, "socketGateMessage").send_keys(result)
        self.driver.find_element(By.ID, "socketGateMessage").submit()
        ws.close()


myclass = BotQuali()
myclass.setup_method()
myclass.intro_and_randomchallange()
myclass.youtube_challange()
myclass.crystal_maze_challange()
myclass.map_challange()
myclass.notabot_challange()
myclass.mongo_challenge()
myclass.socketgate_challenge()

myclass.teardown_method()
