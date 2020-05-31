import pygame

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


def main():
    pygame.init()
    size = [500,500]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Space_Batle")

    jugador = Player()
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

        screen.fill([255,255,255])
        screen.blit(jugador.imagen,[jugador.x,jugador.y])
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
