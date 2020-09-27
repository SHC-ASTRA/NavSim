import pygame
from WorldManager.WorldManager import *


def main():
    rover = Rover()
    world = WorldManager(rover, time_scale=1.0)

    alive = True

    while alive:
        pass


if __name__ == '__main__':
    main()
