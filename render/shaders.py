class Shader:
    def __init__(self, contexte):
        self.contexte = contexte
        self.shaders = dict()

        #self.shaders['triangle'] = self.get_shader_program('triangle')
        self.shaders['cube'] = self.get_program('cube')

    def get_program(self, shader_program_name):
        with open(f'shaders/{shader_program_name}.frag') as file: #fragment shader
            fragment_shader = file.read()
    
        with open(f'shaders/{shader_program_name}.vert') as file: #vertex shader
            vertex_shader = file.read()
            
        return self.contexte.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

    def destroy(self):
        [shader.release() for shader in self.shaders.values()]