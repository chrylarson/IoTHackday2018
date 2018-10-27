#!/usr/bin/python

from guizero import App, Text, TextBox, PushButton, Slider, Picture

app = App(title="Hello world", width=960, height=420)

welcome_message = Text(app, text="Welcome to the Mobile Nurse App")
my_name = TextBox(app)

def say_my_name():
    welcome_message.value = my_name.value

update_text = PushButton(app, command=say_my_name, text="Display my name")

def change_text_size(slider_value):
    welcome_message.size = slider_value

text_size = Slider(app, command=change_text_size, start=10, end=80)

my_map = Picture(app, image="map.png", width=900, height=350)

app.display()