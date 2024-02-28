users = list()


def main():
    print("### MY COMPANY ###")
    print("-" * 10)
    print("1.Register")
    print("2.Login")
    print("-" * 10)
    choose = int(input("Choose Action : "))

    if (choose == 1):
        register()
    elif (choose == 2):
        login()


kucukharfler = "abcdefghijkLmnopqrstuvwxyz"
buyukharfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rakamlar = "0123456789"


def is_true_password(password):
    lowercase = False
    uppercase = False
    digit = False
    is_long = len(password) >= 4
    for i in password:
        if i in kucukharfler:
            lowercase = True
        elif i in buyukharfler:
            uppercase = True
        elif i in rakamlar:
            digit = True

    return lowercase and uppercase and digit and is_long


def register():
    username = input("Username : ")
    password = input("Password : ")
    user = {"username": username, "password": password}
    if not is_true_password(password):
        print("Şifre en az 1 büyük harf bir küçük harf ve 1 sayı içermelidir.")
    else:
        users.append(user)
        print("Succesfull")


main()


def login():
    is_user = False
    username = input("Username : ")
    password = input("Password : ")
    for user in users:
        if (user["username"] == username and user["password"] == password):
            print("Succesfull")
            is_user = True
            break
    if (is_user == False):
        print("Login Failed!")
    main()


main()
print("Artık burası çalıştı!")
