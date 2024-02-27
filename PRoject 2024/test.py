friends = {
    'John' : {
        'age' : 13,
        'sports' : ['soccer', 'basketball', 'golf']
    
    },

    'Polly' : {
        'age' : 14,
        'sports' : ['dancing', 'ice skating', 'soccer']
    }
}

action = input("1 - add new friend, 2 - del friend, 3 - change age, 4 - add new sport, 5 - del sport, 6 - show all friends, 7 - show all info, 0-stop")

while action != '0':
    if action == '7':
        print(friends)
    elif action == '1':
        name = input("Name of friend?")
        age_friend = int(input("Age of friend?"))
        sports_play = input("Enter friends favorite sports (Seperated by coma).").split(',')
        friends[name] = {
            'age' : age_friend,
            'sports' : sports_play
        }
    elif action == '2':
        delete_friend = input("What friend do you want deleted?")

        if delete_friend in friends:
            del friends[delete_friend]
        else:
            print("You don't have that friend.")
    elif action == '3':
        friend_name = input("What is you're friends name?")

        if friend_name in friends:
            new_age = int(input("What is you're friends new age?"))
            friends[friend_name]['age'] = new_age
        else:
            print("You don't have that friend.")
    elif action == '4':
        friend_name = input("What is you're friends name?")

        if friend_name in friends:
            new_sport = input("Whats new sport does you're friend play?")
            if new_sport not in friends[friend_name]['sports']:
                friends[friend_name]['sports'].append(new_sport)
            else:
                print()

    action = input("1 - add new friend, 2 - del friend, 3 - change age, 4 - add new sport, 5 - del sport, 6 - show all friends, 7 - show all info, 8-stop")




