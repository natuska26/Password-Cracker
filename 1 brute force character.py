import random
character = "0123456789abcdefghijklmnopqrstuvwxyz" #son solo caracteres en minúscula
character_list = list(character) 
password = input("Ingresá la contraseña: ")
guess = ""
while (guess !=password): #does not equal password es !=
    guess = random.choices(character_list, k=len(password))
    #print(guess)
    guess ="".join(guess)
    #print(guess)
print("La contraseña es "+ guess)
exit()
