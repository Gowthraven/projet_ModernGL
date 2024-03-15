from .model_utils import *

class SkyBox(BaseModel):
    def __init__(self, window, vao_name='skybox', tex_id='skybox', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(window, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        view = glm.mat4(glm.mat3(self.camera.view))
        self.program['m_invProjView'].write(glm.inverse(self.camera.projection * view))

    def on_init(self):
        self.texture = self.window.mesh.texture.textures[self.tex_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)