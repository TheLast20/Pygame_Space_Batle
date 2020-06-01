import pygame,random
from data.charter import *
from data.funtion import *

def main():
    #Inicializo el sistema
    pygame.init()
    size = [500,500]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Space_Batle")

    #Genero los elementos
    jugador = Player()
    meteorite = Enemy()

    #Create Clock
    clock = pygame.time.Clock()

    game = True
    while game:
        #"Genero las holeadas"
        num = 2 + jugador.level

        for i in range(num):
            meteorite.create()
            run = True

            while run:
                if len(meteorite.elements)==0:
                    run = False

                if jugador.life >0 :
                    controlers(jugador, size)
                    screen_update(screen)
                    destroy(jugador, meteorite, screen)

                    if collid_nave(jugador,meteorite):
                        jugador.life -=1
                        jugador.elements = []
                        while len(meteorite.elements)>0:
                            screen_update(screen)
                            meteorite.moven()
                            screen.blit(jugador.imagen_kill, [jugador.x, jugador.y])
                            meteorite.draw_elements(screen)
                            jugador.draw_elements(screen)
                            screen_text(screen, jugador)
                            pygame.display.update()
                            clock.tick(60)

                    else:
                        meteorite.moven()
                        jugador.moven()
                        screen.blit(jugador.imagen,[jugador.x,jugador.y])
                        meteorite.draw_elements(screen)
                        jugador.draw_elements(screen)
                        screen_text(screen, jugador)

                        pygame.display.update()

                else:
                    game = False
                    run = False

                clock.tick(60)


        jugador.level+=1

    exit()




    #
if __name__ == '__main__':
    main()
