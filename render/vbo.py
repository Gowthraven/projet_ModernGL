from .vbo_utils import *
from .vbo_elements import *
from .vbo_skybox import *

class VBO:
    # Classe qui contient les VBOs, dans le GPU

    def __init__(self, contexte):
        self.vbos = {}
        self.vbos['cube'] = CubeVBO(contexte)
        self.vbos['cat'] = CatVBO(contexte)
        self.vbos['cabane']  = CabaneVBO(contexte)
        self.vbos['skybox'] = SkyBoxVBO(contexte)

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]


