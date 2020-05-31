import pygame,random


#---------------------------------------------------
class Ships():
    def __init__(self):
        self.x = None
        self.y = None
        self.speed = None
        self.imagen = None
        self.size = None





class Player(Ships):
    def __init__(self):
        super().__init__()
        self.x = 300
        self.y = 200

        self.score = 0

        self.speed = 10
        self.speed_laser = -1

        #Size
        self.size = [60,60]
        self.size_laser = [10,31]

        #IMAGEN
        self.imagen = pygame.image.load("resources/pixel_ship_yellow.png").convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen,self.size)

        #IMAGEN LASER
        self.imagen_shot = pygame.image.load("resources/pixel_laser_yellow.png").convert_alpha()
        self.imagen_shot =pygame.transform.scale(self.imagen_shot,self.size_laser)


        self.lasers = []

    def shot(self):
        self.laser = (self.x + 25, self.y - 30 )
        self.lasers.append(self.laser)

    def move_shot(self):
        l = []
        for laser in self.lasers:
            l.append([laser[0],laser[1] + self.speed_laser])
        self.lasers = l[::]



class Enemy(Ships):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.size = [60,60]
        self.imagen = pygame.image.load("resources/meteorite.png").convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen,self.size)

        self.meteorites = []

    def move_meteorites(self):
        self.speed = round(self.level + 1)
        l = []
        for meteoro in self.meteorites:
            l.append([meteoro[0], meteoro[1] + self.speed])
        self.meteorites = l[::]

    def draw(self,screen):
        for meteoro in self.meteorites:
            screen.blit(self.imagen, [meteoro[0], meteoro[1]])


    def create(self):
        self.n1 = 5
        self.n2 = 8

        self.len_meteorite = random.randint(self.n1, self.n2)

        self.L = []

        for i in range(self.len_meteorite):
            self.bandera = True
            while self.bandera:
                self.x = random.randint(0, 500 - self.size[0])
                self.y = random.randint(-900, -320)

                self.bandera = False
                for i in self.L:
                    rect1 = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
                    rect2 = pygame.Rect(i[0], i[1], self.size[0], self.size[1])
                    self.cond = rect1.colliderect(rect2)
                    self.bandera = self.bandera or self.cond
            self.L.append([self.x,self.y])

        self.meteorites = self.L[::]

#---------------------------------------------------------------

def screen_update(screen,score):
    #Title
    font = pygame.font.Font(None,50)
    text = "Score: {}".format(str(score))

    #Background
    background = pygame.image.load("resources/background-black.png").convert_alpha()
    background = pygame.transform.scale(background,[500,500])

    screen.blit(background,[0,0])
    screen.blit(font.render(text,0,[255,255,255]),[0,0])






def main():
    pygame.init()
    size = [500,500]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Space_Batle")

    jugador = Player()
    meteorite = Enemy()

    meteorite.create()

    print(meteorite.meteorites)



    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jugador.shot()


        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and jugador.y + jugador.speed >0:
            jugador.y-= jugador.speed

        if keys[pygame.K_s] and jugador.y + jugador.speed + jugador.size[1] - 10< size[1]:
            jugador.y += jugador.speed

        if keys[pygame.K_a] and jugador.x + jugador.speed >0:
            jugador.x-= jugador.speed

        if keys[pygame.K_d] and jugador.x + jugador.speed + jugador.size[0]-15< size[1]:
            jugador.x+= jugador.speed





        screen_update(screen,jugador.score)
        meteorite.move_meteorites()

        jugador.move_shot()

        screen.blit(jugador.imagen,[jugador.x,jugador.y])
        meteorite.draw(screen)

        for i in jugador.lasers:
            screen.blit(jugador.imagen_shot, [i[0], i[1]])

        jugador.move_shot()

        pygame.display.update()
        clock.tick(60)

#
if __name__ == '__main__':
    main()
