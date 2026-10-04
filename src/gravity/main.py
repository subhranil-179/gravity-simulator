import pygame
from .body import Body, Space
from .simulation import Simulation

def main():
    # sun = Body("Sun", 20.5700, 5.972*332946, 'yellow', coordinates=(200, 200), velocity=(5, 5))
    # mercury = Body("Mercury", 1.0900, 0.370, 'orange', coordinates=(280, 400), velocity=(40, 0))
    # earth = Body("Earth", 6.371, 5.972, 'blue', coordinates=(300, 700), velocity=(25, -7))
    # moon = Body("Moon", 1.5700, 0.072, 'white', coordinates=(330, 720), velocity=(22, -5))
    # jupiter = Body("Jupiter", 12.5700, 5.972*332946, 'brown', coordinates=(1400, 500), velocity=(-5, -5))

    sun = Body("Sun", 20.5700, 5.972*339949, 'yellow', coordinates=(900, 300), velocity=(15, 15))
    mercury = Body("Mercury", 1.0900, 0.370, 'orange', coordinates=(280, 400), velocity=(40, 0))
    earth = Body("Earth", 6.371, 5.972, 'blue', coordinates=(300, 700), velocity=(25, -7))
    moon = Body("Moon", 1.5700, 0.072, 'white', coordinates=(330, 720), velocity=(22, -5))
    jupiter = Body("Jupiter", 12.5700, 5.972*332941, 'brown', coordinates=(1400, 500), velocity=(-15, -15))

    space = Space((sun, mercury, earth, moon, jupiter))

    simulation = Simulation(space)
    simulation.run()

    pygame.quit()

    return 0

if __name__ == '__main__':
    main()

'''
Force -> accelartion -> x, y
f = (Gm1m2/r**r)
'''
