import pygame,random

#---------------------------------------------------
class Ships():
    def __init__(self):
        self.level = 1
        self.x = None
        self.y = None

        self.size = None

        #Lasers, Meteoros
        self.elements = None
        self.speed_element = None
        self.imagen_element = None
        self.size_element = None

        self.limit = None
        self.direction = None

    def moven(self):
        self.L = []
        for element in self.elements:
            if (self.limits(element)):
                self.L.append([element[0], element[1] + self.speed_element])
        self.elements = self.L[::]

    def limits(self,element):
        if self.direction == "UP":
            return element[1]  > self.limit

        elif self.direction == "DOWN":
            return element[1] + self.size_element[1] + self.speed_element < self.limit

    def draw_elements(self,screen):
        for element in self.elements:
            screen.blit(self.imagen_element, [element[0], element[1]])

class Player(Ships):
    def __init__(self):
        super().__init__()
        #Caracteristicas
        self.x = 300
        self.y = 200
        self.speed = 10
        self.score = 0
        self.life = 3

        #Lasers
        self.elements = []
        self.speed_element = -5
        self.limit = -50
        self.direction = "UP"


        #Size
        self.size = [60,60]
        self.size_element = [10,31]

        #IMAGEN
        self.imagen = pygame.image.load("resources/pixel_ship_yellow.png").convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen,self.size)

        self.imagen_kill = pygame.image.load("resources/explotion.png").convert_alpha()
        self.imagen_kill = pygame.transform.scale(self.imagen_kill,self.size)

        #IMAGEN LASER
        self.imagen_element  = pygame.image.load("resources/pixel_laser_yellow.png").convert_alpha()
        self.imagen_element  =pygame.transform.scale(self.imagen_element,self.size_element)

    def shot(self):
        self.laser = (self.x + 25, self.y - 30 )
        self.elements.append(self.laser)

class Enemy(Ships):
    def __init__(self):
        super().__init__()
        self.size_element = [60,60]

        #Meteorites
        self.elements = []
        self.speed_element = 5
        self.imagen_element = pygame.image.load("resources/meteorite.png").convert_alpha()
        self.imagen_element = pygame.transform.scale(self.imagen_element,self.size_element)

        self.limit = 550
        self.direction = "DOWN"


    def change_speed(self):
        self.speed_element = round(self.level + 1)


    def create(self):
        self.n1 = 5
        self.n2 = 8

        self.len_meteorite = random.randint(self.n1, self.n2)

        self.L = []

        for i in range(self.len_meteorite):
            self.bandera = True
            while self.bandera:
                self.x = random.randint(0, 500 - self.size_element[0])
                self.y = random.randint(-600, -320)

                self.bandera = False
                for i in self.L:
                    rect1 = pygame.Rect(self.x, self.y, self.size_element[0], self.size_element[1])
                    rect2 = pygame.Rect(i[0], i[1], self.size_element[0], self.size_element[1])
                    self.cond = rect1.colliderect(rect2)
                    self.bandera = self.bandera or self.cond
            self.L.append([self.x,self.y])

        self.elements = self.L[::]
