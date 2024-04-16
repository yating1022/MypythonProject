def main():
    defl = [false] * 5
    password = input("输入密码")
    for x in password :
        if not defl[0] and str.isdigit(x):
            defl[0] =  True
        elif not defl[1] and str.islower(x):
            defl[1] = True
        elif not defl[2] and str.isupper(x):
            defl[2] = True
        elif not defl[3] and x in '_':
            defl[3] = True
        elif not defl[4] and x in '#%^&*()':
            defl[4] = True
    print()