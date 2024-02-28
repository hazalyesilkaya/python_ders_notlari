users = list()


def main():
    print("### MY COMPANY ###")
    print("1. Kaydol/Register")
    print("2.Login")
    print("-" * 10)
    choose = int(input("Choose Action: "))

    if choose == 1:
        register()
    elif choose == 2:
        login()


def register():
    username = input("Username: ")
    password = input("Pasword: ")
    user = {"username": username, "password": password}
    users.append(user)
    print("Successful")
    main()


def login():
    is_user = False
    username = input("Username: ")
    password = input("Pasword: ")
    for user in users:
        if (user["username"] == username) and (user["password"] == password):
            print("Successful")
            is_user = True
            break
        if not is_user:
            print("login Unsuccessful")
    main()


main()
