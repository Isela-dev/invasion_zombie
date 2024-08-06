print("¡Advertencia! Se ha detectado una invasión zombie en la ciudad")
print("Permanezca en interiores y siga las instrucciones de las autoridades")

nombre = "Luffy"
edad = 13
puntos_salud = 100
tiene_armas = True

print(f"Nombre: {nombre}")
print(f"Edad : {edad}")
print(f"Punto de Salud: {puntos_salud}")
print(f"Tiene armas: {tiene_armas}")

cantidad_zombies = 12

if cantidad_zombies > 5:
    print("¡Demasiados zombies! ¡Debes huir!")
else:
    print("Puedes enfrentarte a los zombies")

def calcular_dano(arma):
    if arma == "pistola":
        return 50
    elif arma == "rifle":
        return 80
    elif arma == "bate":
        return 20
    else:
        return 0
    
arma = "rifle"
dano = calcular_dano(arma)
print(f"El daño causado al zombie con {arma} es: {dano}")

zombies = [
    {"nombre" : "Zombie1", "puntos_salud": 50, "tipo_ataque": "mordida"},
    {"nombre" : "Zombie1", "puntos_salud": 70, "tipo_ataque": "arañazo"},
    {"nombre" : "Zombie1", "puntos_salud": 100, "tipo_ataque": "embestida"},
]

for zombie in zombies:
    print(f"Nombre:{zombie['nombre']}, Puntos de Salud: {zombie['puntos_salud']}, Tipo de Ataque: {zombie['tipo_ataque']}")
    
#Aimulación de supervivencia

comida = 3 #Número de comidas
municiones = 50 #Número de balas
salud = 100 #Puntos de salud

print("Comienza el día de supervivencia...")

#Encontrar comida para sobrevivir

comida += 1

print(f"Encuentras comida. Comida disponible:{comida}")

#Encuentras zombies
zombies_encuentrados = 6
if zombies_encuentrados >0;
    print(f"Encuentras {zombies_encuentrados} zombies")
    municiones -= zombies_encuentrados * 2 #Usar balas por cada zombie
    salud -= zombies_encuentrados *5 #Pierdes 5 puntos de salud por zombie
    
print(f"Municiones restantes: {municiones}")
print(f"Salud restante: {salud}")

#Final del día
if salud >0:
    print("Sobreviviste el día FELICIDADES!")
else:
    print("No sobreviviste el día")
    
#Inventario de supervivencia

inventario = []

def mostrar_inventario():
    print("Inventario de Supervivencia:")
    for item in inventario:
        print(f"-{item}")
        
def agregar_item(item):
    inventario.append(item)
        print(f"{item}agregado al inventario")
    
def quitar_item(item):
    if item.remove(item)
        print(f"{item}  quitado del inventario.")
    else:
        print(f"No se encontró {item} en el inventario")
        
        
#EJEMPLO DE USO

agregar_item("Pistola")
agregar_item("Botiquín")
mostrar_inventario()
quitar_item("Pistola")
mostrar_inventario()

