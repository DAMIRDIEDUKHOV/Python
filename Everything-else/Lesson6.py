#allien_0 = {'color': 'green', 'points': 5, 'name': 'fkaghkadlrio'} # A dictionary in Python is an unordered collection of key-value pairs, where each key is unique within the dictionary. The keys are used to index and retrieve the corresponding values. Dictionaries are defined using curly braces {} and colons : to separate keys and values.

#print(allien_0['color'])
#print(allien_0['points'])
#print(allien_0['name'])

#allien_0 = {'color': 'green', 'points': 5}

#extra_points = allien_0['points']
#print(f"You've just arened {extra_points} points")

#allien_0 = {'color': 'green', 'points': 5,}
#print(allien_0)

#allien_0['x_position'] = 25
#allien_0['y_position'] = 0

#print(allien_0)

#allien = {}

#allien['color'] = 'green'
#allien['points'] = '5'

#print(allien)


#allien = {'color': 'green'}
#print(f'The alliens color is {allien["color"]}.') 

#allien['color'] = 'yellow'
#print(f'Now the alliens color is {allien["color"]}!!!')

#allien = {'x_position': 5, 'y_position': 0, 'speed': 'slow'}
#print(f"The alliens x_position is at {allien['x_position']}")

#if allien['speed'] == 'slow':
    #speed_increment = 1
#elif allien['speed'] == 'medium':
    #speed_increment = 2
#else:
    #speed_increment = 3

#allien['x_position'] = allien['x_position'] + speed_increment

#print(f"The alliens position is now {allien['x_position']}") 

#allien = {'color': 'green', 'points': 5}
#print(allien)

#del allien['color']
#print(allien)

#favorite_video_games = {
    #'damir': 'rocket legue',
    #'yehor': 'it_takes_two',
    #'eleonora': 'call_of_duty',
    #'daddy': 'tanks_of_trouble',
    #'mommy': 'nothing'
    #}

#games = favorite_video_games['damir'].title()
#print(f"My favorite video game is {games}")


#allien = {
    #'color': 'green',
    #'speed': 'meduim'
    #}
#point_value = allien.get('points', 'no_point_value_assigned') # In Python, the .get() method is a built-in method available for dictionary objects. It allows you to retrieve the value associated with a specified key from the dictionary.
#print(point_value)

#family = {
    #'Damir': 'red',
    #'Eleonora': 'purple',
    #'Yehor': 'green',
    #'Daddy': 'blue',
    #'Mommy': 'rose',
    #'family_color': '#803F56'
#}

#color = family['family_color']
#print(f"The family color is {color},")
#print("You can find the type in google.")

#fortnite_loggin = {
    #'username': 'the_iron-boy',
    #'firstname': 'Damir',
    #'lastname': 'Diedukhov',
    #'fullname': 'Damir Diedukhov'
    #}

#for key, value in fortnite_loggin.items():
    #print(f"\nKey: {key}") # key represents the username firstname aka
    #print(f"Value: {value}") # value represents the names given to the key.



#favorite_lang = {
    #'damir': 'python',
    #'yehor': 'scratch',
    #'eleonora': 'c++',
    #'daddy': 'ruby',
    #'mommy': 'java'
#}

#for name in favorite_lang.keys(): #In Python, the .keys() method is used to retrieve a view object that contains the keys of a dictionary. 
    #print(f"{name.title()}'s favorite language is {lang.title()}.")
    #print(name.title())

#favorite_lang = {
    #'damir': 'python',
    #'yehor': 'scratch',
    #'eleonora': 'c++',
    #'daddy': 'ruby',
    #'mommy': 'java'
    #}

#friends = ['damir']
#for name in favorite_lang.keys():
    #print(f"Hi {name.title()}")

    #if name in friends:
        #language = favorite_lang[name].title()
        #print(f"\t{name.title()}, I see you love {language}.")   

favorite_lang = {
    'damir': 'python',
    'yehor': 'scratch',
    'eleonora': 'c++',
    'daddy': 'ruby',
    'mommy': 'java'
    }


for name in sorted(favorite_lang.keys()):
    print(f"{name.title()}, thank you for programming.")

if 'brother' not in favorite_lang.keys():
    print("and brother please start coding more.!!")

