from PySide2.QtCore import *
from PySide2.QtWidgets import *

from PySide2.QtGui import QIcon,QColor
from requests import Session

import nltk

import sys

import restfulChat
import botSql 


#store the state of the program
states = {
    "tag":"",
    "isregistered":False,
    "issubmitting":False,
    "user" : {"name":"","age":0,"tel":"","qual":"","course":""}
}

name = 'You' # Enter your name here!
server = Session()

# GUI:
app = QApplication([])
text_area = QTextEdit()
text_area.setFocusPolicy(Qt.NoFocus)
message = QLineEdit()
layout = QVBoxLayout()
layout.addWidget(text_area)
layout.addWidget(message)
window = QWidget()
window.setLayout(layout)
window.setWindowTitle("Chat Bot")
window.setWindowIcon(QIcon("logo.png"))
window.setGeometry(300, 100, 500, 700)
window.show()


def display_bot_response(msg):
    text_area.append(f"Bot :\n{msg}\n")

def validate_response(response):
    response, tag = response
    states["tag"] = tag
    if(tag == "greeting"):
        display_bot_response(response)
    elif(tag == "plan"):
        display_bot_response(response)
    elif(tag == "registration"):
        if(not states["isregistered"]):
            #request user information
            states["issubmitting"]  =True
            states["isregistered"] = True
            display_bot_response("Please enter your name")
        else:
            display_bot_response("You are already registered")
    else:
        display_bot_response(response)
    
    print(states)


def get_bot_reponse(msg):
    response = restfulChat.Bot(msg)
    validate_response(response)
    
 

# Event handlers:
def get_new_messages():
    if(message.text() == "quit"):
        sys.exit(0)
    else:
        
        if(states['issubmitting']):
            if(states["tag"] == "registration"):
                if(states["user"]["name"] == ""):
                    states["user"]["name"] = message.text()
                    display_bot_response("Please enter your age")
                elif(states["user"]["age"] == 0):
                    states["user"]["age"] = int(message.text())
                    display_bot_response("Please enter your contact number")
                elif(states["user"]["tel"] == ""):
                    states["user"]["tel"] = message.text()
                    display_bot_response("What is your highest qualification?")
                elif(states["user"]["qual"] == ""):
                    states["user"]["qual"] = message.text()
                    display_bot_response("What course do you expect to join?")
                elif(states["user"]["course"] == ""):
                    states["user"]["course"] = message.text()

                    states["issubmitting"] = False
                    name,age,tel,qual,course = states['user'].values()
                    id = botSql.registration(name, age,tel,qual,course)
                    display_bot_response(f"Your registration number is {id}")
                    
        else:
            text_area.append(f"You :\n{message.text()}\n")
            get_bot_reponse(message.text())
    
    message.clear()

    #display the user text
    '''
    new_message = message.text()
    if new_message:
        text_area.append("You : "+new_message)

        
    if(message.text() == "quit"):
        sys.exit(0)
    else:
        get_bot_reponse()
    message.clear()
    '''


# Fire a Enter event
message.returnPressed.connect(get_new_messages)

app.exec_()
