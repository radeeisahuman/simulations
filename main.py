import pygame as pg
import shapes

def main():
    pg.init()
    screen = pg.display.set_mode((1600, 780))
    pg.display.set_caption('Gravity Sim')
    clock = pg.time.Clock()
    circle = shapes.Circle((255,255,0), 800, 100, 50)
    
    running = True

    while running:
        time = clock.tick(60)/1000
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running=False
        circle.fall(time)
        screen.fill((0, 0, 0))
        circle.render(screen)
        rectangle = pg.draw.rect(screen, (0, 255, 0), (0, 600, 1600, 180))
        pg.display.flip()
        clock.tick(60)

    pg.quit()

if __name__ == '__main__':
    main()