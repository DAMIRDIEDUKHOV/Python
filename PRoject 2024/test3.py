user_input = input("Enter a sentence with spaces: ")
words = user_input.split(' ')  # Splitting based on spaces

# Removing empty strings (resulting from consecutive spaces) and commas from the list
words = [word for word in words if word == '' or word == ',']

print("Words:", words)