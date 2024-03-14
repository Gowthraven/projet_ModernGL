import glm
import pygame as pg

#Propriétés de la caméra, voir perspective projection
FOV = 50 #en degrés, champ de vision
NEAR = 0.1
FAR = 100
SPEED = 0.005
SENSITIVITY = 0.05

class Camera: 
    def __init__(self, window, rot_y=0, rot_x=-90, position=(0,0,4), up=(0,1,0)):
        self.window = window
        self.aspect_ratio = window.WIN_SIZE[0] / window.WIN_SIZE[1]

        self.position = glm.vec3(position) #Position de la caméra
        self.up = glm.vec3(up)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)

        self.m_projection = self.get_projection_matrix()
        self.m_view = self.get_view_matrix()

        self.rot_x = rot_x #Rotation autour de l'axe x
        self.rot_y = rot_y #Rotation autour de l'axe y

    def get_projection_matrix(self): 
        """Return the projection matrix."""
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR) #glm.perspective(FOV, aspect_ratio, near, far)
    
    def get_view_matrix(self):
        """Return the view matrix."""
        return glm.lookAt(self.position, glm.vec3(0), self.up) #glm.lookAt(eye, center, up)
    
    def rotate(self):
        x_rel, y_rel = pg.mouse.get_rel()
        self.rot_x += x_rel * SENSITIVITY
        self.rot_y -= y_rel * SENSITIVITY
        self.rot_y = max(-89, min(89, self.rot_y))


    def update_camera_vectors(self):
        rot_x, rot_y = glm.radians(self.rot_x), glm.radians(self.rot_y)

        self.forward.x = glm.cos(rot_x) * glm.cos(rot_y)
        self.forward.y = glm.sin(rot_y)
        self.forward.z = glm.sin(rot_x) * glm.cos(rot_y)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

    def move(self):
        velocity = SPEED * self.window.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_z]:
            self.position += self.forward * velocity
        if keys[pg.K_s]:
            self.position -= self.forward * velocity
        if keys[pg.K_q]:
            self.position -= self.right * velocity
        if keys[pg.K_d]:
            self.position += self.right * velocity
        if keys[pg.K_SPACE]:
            self.position += self.up * velocity
        if keys[pg.K_LSHIFT]:
            self.position -= self.up * velocity
