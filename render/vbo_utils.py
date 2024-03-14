import numpy as np
import moderngl as mg
import pywavefront as pwf

class InitVBO: 
    def __init__(self, contexte): 
        self.contexte = contexte
        self.vbo = self.get_vbo()
        self.format = None 
        self.attributs = None

    def get_vbo(self): 
        vertex_coord = self.get_vertex_coord()
        return self.contexte.buffer(vertex_coord)

    def destroy(self): 
        self.vbo.release()

    def get_vertex_coord(self):
        pass
    
class CubeVBO:
    def __init__(self, contexte): 
        self.contexte = contexte
        self.vbo = self.get_vbo()
        self.format = '2f 3f 3f' #2f -> texture coordinates, 3f -> normal, 3f -> position
        self.attributs = ['in_texcoord', 'in_normal', 'in_position']

    @staticmethod
    def get_data(vertices, tab_indices):
        data = [vertices[indice] for triangle in tab_indices for indice in triangle] 
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), ( 1, -1,  1), 
                    (1,  1,  1), (-1, 1,  1),
                    (-1, 1, -1), (-1, -1, -1), 
                    (1, -1, -1), ( 1, 1, -1)]

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
                             (3, 1, 2), (3, 0, 1),]
        
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