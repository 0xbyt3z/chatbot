from PySide2.QtCore import *
from PySide2.QtWidgets import *
from requests import Session

import restfulChat

name = '' # Enter your name here!
chat_url = ''
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
window.show()

def validate_response(response):
    response, tag = response
    if(tag == "greetings"):
        pass
    if(tag == "registration"):
        if(not states["isregistered"]):
            #request user information
            states["isregistered"] = True
        else:
            res.append(f"{bot_name}: You are already registered")

def botresponse():
    response = restfulChat.Bot(message.text())
    validate_response(response)

# Event handlers:
def display_new_messages():

    #display the user text
    new_message = "You : " + message.text()
    if new_message:
        text_area.append(new_message)

        
    botresponse()


# Fire a Enter event
message.returnPressed.connect(display_new_messages)


app.exec_()
