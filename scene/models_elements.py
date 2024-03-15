from .model_utils import *


class Cube(ExtendedBaseModel):
    def __init__(self, window, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(window, vao_name, tex_id, pos, rot, scale)

class RotationCube(Cube):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self):
        self.model = self.get_model_matrix()
        super().update()

class Cat(ExtendedBaseModel):
    def __init__(self, window, vao_name='cat', tex_id='cat',
                 pos=(0, 0, 0), rot=(-90, 50, 0), scale=(0.15, 0.15, 0.15)):
        super().__init__(window, vao_name, tex_id, pos, rot, scale)

class Cabane(ExtendedBaseModel):
    def __init__(self, window, vao_name='cabane', tex_id='cabane',
                 pos=(0, 0, 0), rot=(0, -20, 0), scale=(2, 2, 2)):
        super().__init__(window, vao_name, tex_id, pos, rot, scale)
