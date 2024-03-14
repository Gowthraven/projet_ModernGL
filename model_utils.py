import numpy as np

class Triangle: 
    def __init__(self, engine):
        self.engine = engine
        self.contexte = engine.contexte 
        self.shader_program = self.get_shader_program('triangle')
        self.vbo = self.create_vbo()
        self.vao = self.create_vao()
        self.on_init()

    def on_init(self):
        self.shader_program['m_projection'].write(self.engine.camera.m_projection)
        
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

