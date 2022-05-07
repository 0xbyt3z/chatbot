from PySide2.QtCore import *
from PySide2.QtWidgets import *

from PySide2.QtGui import QIcon
from requests import Session

import restfulChat

#store the states of the program
states = {
    "isregistered":False,
}

name = 'chamara' # Enter your name here!
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
window.setGeometry(300, 300, 700, 900)
window.show()

def display_bot_response(response):
    text_area.append(f"Bot : {response}")

def validate_response(response):
    response, tag = response

    if(tag == "greetings"):
        pass
    if(tag == "registration"):
        if(not states["isregistered"]):
            #request user information
            display_bot_response(response)
            states["isregistered"] = True
        else:
            display_bot_response("You are already registered")
    else:
        display_bot_response(response)

def get_bot_reponse():
    response = restfulChat.Bot(message.text())
    validate_response(response)

# Event handlers:
def display_new_messages():

    #display the user text
    new_message = "You : " + message.text()
    if new_message:
        text_area.append(new_message)

        
    get_bot_reponse()
    message.clear()


# Fire a Enter event
message.returnPressed.connect(display_new_messages)

app.exec_()
