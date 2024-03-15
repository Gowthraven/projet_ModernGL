import numpy as np
from .vbo_utils import BaseVBO

class SkyBoxVBO(BaseVBO):
    def __init__(self, contexte):
        super().__init__(contexte)
        self.format = '3f'
        self.attribs = ['aPos']

    def get_vertex_data(self):
        # Dans le cas d'un skybox, on ne veut pas de coordonnées de texture
        # les coordonnées sont vues depuis la caméra, mais la projection est appliquée (clip space)
        z = 0.999
        vertices = [(-1, -1, z), (3, -1, z), (-1, 3, z)]
        vertex_data = np.array(vertices, dtype='f4')
        return vertex_data