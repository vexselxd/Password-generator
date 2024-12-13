import random
while True:
    long = int(input("Escoge la longitud de la contraseña(ejem: 6)"))
    caracteres = "+-/*!&$#?=@abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(long):
        password = password + random.choice(caracteres)
    print(password)
