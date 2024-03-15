#from scene.model_utils import *
from scene.models_elements import *
from scene.model_skybox import *
import glm

class Scene:
    def __init__(self, window):
        self.window = window
        self.objects = []
        self.load()
        self.skybox = SkyBox(window)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        window = self.window
        add = self.add_object

        # Cube qui rotate
        self.moving_cube = RotationCube(window, pos=(10, 10, 10), scale=(3, 3, 3), tex_id=1)
        add(self.moving_cube)

        # Pour crééer le sol, pour visualiser les ombres, on créé un "sol" de cubes
        n, s = 40, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(window, pos=(x, -s, z)))

                
        add(Cabane(window, pos=(0, -3, -10)))
        add(Cat(window, pos=(20, -1, 0)))

    def update(self):
        self.moving_cube.rot.xyz = self.window.time