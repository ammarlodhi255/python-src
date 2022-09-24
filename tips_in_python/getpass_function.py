from getpass import getpass

# Using getpass to make password invisible while the user types it out
username = input('Username: ')
password = getpass('Password: ')

print('Logging in....')
