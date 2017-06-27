from Spydetails import spy, Spy, ChatMessage, friends             #import from another folder
from steganography.steganography import Steganography             #used to hide the text image
from datetime import datetime                                        # import date and time

STATUS_MESSAGES = ['Busy', 'Learning Python', 'Dont Forget To Add Comment']        #for giving a staus


print "Hello!"                                                    #to print from starting
print "Let\'s get started"

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "         # it print the quiestion
existing = raw_input(question)


def add_status():                        # Function to add a status

    updated_status_message = None            # For Update A Status

    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)              # print status message if yes
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the existing status (y/n)? ")            # print from above status

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")           # ask to set a status msg


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))                      # check the above msg


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:                                                       # Check whether msg is updated or not
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message


def add_friend():            # Function for add a friend

    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("Please add your friend's name: ")                  # print friend's name
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")                                                    # print age
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")                                             # pring rating
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)


def select_a_friend():                       # function for selecting a frnd
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,friend.age,friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():                                         # function for send a msg using a staganography

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")                     # to  give image name
    output_path = "output.jpg"                                                        # path of the file
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


def read_message():                                             # Function for read a msg

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")                 # To read a msg of secret snd msg

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"

# function for reading chat history
def read_chat_history():                                        # Function to read a chat history

    read_for = select_a_friend()

    for chat in friends[read_for].chats:
        if (chat.sent_by_me==True):                           # it will show my message
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
            #
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def start_chat(spy):                                             # Function to start a chat

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:                                 # it will define the age category


        print "Authentication complete. Welcome " + spy.name + " age: " \ + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

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


    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")                  # if you are a new user then it will ask your intro

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid spy name'
