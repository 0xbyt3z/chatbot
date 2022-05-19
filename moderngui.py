from PySide2.QtCore import *
from PySide2.QtWidgets import *

from PySide2.QtGui import QIcon,QColor
from requests import Session

import nltk

import sys

import restfulChat
import botSql 


#store the states of the program
states = {
    "tag":"",
    "isregistered":False,
    "issubmitting":False,
    "user" : {"name":"","age":0,"tel":""}
}

name = 'chamara' # Enter your name here!
server = Session()

app = QApplication([])
window =  QWidget()
container = QVBoxLayout()
message = QLineEdit()
layout = QVBoxLayout()
layout.addWidget(container)
layout.addWidget(message)
window = QWidget()
window.setLayout(layout)
window.setWindowTitle("Chat Bot")
window.setWindowIcon(QIcon("logo.png"))
window.setGeometry(300, 100, 500, 700)
window.show()
# GUI:
'''
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
'''

def display_bot_response(msg):
    button1 =  QPushButton(f"Bot : {msg}")
    layout.addWidget(button1)
    #text_area.append(f"Bot : {msg}")

def validate_response(response):
    response, tag = response
    states["tag"] = tag
    if(tag == "greetings"):
        pass
    if(tag == "registration"):
        if(not states["isregistered"]):
            #request user information
            display_bot_response(response)
            states["issubmitting"]  =True
            states["isregistered"] = True
            display_bot_response("Please enter your name")
        else:
            display_bot_response("You are already registered")
    else:
        text_area.append(f"Bot : {response}")
    
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
                    states["issubmitting"] = False
                    name,age,tel = states['user'].values()
                    id = botSql.registration(name, age, tel)
                    display_bot_response(f"Your registration number is {id}")
                    
        else:
            button1 =  QPushButton(f"You : {message.text()}")
            layout.addWidget(button1)
            #text_area.append(f"You : {message.text()}")
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
