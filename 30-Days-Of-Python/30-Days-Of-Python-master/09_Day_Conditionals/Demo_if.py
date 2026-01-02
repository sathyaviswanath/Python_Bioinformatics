#access the database
user = 'yogesh'
access_level = 9
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')