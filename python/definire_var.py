db_username = "peter"
db_password = "123"
username = input("username:")
password = input("password")
if username == db_username and password == db_password:
    print("Corect!")
else:
    print("Incorect!")