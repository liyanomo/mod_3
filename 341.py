341.py
login = str (input("введите логин:"))
password = str (input("введите пароль:"))
def register1 ():
    register = {'login1' : admin }
    json.damp(register1)
    with open('register1', 'r') as f:
        register1=json.load(f)
    if login not in regiser.keys() :
        regiser[name] = password
        with open('register1', 'a') as f:  
            json.damp(login)
        print ('регистрация прошла успешно')
    else :
        print ("пользователь с таким логином уже существует")