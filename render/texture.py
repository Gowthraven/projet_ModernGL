import moderngl as mg   
import glm
import pygame as pg

class Texture: 
    def __init__(self, window): 
        self.window = window
        self.contexte= window.contexte

        self.textures= dict()

        self.textures[0] = self.get_texture('assets/textures/grass.jpg')


    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]