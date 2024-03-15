from .vao import VAO
from .texture import Texture

class Mesh:
    def __init__(self, window):
        self.window = window
        self.vao = VAO(window.contexte)
        self.texture = Texture(window)

    def destroy(self):
        self.vao.destroy()
        self.texture.destroy()