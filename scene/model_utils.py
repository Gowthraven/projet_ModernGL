import moderngl as mgl
import numpy as np
import glm


class BaseModel:
    def __init__(self, window, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.window = window
        self.pos = pos
        self.vao_name = vao_name
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = window.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.window.camera

    def get_model_matrix(self):
        # Matrice du modèle (position, rotation, échelle)
        model = glm.mat4()
        model = glm.translate(model, self.pos)
        model = glm.scale(model, self.scale)
        # Rotation
        model = glm.rotate(model, self.rot.z, glm.vec3(0, 0, 1))
        model = glm.rotate(model, self.rot.y, glm.vec3(0, 1, 0))
        model = glm.rotate(model, self.rot.x, glm.vec3(1, 0, 0))
        return model

    def render(self):
        # Mise à jour des paramètres, rendu
        self.update()
        self.vao.render()


class ExtendedBaseModel(BaseModel):
    def __init__(self, window, vao_name, tex_id, pos, rot, scale):
        super().__init__(window, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use(location=0)
        self.program['camPos'].write(self.camera.position)
        self.program['view'].write(self.camera.view)
        self.program['model'].write(self.model)

    def update_shadow(self):
        self.shadow_program['model'].write(self.model)

    def render_shadow(self):
        self.update_shadow()
        self.shadow_vao.render()

    def on_init(self):
        self.depth_texture = self.window.mesh.texture.textures['depth_texture']
        self.program['shadowMap'] = 1
        self.depth_texture.use(location=1)

        self.shadow_vao = self.window.mesh.vao.vaos['shadow_' + self.vao_name]
        self.shadow_program = self.shadow_vao.program
        self.shadow_program['projection'].write(self.camera.projection)
        self.shadow_program['view_light'].write(self.window.light.view_light)
        self.shadow_program['model'].write(self.model)

        self.program['view_light'].write(self.window.light.view_light)
        self.program['u_resolution'].write(glm.vec2(self.window.WIN_SIZE))

        self.texture = self.window.mesh.texture.textures[self.tex_id]
        self.program['u_texture'] = 0
        self.texture.use(location=0)
        self.program['projection'].write(self.camera.projection)
        self.program['view'].write(self.camera.view)
        self.program['model'].write(self.model)
        self.program['light.position'].write(self.window.light.position)
        self.program['light.I_ambiant'].write(self.window.light.I_ambiant)
        self.program['light.I_diffuse'].write(self.window.light.I_diffuse)
        self.program['light.I_specular'].write(self.window.light.I_specular)
