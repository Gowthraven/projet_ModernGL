import pygame as pg
import moderngl as mgl
import glm


class Texture:
    def __init__(self, window):
        self.window = window
        self.contexte = window.contexte
        self.textures = {}
        self.textures[0] = self.get_texture(path='assets/textures/grass.png')
        self.textures[1] = self.get_texture(path='assets/textures/rubiks_cube.jpg')
        self.textures['cat'] = self.get_texture(path='assets/cat/Cat_diffuse.jpg')
        self.textures['cabane'] = self.get_texture(path='assets/cabane/Wood_Tower_Col.jpg')

        self.textures['skybox'] = self.get_texture_box(dir_path='assets/shybox/', ext='jpg')
        self.textures['depth_texture'] = self.get_depth_texture()

    def get_depth_texture(self):
        # Création de la texture de profondeur
        depth_texture = self.contexte.depth_texture(self.window.WIN_SIZE)
        depth_texture.repeat_x = False
        depth_texture.repeat_y = False
        return depth_texture

    def get_texture(self, path):
        # Chargement de l'image
        texture = pg.image.load(path).convert()
        # Inversion de l'image
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        # Conversion en texture moderngl
        texture = self.contexte.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB')) 
        
        # Mipmaps 
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        texture.anisotropy = 32.0 # Facteur d'anisotropie
        return texture

    def destroy(self):
        [texture.release() for texture in self.textures.values()]

    def get_texture_box(self, dir_path, ext='png'):
        # Chargement des textures de la skybox
        faces = ['right', 'left', 'top', 'bottom'] + ['front', 'back'][::-1]
        textures = []
        for face in faces:
            texture = pg.image.load(dir_path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']: # Inversion de l'image pour les faces droite, gauche, avant et arrière
                texture = pg.transform.flip(texture, flip_x=True, flip_y=False)
            else:
                texture = pg.transform.flip(texture, flip_x=False, flip_y=True)

            textures.append(texture)

        size = textures[0].get_size()
        texture_cube = self.contexte.texture_cube(size=size, components=3, data=None)

        for i in range(6):
            texture_data = pg.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube