from Spydetails import spy, Spy, ChatMessage, friends             #import from another folder
from steganography.steganography import Steganography             # import used to hide the text image
from datetime import datetime                                        # import date and time

STATUS_MESSAGES = ['Busy', 'Learning Python', 'Dont Forget To Add Comment']        # for giving a staus


print "Hello!"                                                    # to print from starting
print "Let\'s get started"
# it print the quiestion
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)

# Function to add a status
def add_status():

    # For Update A Status
    updated_status_message = None

# it check whether the current status
    if spy.current_status_message != None:

        # print current status message if yes
        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    # print from above status
    default = raw_input("Do you want to select from the existing status (y/n)? ")

    if default.upper() == "N":
        # ask to set a new status msg
        new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

        # It will ignore the uppercase if return in lower
    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        # check the above msg
        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    # Check whether msg is updated or not
    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message

 # Function for add a friend
def add_friend():

    new_friend = Spy('','',0,0.0)
    # it will print friend's name
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    # this function will ask for the age
    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    # this function will ask for the spy rating
    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        #it will give error if the user enter wrong spyrating
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)

# function for selecting a frnd
def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,friend.age,friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

# function for send a msg using a staganography
def send_message():

    friend_choice = select_a_friend()
    # it will ask to  give image name
    original_image = raw_input("What is the name of the image?")
    # path of the file
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

# function for a new chat
    new_chat ={
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
        }

    friends[friend_choice].chats.append(new_chat)
    print "Your secret message image is ready!"

# Function for read a msg
def read_message():
    sender = select_a_friend()

    # To read a msg of secret snd msg
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    print friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"

# function for reading chat history
def read_chat_history():

    read_for = select_a_friend()

    for chat in friends[read_for].chats:
        if (chat.sent_by_me==True):                           # it will show my message
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)

        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def start_chat(spy):                                             # Function to start a chat

    spy.name = spy.salutation + " " + spy.name

    # it will define the age category
    if spy.age > 12 and spy.age < 50:


        print "Authentication complete. Welcome " + spy.name + " age: "  + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            # It help to select a choice which will you want
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

if existing == "Y":
    start_chat(spy)
else:

    spy = Spy('','',0,0.0)

    # if you are a new user then it will ask your intro
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid spy name'

