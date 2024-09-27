import random
number = int(input("Contraseña "))
guess = 0
while (guess != number):
    guess = random.randint(0,999999)
    print(guess)
print("La contraseña es "+str(number))
exit()
