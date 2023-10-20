import string

def check_password(password):
    a = 0  #mała litera
    b = 0  #duża litera
    c = 0  #cyfra
    d = 0  #znak specjalny
    e = 0  #16 znaków
    listofp = list(password)
    for element in listofp:
        if element.islower() and a != 1:
            a = 1
        elif element.isupper() and b != 1:
            b = 1
        elif element.isdigit() and c != 1:
            c = 1
        elif element in string.punctuation and d != 1:
            d = 1
    if len(listofp) >= 16:
        e = 1
    if a == 1 and b == 1 and c == 1 and d == 1 and e == 1:
        return "Strong password"
    else:
        return "Weak password"

password = input("Podaj hasło: ")
results = check_password(password)
print(results)
