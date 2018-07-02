pokemon_elegido =input("contra que pokemon combates? (squirtle / charmander / bulbasur): ")

vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == "squirtle":
    vida_enemigo = 90

if pokemon_elegido == "charmander":
    vida_enemigo = 80

if pokemon_elegido == "bulbasur":
    vida_enemigo = 100

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("ataque (chispazo / bola voltio)")

    if ataque_elegido == "chispazo":
        vida_enemigo -= 10
    if ataque_elegido == "bola voltio":
        vida_enemigo -= 12

    if pokemon_elegido == "squirtle":
        vida_pikachu -= 8

    if pokemon_elegido == "squirtle":
        vida_pikachu -= 8
    print("squirtle te hace un ataque de 8 de dano")

    if pokemon_elegido == "charmander":
        vida_pikachu -= 7
    print("charmander te hace un ataque de 7 de dano")

    if pokemon_elegido == "bulbasur":
        vida_pikachu -= 10
    print("bulbasur te hace un ataque de 10 de dano")

while vida_pikachu >0 and vida_enemigo > 0:
    pritn("codigo combate")

print("el combate ha terminado")