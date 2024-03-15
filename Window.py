import pygame as pg
import moderngl as mgl
import sys

from scene.model_utils import *
from scene.camera import Camera
from scene.light import Light
from render.mesh import Mesh
from scene.scene import Scene
from scene.render import Render


class Window:
    def __init__(self, win_size=(1600, 900)):
        pg.init()
            # Configuration d'OpenGL
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 4)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        self.WIN_SIZE = win_size
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)

            # Création du contexte OpenGL
        self.contexte = mgl.create_context()
        self.contexte.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)

            # Gestion des événements
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

            # Temps
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0

            # Elements de la scène
        self.light = Light()
        self.camera = Camera(self)
        self.mesh = Mesh(self)
        self.scene = Scene(self)
        self.scene_renderer = Render(self)

    def render(self):
            # Clear du framebuffer, rendu de la scène et swap des buffers
        self.contexte.clear(color=(0, 0, 0))
        self.scene_renderer.render()
        pg.display.flip() # Swap des buffers

    def get_time(self): #Utile pour le cube qui tourne
        self.time = pg.time.get_ticks() * 0.001

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                self.scene_renderer.destroy()
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.get_time() #utile pour le cube qui tourne
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)

