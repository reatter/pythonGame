# Am Anfang kann man Module laden und importieren
# Das sind Programmteile, die von anderen programmiert wurden
import pygame
from pygame.locals import *


# Das ist ein Kommentar

# Python speaks english
print("Hallo Paul")

# damit python etwas mehrmals macht, gibt es die for-Schleife, und Listen wir range(100)
for nummer in range(100):
    # das innere der Schleife ist eingerückt
    print("Zahl ", nummer)

pygame.init()  # pygame startet

# Farben werden als RGB-Tupel gespeichert
# ROT GRÜN BLAU WERT aus 0-255
BLUE = (0, 0, 255)

# ein Screen zum Zeichnen des spiels
screen = pygame.display.set_mode(size=(1920, 1080))

# def definiert eine Funktion, die man immer wieder verwenden kann.
def drawCircle():
    pos=pygame.mouse.get_pos()
    pygame.draw.circle(screen, BLUE, pos, 20) # Here <<<

