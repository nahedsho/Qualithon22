# QulithonMap
A bot that solve challenges step to find the treasure 


BotQuali.py has a class called BotQuali() the has all the challenges as functions 

setup_method() : 
this function will run the setup for the browser 

myclass.intro_and_randomchallange()
this function will start the first challange it will get all buttons id and will start click it until it get to the next page

youtube_challange()
this function will play the youtube video and it suspend untill it reach the needed point and it will do the next step

crystal_maze_challange()
this function get trick part it will get js data and i will solve the maze upon it 

map_challange()
this function will foucs on the map and do move up and left and then it will click sumbit

notabot_challange()
this function will bypass the bot casue it's not a bot will just do a console command this will sumbit the page to the next challange

mongo_challenge()
this function will connect to dbmongo using pymongo and it will try to find the challage code and return the resoponse code to submitted

socketgate_challenge()
this function will connect to ws using websocket and it will send the token and the return token will be the submitted

teardown_method()
this function will terminate the browser
