import random 
piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijeras = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imagenes = [piedra, papel, tijeras]

usuario = int(input("¿Que eliges? Escriba 0 para Piedra, 1 para Papel o 2 para Tijeras: "))
print(imagenes[usuario])

computadora = random.randint(0,2)
print("Computadora: ")
print(imagenes[computadora])

if usuario >= 3 or usuario < 0:
    print("Tienes que escribir un numero valido, Tu Pierdes")

if usuario == 0 and computadora == 2:
    print("Tu Ganas")
elif computadora == 0 and usuario == 2:
    print("Tu pierdes")
elif computadora > usuario:
    print("Tu pierdes")
elif usuario > computadora:
    print("Tu Ganas")
elif computadora == usuario:
    print("Empate")




