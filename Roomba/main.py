import pygame
from simulator import Simulator

if __name__ == "__main__":
    pygame.init()
    sim = Simulator()
    sim.run()
    pygame.quit()
