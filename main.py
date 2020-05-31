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
        self.imagen = pygame.image.load("resources/pixel_ship_blue_small.png").convert_alpha()
        self.score = 0


class Enemy(Ships):
    def __init__(self,x,y):
        super().__init__()
        self.speed = 5
        self.imagen = pygame.image.load("resources/meteorite.png").convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen,[50,50])
        self.x = x
        self.y = y

    def move(self):
        self.y += self.speed

#---------------------------------------------------------------

def screen_update(screen,score):
    #Title
    font = pygame.font.Font(None,30)
    text = "Score: {}".format(str(score))

    #Background
    background = pygame.image.load("resources/background-black.png").convert_alpha()

    screen.blit(background,[0,0])
    screen.blit(font.render(text,0,[255,255,255]),[0,0])









def main():
    pygame.init()
    size = [800,800]
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

        screen.blit(jugador.imagen,[jugador.x,jugador.y])
        screen.blit(meteorite.imagen, [meteorite.x, meteorite.y])
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
