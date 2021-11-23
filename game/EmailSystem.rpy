init:
    image emailbackground = "images/Backgrounds/email_bg.png"
    $ inbox_mail = []
    $ conversations = [] ## Conversations are held in here, for refrence, arrays start at 0 rather than 1.
    $ email_options = {} ## This is a dictionary
    $ current_conversation = None
    $ NewEmail = False

style emailframe1:
    padding gui.frame_borders.padding
    background Frame("gui/email_frame_1.PNG", gui.frame_borders, tile=gui.frame_tile)

style emailframe2:
    padding gui.frame_borders.padding
    background Frame("gui/email_frame_2.PNG", gui.frame_borders, tile=gui.frame_tile)

style emailScrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/scrollbg.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/scrollbox.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init python:
    class Mail():
        def __init__(self, sender, email, subject, label_name):
            self.sender = sender
            self.email = email
            self.subject = subject
            self.label_name = label_name

    def Add_Email(sender, email, subject, label_name):
        inbox_mail.append(Mail(sender, email, subject, label_name))
        conversations.append(Conversation())

    class Message():
        def __init__(self, sender, email, message, options, labels):
            self.sender = sender
            self.email = email
            self.message = message
            self.options = []
            self.labels = []

    class Conversation():
        def __init__(self):
            self.messages = []

        def Add_Message(self, sender, email, message, options, labels):
            if NewEmail == True:
                self.messages = []
                global NewEmail
                NewEmail = False
            for i in self.messages:
                if i.sender == sender and i.email == email and i.message == message:
                    return
            self.messages.append(Message(sender, email, message, options, labels))
            renpy.pause(7)
            renpy.restart_interaction()

screen Inbox():
    frame:
        style "emailframe2"
        xalign 0.95
        yalign 0.3
        xsize 500
        ysize 800
        vbox:
            side "c r":
                area (5,0,800,5000)
                viewport id "Inbox_list":
                    mousewheel True
                    vbox:
                        for i in inbox_mail:
                            frame:
                                style "emailframe1"
                                xsize 440
                                xoffset 12
                                yoffset 18
                                ypadding 12
                                vbox:
                                    text i.subject:
                                        xoffset 12
                                    text i.sender + " " + i.email:
                                        xoffset 12
                                    textbutton "Open" action [SetVariable("current_conversation", conversations[inbox_mail.index(i)]), Jump(i.label_name)]:
                                        xoffset 12
                vbar value YScrollValue("Inbox_list"):
                    xpos -5
                    style "emailScrollbar"

screen Current_Email():
    frame:
        style "emailframe2"
        xalign 0.1
        yalign 0.3
        xsize 700
        ysize 800
        vbox:
            side "c l":
                area (0,0,1000,785)
                ypos 8
                viewport id "Email_Convo":
                    mousewheel True
                    vbox:
                        for i in current_conversation.messages:
                            frame:
                                style "emailframe1"
                                xsize 640
                                xoffset 6
                                yoffset 12
                                vbox:
                                    text i.sender + " " + i.email:
                                        line_spacing 10
                                        xoffset 5
                                    text i.message:
                                        xoffset 9
                vbar value YScrollValue("Email_Convo"):
                    style "emailScrollbar"

screen EmailOptions():
    frame:
        xalign 0.12
        yalign 0.83
        xsize 645
        ysize 250
        vbox:
            spacing 12
            for key, value in email_options.items():
                frame:
                    xsize 600
                    xoffset 15
                    yoffset 50
                    textbutton "[key]":
                        properties gui.button_text_properties("choice_button")
                        action [Jump(value), Hide("EmailOptions")]
