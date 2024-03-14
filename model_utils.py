import numpy as np

class Triangle: 
    def __init__(self, window):
        self.window = window
        self.contexte = window.contexte 
        self.shader_program = self.get_shader_program('triangle')
        self.vbo = self.create_vbo()
        self.vao = self.create_vao()
        self.on_init()

    def on_init(self):
        self.shader_program['m_projection'].write(self.window.camera.m_projection)
        
    def render(self): 
        """Render the triangle."""
        self.vao.render()

    def destroy(self):
        """Destroy the triangle."""
        self.vao.release()
        self.vbo.release()
        self.shader_program.release()

    def get_vertex_coord(self): 
        """Return the vertex coordinates."""
        vertex_coord = [(-0.6, -0.8, 0.0), (0.6, -0.8, 0.0), (0.0, 0.8, 0.0)]
        return np.array(vertex_coord, dtype='f4')
    
    def create_vbo(self): 
        """Return the vertex buffer object."""
        vbo = self.contexte.buffer(self.get_vertex_coord())
        return vbo
    
    
    def get_shader_program(self, shader): 
        """Return the shader program."""
        with open(f'shaders/{shader}.vert', 'r') as file: 
            vertex_shader = file.read()

        with open(f'shaders/{shader}.frag', 'r') as file:
            fragment_shader = file.read()

        programme = self.contexte.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return programme
    
    def create_vao(self): 
        vbo= self.create_vbo()
        vao = self.contexte.vertex_array(self.shader_program, [(vbo, '3f', 'in_position')]) #3f -> Buffer format, in_position -> attributes
        return vao
    

class Cube: 
    def __init__(self, window):
        self.window = window
        self.contexte = window.contexte 
        self.shader_program = self.get_shader_program('cube')
        self.vbo = self.create_vbo()
        self.vao = self.create_vao()
        self.on_init()

    def on_init(self):
        self.shader_program['m_projection'].write(self.window.camera.m_projection)
        self.shader_program['m_view'].write(self.window.camera.m_view)
        
    def render(self): 
        """Render the triangle."""
        self.vao.render()

    def destroy(self):
        """Destroy the triangle."""
        self.vao.release()
        self.vbo.release()
        self.shader_program.release()

    def get_vertex_coord(self): 
        """Return the vertex coordinates."""
        vertex_coord = [(-1,-1, 1), (1,-1, 1),
                        (1, 1, 1), (-1, 1, 1), 
                        (-1,-1,-1), (1,-1,-1),
                        (1, 1,-1), (-1, 1,-1)]
        
        indices= [(0,2,3), (0,1,2),
                  (1,7,2), (1,6,7),
                  (6, 5, 4), (4, 7, 6), 
                  (3,4, 5), (3,5,0),
                  (3,7,4), (3,2,7), 
                  (0,6,1), (0,5,6)]
        #ordre : clockwise
        vertex_coord = self.get_data(vertex_coord, indices)
        return vertex_coord
    
    @staticmethod
    def get_data(vertex_coord, indices):
        data = []
        for triangle in indices:
            for vertex in triangle:
                data.append(vertex_coord[vertex])

        return np.array(data, dtype='f4')
    
    def create_vbo(self): 
        """Return the vertex buffer object."""
        vbo = self.contexte.buffer(self.get_vertex_coord())
        return vbo
    
    
    def get_shader_program(self, shader): 
        """Return the shader program."""
        with open(f'shaders/{shader}.vert', 'r') as file: 
            vertex_shader = file.read()

        with open(f'shaders/{shader}.frag', 'r') as file:
            fragment_shader = file.read()

        programme = self.contexte.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return programme
    
    def create_vao(self): 
        vbo= self.create_vbo()
        vao = self.contexte.vertex_array(self.shader_program, [(vbo, '3f', 'in_position')]) #3f -> Buffer format, in_position -> attributes
        return vao

