import numpy as np
import moderngl as mgl
import pywavefront

from .vbo_utils import BaseVBO

"""
Fichier de définition des VBOs (Vertex Buffer Objects)
Pour les modèles 3D que l'on souhaite afficher
"""

class CatVBO(BaseVBO):
    def __init__(self, window):
        super().__init__(window)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('assets/cat/12221_Cat_v1_l3.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    

class CabaneVBO(BaseVBO):
    def __init__(self, window):
        super().__init__(window)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('assets/cabane/wooden watch tower2.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    

class CubeVBO(BaseVBO):
    def __init__(self, contexte):
        super().__init__(contexte)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord', 'in_normal', 'in_position'] 

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), ( 1, -1,  1), (1,  1,  1), (-1, 1,  1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), ( 1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = self.get_data(vertices, indices)

        tex_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1)]
        tex_coord_data = self.get_data(tex_coord_vertices, tex_coord_indices)

        normals = [( 0, 0, 1) * 6,
                   ( 1, 0, 0) * 6,
                   ( 0, 0,-1) * 6,
                   (-1, 0, 0) * 6,
                   ( 0, 1, 0) * 6,
                   ( 0,-1, 0) * 6,]
        normals = np.array(normals, dtype='f4').reshape(36, 3)

        vertex_data = np.hstack([normals, vertex_data])
        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')