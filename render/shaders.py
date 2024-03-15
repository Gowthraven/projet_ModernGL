class Shader:
    def __init__(self, contexte):
        self.contexte = contexte
        self.programs = {}
        
        self.programs['base'] = self.get_program('base')
        self.programs['skybox'] = self.get_program('skybox')
        self.programs['shadow_map'] = self.get_program('shadow_map')

    def get_program(self, shader_name):
        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()

        return self.contexte.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

    def destroy(self):
        [program.release() for program in self.programs.values()]