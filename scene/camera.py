import os
import glm
import pygame as pg


class Camera:
    def __init__(self, window, position=(0, 0, 4), rot_y=-90, rot_x=0):
        self.window = window
        self.aspect_ratio = window.WIN_SIZE[0] / window.WIN_SIZE[1]

        self.rot_y = rot_y
        self.rot_x = rot_x

        self.position = glm.vec3(position)
        self.droite = glm.vec3(1, 0, 0)
        self.haut = glm.vec3(0, 1, 0)
        self.avant = glm.vec3(0, 0, -1)

        # Matrice de projection et de vue
        self.projection = self.get_projection_matrix()
        self.view = self.get_view_matrix()

    def update_camera_vectors(self):
        rot_y, rot_x = glm.radians(self.rot_y), glm.radians(self.rot_x) # Conversion en radians
    
        self.avant.x = glm.cos(rot_y) * glm.cos(rot_x)
        self.avant.y = glm.sin(rot_x)
        self.avant.z = glm.sin(rot_y) * glm.cos(rot_x)
        self.avant = glm.normalize(self.avant)

        self.droite = glm.normalize(glm.cross(self.avant, glm.vec3(0, 1, 0)))
        self.haut = glm.normalize(glm.cross(self.droite, self.avant))

    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.rot_y += rel_x * SENSITIVITY
        self.rot_x -= rel_y * SENSITIVITY
        self.rot_x = max(-89, min(89, self.rot_x))

    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.view = self.get_view_matrix()


    def move(self):
        # Déplacement de la caméra
        vitesse = SPEED * self.window.delta_time
        keys = pg.key.get_pressed()

        if keys[pg.K_q] or keys[pg.K_LEFT]:
            self.position -= self.droite * vitesse # Gauche
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.position += self.droite * vitesse # Droite

        if keys[pg.K_z] or keys[pg.K_UP]:
            self.position += self.avant * vitesse # Avancer
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.position -= self.avant * vitesse # Reculer
        
        if keys[pg.K_SPACE]:
            self.position += self.haut * vitesse # Monter
        if keys[pg.K_LALT]:
            self.position -= self.haut * vitesse # Descendre

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.avant, self.haut)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)
    

# Configuration des paramètres de la caméra
    
def load_config(config_filepath):
    params = {}
    with open(config_filepath, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            params[key] = float(value)  
    return params

camera_script_path = os.path.dirname(os.path.abspath(__file__))
config_filepath = os.path.join(camera_script_path, 'config.txt')
params = load_config(config_filepath)

FOV = params['FOV'] # "Field of view" (angle de vue)
NEAR = params['NEAR'] 
FAR = params['FAR'] 
SPEED = params['SPEED'] # Vitesse de déplacement
SENSITIVITY = params['SENSITIVITY'] # Sensibilité de la souris
    
