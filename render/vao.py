from .vbo import VBO
from .shaders import Shader

class VAO:
    def __init__(self, contexte):
        self.contexte = contexte
        self.vbo = VBO(contexte)
        self.program = Shader(contexte)
        self.vaos = {}

        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['base'],
            vbo = self.vbo.vbos['cube'])
        self.vaos['shadow_cube'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['cube'])
        
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox'])

        self.vaos['cat'] = self.get_vao(
            program=self.program.programs['base'],
            vbo=self.vbo.vbos['cat'])
        self.vaos['shadow_cat'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['cat'])
        
        self.vaos['cabane'] = self.get_vao(
            program=self.program.programs['base'],
            vbo=self.vbo.vbos['cabane'])
        self.vaos['shadow_cabane'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['cabane'])


    def get_vao(self, program, vbo):
        vao = self.contexte.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()