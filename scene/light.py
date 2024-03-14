import glm 

class Light:
    def __init__(self, position=(1,1,-1), color=(1,1,1)):
        self.position = glm.vec3(position) #Position de la lumière
        self.color = glm.vec3(color) #Couleur de la lumière

        self.I_ambiant = 0.1 * self.color #intensité ambiante
        self.I_diffuse = 0.8 * self.color #intensité diffuse
        self.I_specular = 0.9 * self.color #intensité spéculaire