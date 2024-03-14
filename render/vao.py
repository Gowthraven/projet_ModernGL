from vbo import VBO
from shaders import Shader

class VAO: 
    def __init__(self, contexte): 
        self.contexte = contexte
        self.vbo = VBO(contexte)
        self.shader= Shader(contexte)
        self.vao = dict()

    #déclarer ici le vao pour chaque vbo
        

    #todo : déclarer le vao pour le cube 

    def get_vao(self, shader, vbo):
        return self.ctx.vertex_array(shader, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)

    def destroy(self):
        self.vbo.destroy()
        self.shader.destroy()
