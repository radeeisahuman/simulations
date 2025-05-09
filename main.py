import pygame as pg
import shapes

def main():
    pg.init()
    screen = pg.display.set_mode((1600, 780))
    pg.display.set_caption('Gravity Sim')
    clock = pg.time.Clock()
    circle = shapes.Circle(50, (800, 100), (255,255,0))
    circle.draw(screen)
    rectangle = pg.draw.rect(screen, (0, 255, 0), (0, 600, 1600, 180))
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running=False
        circle.fall()
        pg.display.flip()
        clock.tick(60)

    pg.quit()

if __name__ == '__main__':
    main()