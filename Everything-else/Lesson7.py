#allien_0 = {'color' : 'green', 'points' : 5}

#print(allien_0['color'])
#print(allien_0['points'])

#new_points = allien_0['points']
#print("You jus earned", new_points, "points.")

#print(allien_0)

#allien_0['x_postion'] = 0
#allien_0['y_postion'] = 50

#print(allien_0)


#allien_0 = {}

#print(allien_0)

#allien_0['color'] = 'green'
#allien_0['points'] = 5

#print(allien_0)


#allien_0 = {'color' : 'green'}

#print("The alliens color is.", allien_0['color'])

#new_color = allien_0['color'] = 'yellow'

#print("\nThe alliens new color is.", new_color)


#allien_0 = {'x_position' : 0, 'y_position' : 50, 'speed' : 'medium'}
#print("The alliens x and y position is now: \n\tX_position:", allien_0['x_position'], "\n\tY_position:", allien_0['y_position'])

#if allien_0['speed'] == 'slow':
#    allien_0['x_position'] = 10
#    allien_0['y_position'] = 60
#elif allien_0['speed'] == 'medium':
#    allien_0['x_position'] = 20
#    allien_0['y_position'] = 70
#elif allien_0['speed'] == 'fast':
#    allien_0['x_position'] = 30
#    allien_0['y_position']= 80
#else:
#    allien_0['x_position'] = 50
#    allien_0['y_position'] = 100

#ORRRRRRRRRRRRRRRRR
#if allien_0['speed'] == 'slow':
#    x_increment = 10
#    y_increment = 10
#elif allien_0['speed'] == 'medium':
#    x_increment = 20
#    y_increment = 20
#elif allien_0['speed'] == 'fast':
#    x_increment = 30
#    y_increment = 30
#else:
#    x_increment = 50
#    y_increment = 50


#allien_0['x_position'] = allien_0['x_position'] + x_increment
#allien_0['y_position'] = allien_0['y_position'] + y_increment

#print("\nThe alliens ne x and y position is:", "\n\tX_position:", allien_0['x_position'], "\n\tY_position:", allien_0['y_position'])


#fav_lang = {
#    'damir' : 'python',
#    'elea' : 'ball python',
#    'daddy' : 'ruby',
#    'mommy' : 'aws',
#    'yehor' : 'scratch'

#}

#lang = fav_lang['damir'].title()
#print('Damirs favorite language is', lang, ".")

#user_0 = {
#    'username' : 'the_iron-boy',
#    'first' : 'damir',
#    'last' : 'diedukhov'
#}

#for key, value in user_0.items():
#    print(f'\nKey : {key}'.title())
#    print(f'Value : {value}'.title())

num = int(input("ENter a number and I'll tell you if it's even or odd."))

if num % 2 == 0:
    print(f"\nThe number {num} is even.")
else:
    print(f"\nThe number {num} is odd.")