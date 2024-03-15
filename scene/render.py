class Render:
    def __init__(self, window):
        self.window = window
        self.contexte = window.contexte
        self.mesh = window.mesh
        self.scene = window.scene

        # Buffer pour la profondeur
        self.depth_texture = self.mesh.texture.textures['depth_texture']
        self.depth_fbo = self.contexte.framebuffer(depth_attachment=self.depth_texture)

    def destroy(self):
        self.depth_fbo.release()

    def render_shadow(self):
        self.depth_fbo.clear()
        self.depth_fbo.use()
        for obj in self.scene.objects:
            obj.render_shadow()

    def main_render(self):
        self.window.contexte.screen.use()
        for obj in self.scene.objects:
            obj.render()

        self.scene.skybox.render()

    def render(self):
        self.scene.update()
        # Passe 1 : rendu de la profondeur, ombres, Passe 2 : rendu de la scène
        self.render_shadow()
        self.main_render()
