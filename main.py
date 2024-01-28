users_details = {
  'user1': {'username': 'user1', 'password': 'pass123', 'details': 'user1 details'},
  'user2': {'username': 'user2', 'password': 'pass456', 'details': 'user2 details'},
  # ...
}

def register_user():
  new_username = input("Enter a new username: ")
  new_password = input("Enter a password for the new user: ")

  # Check if the username is already taken
  if new_username in users_details:
      print("Username already taken. Please choose a different username.")
      return

  # Add the new user to the user_details dictionary
  users_details[new_username] = {'username': new_username, 'password': new_password, 'details': f'Details for {new_username}'}
  print("User registration successful!")

def login_user():
  while True:
      username = input("Enter the username (or 'exit' to quit, 'register' to register a new user): ")

      if username.lower() == 'exit':
          print("Exiting the login program.")
          break  # Exit the loop
      elif username.lower() == 'register':
          register_user()
      elif username not in users_details:
          print("User not registered. Please try again.")
      else:
          password = input("Enter the password: ")
          if users_details[username]['password'] != password:
              print("Invalid credentials. Please try again.")
          else:
              print("Login successful!")
              print("User details:", users_details[username]['details'])

# Call the function to start the login loop
login_user()
