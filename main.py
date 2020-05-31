import pygame

#---------------------------------------------------
class Ships():
    def __init__(self):
        self.x = None
        self.y = None
        self.speed = None
        self.imagen = None


class Player(Ships):
    def __init__(self):
        super().__init__()
        self.x = 300
        self.y = 200
        self.speed = 10
        self.speed_laser = -1
        self.imagen = pygame.image.load("resources/pixel_ship_yellow.png").convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen,[60,60])
        self.score = 0
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
    def __init__(self,x,y):
        super().__init__()
        self.speed = 5
        self.imagen = pygame.image.load("resources/meteorite.png").convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen,[70,70])
        self.x = x
        self.y = y

    def move(self):
        self.y += self.speed

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
    meteorite = Enemy(50,-10)



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

        if keys[pygame.K_w]:
            jugador.y-= jugador.speed

        if keys[pygame.K_s]:
            jugador.y += jugador.speed

        if keys[pygame.K_a]:
            jugador.x-= jugador.speed

        if keys[pygame.K_d]:
            jugador.x+= jugador.speed





        screen_update(screen,jugador.score)
        meteorite.move()

        jugador.move_shot()

        screen.blit(jugador.imagen,[jugador.x,jugador.y])
        screen.blit(meteorite.imagen, [meteorite.x, meteorite.y])

        for i in jugador.lasers:
            im = pygame.image.load("resources/pixel_laser_yellow.png").convert_alpha()
            im = pygame.transform.scale(im,[10,31])
            screen.blit(im, [i[0], i[1]])

        jugador.move_shot()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
