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
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True) #flip the image
        texture = self.contexte.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB')) #convert the image to a texture
        
        # AF
        texture.anisotropy = 32.0 
        # mipmaps
        texture.filter = (mg.LINEAR_MIPMAP_LINEAR, mg.LINEAR) #minification, magnification
        texture.build_mipmaps() #génère les mipmaps

        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]

    def get_depth_texture(self):
        """Create a depth texture."""
        depth_texture = self.contexte.depth_texture(self.app.WIN_SIZE)
        depth_texture.repeat_x, depth_texture.repeat_y = False, False
        return depth_texture

    def get_texture_cube(self, dir_path, extension='png'):
        """Create a texture cube."""
        faces = ['right', 'left', 'top', 'bottom'] + ['front', 'back'][::-1]
        textures = []
        for face in faces:
            texture = pg.image.load(dir_path + f'{face}.{extension}').convert()
            
            if face in ['right', 'left', 'front', 'back']:
                texture = pg.transform.flip(texture, flip_x=True, flip_y=False)
            else: #top, bottom
                texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
            textures.append(texture)

        size = textures[0].get_size()
        texture_cube = self.ctx.texture_cube(size=size, components=3, data=None)

        for i in range(6):
            texture_data = pg.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube
