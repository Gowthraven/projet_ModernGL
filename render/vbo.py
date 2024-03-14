import numpy as np
import moderngl as mg
import pywavefront as pwf

class VBO: 
    def __init__(self, contexte): 
        self.vbo = dict()
        self.vbo['cube'] = CubeVBO(contexte)
        self.vbo['triangle'] = TriangleVBO(contexte)

    def destroy(self): 
        [vbo.destroy() for vbo in self.vbo.values()]

class InitVBO: 
    def __init__(self, contexte): 
        self.contexte = contexte
        self.vbo = self.get_vbo()
        self.format = None 
        self.attributs = None

    def get_vbo(self): 
        raise NotImplementedError

    def destroy(self): 
        self.vbo.release()


