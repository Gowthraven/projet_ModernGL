import glm

#Propriétés de la caméra, voir perspective projection
FOV = 45 #en degrés, champ de vision
NEAR = 0.1
FAR = 100.0

class Camera: 
    def __init__(self, window):
        self.window = window
        self.aspect_ratio = window.WIN_SIZE[0] / window.WIN_SIZE[1]
        self.m_projection = self.get_projection_matrix() #Matrice de projection

    def get_projection_matrix(self): 
        """Return the projection matrix."""
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR) #glm.perspective(FOV, aspect_ratio, near, far)