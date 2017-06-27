from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):                 # function for name,sal,age,rating
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:                # it will tell the date and time of msg and chats

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Agarwal', 'Mr.', 24, 4.7)                # Name of the existing user

friend_one = Spy('Vipul', 'Mr.', 4.7, 23)            # Friend's name that has been added
friend_two = Spy('Prince', 'Mr.', 4.65, 21)
friend_three = Spy('Simran', 'Ms.', 4.35, 24)


friends = [friend_one, friend_two, friend_three]

