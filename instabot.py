import requests
import json
from termcolor import colored

BASE_URL = 'https://api.instagram.com/v1/'
ACCESS_TOKEN = '4392741281.7788e8d.25fc02bdcc8d4d28bb8749bba860571e'

SANDBOX_USER = []


def start_bot():
    show_menu = True
    while show_menu:
        menu_choices =  menu_choices = "What do you want to do? " \
                                       "\n 1. Read account details" \
                                       "\n 2. Get details of an user" \
                                       "\n 3. Send a secret message " \
                                       "\n 4. Read a secret message " \
                                       "\n 5. Read Chats from a user " \
                                       "\n 6. Close Application \n"
        menu_choice = raw_input(menu_choices)
        menu_choice = int(menu_choice)

        if menu_choice == 1:
            print colored("Read details\n", 'cyan', attrs=['bold'])
            get_info()
        elif menu_choice == 2:
            print colored("Get details of user using username\n", 'cyan', attrs=['bold'])
            get_userInfo()
        #elif menu_choice == 3:
            #print colored("Send a secret message\n", 'cyan', attrs=['bold'])
            #send_message()
        #elif menu_choice == 4:
            #print colored("Read a secret message\n", 'cyan', attrs=['bold'])
            #read_message()
        #elif menu_choice == 5:
            #print colored("Read existing message\n", 'cyan', attrs=['bold'])
            #read_existing_chat()
        #elif menu_choice == 6:
            #show_menu = False



def get_info():
    select = int(raw_input("Select user for which you want info \n"
                           "1. Info of Access Token Owner\n"
                           "2. Info of other user"))
    if select ==1:
        print colored("Read own details\n", 'cyan', attrs=['bold'])
        request_url = (BASE_URL + 'users/self/?access_token=%s') % (ACCESS_TOKEN)
        user_info = requests.get(request_url).json()
        if user_info:
            with open('user_info.json', 'w') as outfile:
                json.dump(user_info, outfile)
                f1 = open('user_info.json')

            user_info = json.load(f1)
            for item in user_info:
                if item == 'data':
                    user_id = user_info['data']['id']
                    SANDBOX_USER.append(user_id)
                    return user_id


    elif select == 2:
        print colored("Get details of user using username\n", 'cyan', attrs=['bold'])
        id = get_userID()
        request_url = (BASE_URL + 'users/%s/?access_token=%s') % (id, ACCESS_TOKEN)
        user_info = requests.get(request_url).json()

    else:
        print 'Please select a valid option.'

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username:' +colored('%s', 'blue', attrs=['bold']) %(user_info['data']['username'])
            print 'Followers:' + colored('%s', 'green', attrs=['bold']) % (user_info['data']['counts']['followed_by'])
            print 'Following:' + colored('%s', 'red', attrs=['bold']) % (user_info['data']['counts']['follows'])
            print 'Posts:' + colored('%s', 'yellow', attrs=['bold']) % (user_info['data']['counts']['media'])

        else:
            print colored('User has no data','red',attrs=['bold'])
    else:
        print colored('Data not found', 'red', attrs=['bold'])

    quest = raw_input('Do you want to continue with this user? Y/N')
    if quest.upper() == 'Y':
        select = int(raw_input("Select no. corresponding to action you want to perform \n"
                               "1. Like a post\n"
                               "2. Comment on a post\n"))



def get_userID():
    username = raw_input("Enter instagram username of person you want to search")
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') %(username,ACCESS_TOKEN)
    user_info = requests.get(request_url).json()
    if user_info:
        with open('user_info.json', 'w') as outfile:
            json.dump(user_info, outfile)
            f1 = open('user_info.json')

        user_info = json.load(f1)
        for item in user_info:
            if item == 'data':
                user_id = user_info['data'][0]['id']
                SANDBOX_USER.append(user_id)
                return user_id
        else:
            print colored('Add user to sandbox','red',attrs=['bold'])




start_bot()
