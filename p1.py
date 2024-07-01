from turtle import position
from ursina import *
import pygame
from pydub import AudioSegment
from ursina.prefabs.first_person_controller import FirstPersonController



app = Ursina()
modelos_glb = []

def aparecer_modelo():
    # Crear una nueva instancia del modelo cada vez que se haga clic
    modelo_instancia = Entity(
        model='Emoji.glb',  # Reemplaza 'nombre_del_modelo.glb' con tu archivo .glb
        scale=(20, 20, 20),  # Escala del modelo según sea necesario
        position=(random.uniform(190, 150), random.uniform(-100, 100), random.uniform(-505, -750)),  # Posición aleatoria dentro de la habitación
        collider='mesh',
        color=color.random_color()
    )
    modelos_glb.append(modelo_instancia)  # Agregar la instancia a la lista de modelos



# Asegúrate de manejar la lógica de la aplicación Ursina y renderizar la ventana.
def update():
    pass


player = FirstPersonController(speed=150, position=(50, 0, 50), scale=20)  # Nueva posición del jugador
Sky()

def input(key):
    if key == 'escape':
        quit()

# Crear el suelo del museo
platform = Entity(model="cube", collider="box", texture="piso", scale=(3000, 1, 3000), position=(0, 0, 0))


############################################################
# Pared izquierda cuarto principal

wall_1_1 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = -350/2
wall_1_1.z = -500
wall_1_1.y = 0

wall_1_1_1= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1_1.x = -425
wall_1_1_1.z = -500
wall_1_1_1.y = 370

wall_1_11 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_11.x = 325
wall_1_11.z = -500
wall_1_11.y = 0

wall_1_111= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_111.x = 75
wall_1_111.z = -500
wall_1_111.y = 370


#--------------------cuarto1 
# #Emojis

# Añadiendo emojis y elementos interactivos
emoji_2d = Entity(
    model='quad',
    texture='happy.png',
    scale=(70, 50),
    position=(190, 80, -510),
    collider='box',
    on_click=aparecer_modelo 
)

emoji_sad = Entity(
    model='quad',
    texture='emoji_sad.jpeg',
    scale=(50, 50),
    position=(150, 50, -650),  # Ajuste de posición
    collider='box',
)
# pared izquierdo
wall_2 = Entity(
    model='cube',
    scale=(10, 500, 500),
    color=color.white,
    texture='i2.jpeg',
    texture_scale=(5, 5),  # Ajusta esta escala según la calidad de la textura
    collider='box',
    position=(495, 250, -750)
)

# pared frontal
# cubo
wall_1_1_2 = Entity(
    model='cube',
    scale=(500, 1000, 10),
    color=color.white,
    texture='i1.jpeg',
    texture_scale=(8, 12),  # Ajusta esta escala según la calidad de la textura
    collider='box'
)
wall_1_1_2.x = 250
wall_1_1_2.z = -1000  # mover a la derecha
wall_1_1_2.y = 0

# pared derecho
wall_1_1_3 = Entity(
    model='cube',
    scale=(10, 1000, 500),
    color=color.white,
    texture='i3.jpeg',
    texture_scale=(10, 10),  # Ajusta esta escala según la calidad de la textura
    collider='box'
)
wall_1_1_3.x = -5
wall_1_1_3.z = -750
wall_1_1_3.y = 0

#pared intetior1
wall_1_11 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "amarillo.jpg", collider='box')
wall_1_11.x = 325
wall_1_11.z = -505
wall_1_11.y = 0

#pared interior 2
wall_1_111= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "amarillo.jpg", collider='box')
wall_1_111.x = 75
wall_1_111.z = -505
wall_1_111.y = 370
#piso
pisos1 = Entity(model="cube", collider="box", texture="pisos1.jpg", scale=(500, 1, 500), position=(250, 1, -750))


#-------------------------cuarto 2 izquierdo Sala de Redes Sociales
# pared izquierdo
wall_1_1_3 = Entity(model='cube', scale=(10, 1000, 500), color=color.white, texture = "sala_inicio.jpg", collider='box')
wall_1_1_3.x = -15 
wall_1_1_3.z = -750
wall_1_1_3.y = 0

# pared trasera
wall_1_1_2 = Entity(model='cube', scale=(500, 1000, 10), color=color.white, texture = "sala_inicio.jpg", collider='box')
wall_1_1_2.x = -250
wall_1_1_2.z = -1000 # mover a la derecha 
wall_1_1_2.y = 0

# pared de derecho
wall_1_1_3 = Entity(model='cube', scale=(10, 1000, 500), color=color.white, texture = "sala_inicio.jpg", collider='box')
wall_1_1_3.x = -500 
wall_1_1_3.z = -750
wall_1_1_3.y = 0

#pared intetior1
wall_1_11 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "sala_inicio.jpg", collider='box')
wall_1_11.x = -175
wall_1_11.z = -505
wall_1_11.y = 370
#pared interior1_!
wall_1_1_1= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "sala_inicio.jpg", collider='box')
wall_1_1_1.x = -425
wall_1_1_1.z = -505 
wall_1_1_1.y = 370

#piso
pisos1 = Entity(model="cube", collider="box", texture="pisos1.jpg", scale=(500, 1, 500), position=(-250, 1, -750))




#---------------------------------------------------------------------------------------------------------------------------
#se tiene que cambiar habitacion 3 y 4

# Habitación 3

# lado izquierdo
wall_1_1_3 = Entity(model='cube', scale=(10, 1000, 500), color=color.white, texture = "o.png", collider='box')
wall_1_1_3.x = 1.5
wall_1_1_3.z = 750
wall_1_1_3.y = 0

# lado trasero
wall_1_1_2 = Entity(model='cube', scale=(500, 880, 100), color=color.white, texture = "i.png", collider='box')
wall_1_1_2.x = 250
wall_1_1_2.z = 1000
wall_1_1_2.y = 400


# lado derecho

wall_1_1_3 = Entity(model='cube', scale=(10, 1000, 500), color=color.white, texture = "o.png", collider='box')
wall_1_1_3.x = 500 
wall_1_1_3.z = 750
wall_1_1_3.y = 0



#pared interior1
wall_1_11 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "e.png", collider='box')
wall_1_11.x = 325
wall_1_11.z = 510
wall_1_11.y = 20

#pared inteior1_1
wall_1_111 = Entity(model='cube', scale=(155, 255, 5), color=color.white, texture = "sala_reflexion.jpg", collider='box')
wall_1_111.x = 75
wall_1_111.z = 510
wall_1_111.y = 370
#piso
pisos1 = Entity(model="cube", collider="box", texture="pisos1.jpg", scale=(500, 1, 500), position=(-250, 1, -750))


#--------------------------------------------------------
# Habitacion 4

# lado trasero

wall_1_114= Entity(model="cube",scale=(1,250,150), texture="espejo.png",collider="box",position=(-400,300,300)); wall_1_114.rotation_y = 90
wall_1_114.x = -400
wall_1_114.z = 990
wall_1_114.y = 350


wall_1_114= Entity(model="cube",scale=(1,250,120), texture="espejo_1.jpg",collider="box",position=(-400,300,300)); wall_1_114.rotation_y = 90
wall_1_114.x = -240
wall_1_114.z = 990
wall_1_114.y = 350


wall_1_114= Entity(model="cube",scale=(1,250,120), texture="espejo_3.jpg",collider="box",position=(-400,300,300)); wall_1_114.rotation_y = 90
wall_1_114.x = -100
wall_1_114.z = 990
wall_1_114.y = 350

wall_1_114= Entity(model="cube",scale=(1,200,120), texture="espejo_4.png" ,collider="box",position=(-400,300,300)); wall_1_114.rotation_y = 90
wall_1_114.x = -400
wall_1_114.z = 990
wall_1_114.y = 120  

wall_1_114= Entity(model="cube",scale=(1,200,120), texture="espejo_5.jpg",collider="box",position=(-400,300,300)); wall_1_114.rotation_y = 90
wall_1_114.x = -240
wall_1_114.z = 990
wall_1_114.y = 120

wall_1_114= Entity(model="cube",scale=(1,200,120), texture="espejo_6.jpg",collider="box",position=(-400,300,300)); wall_1_114.rotation_y = 90
wall_1_114.x = -100
wall_1_114.z = 990
wall_1_114.y = 120



#   Espejo esquina 

wall_1_114= Entity(model="cube",scale=(0,300,150), texture="e1.png",collider="box",position=(-400,300,300)); wall_1_114.rotation_y = 25
wall_1_114.x = -150
wall_1_114.z = 550
wall_1_114.y = 120

wall_1_114= Entity(model="cube",scale=(0,300,150), texture="e1.png",collider="box",position=(-400,300,300)); wall_1_114.rotation_y = 170
wall_1_114.x = -120
wall_1_114.z = 600
wall_1_114.y = 120

''


#piso
pisos1 = Entity(model="cube", collider="box", texture="pisos1.jpg", scale=(500, 1, 500), position=(-250, 1, -750))






##################################################################
# Pared derecha cuarto principal

wall_1_1 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = -350/2
wall_1_1.z = 500
wall_1_1.y = 0

wall_1_1_1= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1_1.x = -425
wall_1_1_1.z = 500
wall_1_1_1.y = 370

wall_1_11 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_11.x = 325
wall_1_11.z = 500
wall_1_11.y = 0

wall_1_111= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_111.x = 75
wall_1_111.z = 500
wall_1_111.y = 370


#--------------------------------
# Cuarto 1 y 2 izquierdo

# pared 
wall_1_1_2 = Entity(model='cube', scale=(1000, 1000, 10), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1_2.x = 0
wall_1_1_2.z = 1000 # mover a la derecha 
wall_1_1_2.y = 0


# pared de cuarto 1
wall_1_1_3 = Entity(model='cube', scale=(10, 1000, 500), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1_3.x = -500 
wall_1_1_3.z = 750
wall_1_1_3.y = 0


# pared separador cuarto 1 y 2
wall_1_1_3 = Entity(model='cube', scale=(10, 1000, 500), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1_3.x = 0 
wall_1_1_3.z = 750
wall_1_1_3.y = 0
# interior color cuartos 1 y 2 , cuartos izquierdos
wall_1_1 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1.x = -350/2
wall_1_1.z = 505
wall_1_1.y = 0

wall_1_1_1= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_1_1.x = -425
wall_1_1_1.z = 505
wall_1_1_1.y = 370

wall_1_11 = Entity(model='cube', scale=(350, 1000, 5), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_11.x = 325
wall_1_11.z = 505
wall_1_11.y = 0

wall_1_111= Entity(model='cube', scale=(150, 250, 5), color=color.white, texture = "cuartoizquierdo.jpg", collider='box')
wall_1_111.x = 75
wall_1_111.z = 505
wall_1_111.y = 370

#######################################
# Pared enfrente
wall_2 = Entity(model='cube', scale=(10, 1000, 1000), color=color.white, texture = "wall4.jpg", collider='box')
wall_2.x = -500  
wall_2.z = 0
wall_2.y = 0

# Techo del museo
ceiling = Entity(model='cube', scale=(1000, 10, 2000), color=color.white, texture = "wall4_1.jpg", collider='box')
ceiling.y = 500  
ceiling.z =0
ceiling.x = 0


# candelabros de los cuartos
cande = Entity(model="candelabro.glb", scale=(50,50,50), collider='box',position=(0,500,0))
def update():
    cande.rotation_y += 1 #Solo seria sobre su propio radio


# fachada
wall_2 = Entity(model='cube', scale=(1, 480, 400), color=color.white, texture = "MuseoFachada.jpg", collider='box',position=(505,140,0))
wall_2 = Entity(model='cube', scale=(10, 135, 400), color=color.white, texture = "wall4.jpg", collider='box',position=(505,430,0))
wall_2 = Entity(model='cube', scale=(30, 100, 300), color=color.white, texture = "nombre.jpg", collider='box',position=(524,410,0))
wall_2 = Entity(model='cube', scale=(10, 500, 805), color=color.white, texture = "wall4.jpg", collider='box',position=(505,250,595))
wall_2 = Entity(model='cube', scale=(10, 500, 805), color=color.white, texture = "wall4.jpg", collider='box',position=(505,250,-595))




app.run()
