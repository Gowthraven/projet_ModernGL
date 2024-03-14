import numpy as np
import moderngl as mg
import pywavefront as pwf

from .vbo_utils import CubeVBO

class VBO: 
    def __init__(self, contexte): 
        self.vbo = dict()
        self.vbo['cube'] = CubeVBO(contexte)
        # self.vbo['triangle'] = TriangleVBO(contexte)

    def destroy(self): 
        [vbo.destroy() for vbo in self.vbo.values()]
