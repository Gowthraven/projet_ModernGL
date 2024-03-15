import numpy as np
import moderngl as mgl
import pywavefront

"""
Fichier de définition des VBOs (Vertex Buffer Objects)
Contient la classe de base BaseVBO
"""

class BaseVBO:
    def __init__(self, contexte):
        self.contexte = contexte
        self.vbo = self.get_vbo()
        self.format: str = None # Format des données
        self.attribs: list = None # Attributs des données

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.contexte.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()


