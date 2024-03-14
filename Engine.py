import sys
import pygame as pg
import moderngl as mg

class Engine:
    def __init__(self, win_size=(1600, 1000)):
        """Initialize the render engine."""
        pg.init()
        self.WIN_SIZE = win_size

        # openGL context
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)

        self.ctx = mg.create_context()
        self.ctx.enable(flags=mg.DEPTH_TEST | mg.CULL_FACE)
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
    
    def check_events(self):
        """Check for events and handle them."""
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def rendering(self): 
        """Clear the framebuffer and swap buffers."""
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        pg.display.flip()

    def run(self):
        """Run the rendering engine."""
        while True:
            self.check_events()
            self.rendering()
            self.clock.tick(60)
            self.delta_time = self.clock.get_time()
            self.time = pg.time.get_ticks() * 0.001
