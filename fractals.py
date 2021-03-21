import pygame
import sys
import math
import colorsys

pygame.init()

WIDTH = 1920
HEIGHT = 1080

l_system_text = sys.argv[1]
start = int(sys.argv[2]), int(sys.argv[3])
length = int(sys.argv[4])
ratio = float(sys.argv[5])

with open(l_system_text) as f:
    axiom = f.readline()
    num_rules = int(f.readline())
    rules = {}
    for i in range(num_rules):
        rule = f.readline().split(' ')
        rules[rule[0]] = rule[1]
    angle = math.radians(int(f.readline()))


class LSystem():
    def __init__(self, axiom, rules, angle, start, length, ratio):
        self.sentence = axiom
        self.rules = rules
        self.angle = angle
        self.start = start
        self.x, self.y = start
        self.length = length
        self.ratio = ratio
        self.theta = math.pi / 2
        self.positions = []

    def __str__(self):
        return self.sentence

    def generate(self):
        self.x, self.y = self.start
        self.theta = math.pi / 2
        self.length *= self.ratio
        new_sentence = ""
        for char in self.sentence:
            mapped = char
            try:
                mapped = self.rules[char]
            except:
                pass
            new_sentence += mapped
        self.sentence = new_sentence

    def draw(self, screen):
        hue = 0
        for char in self.sentence:
            if char == 'F':
                x2 = self.x - self.length * math.cos(self.theta)
                y2 = self.y - self.length * math.sin(self.theta)
                pygame.draw.line(screen, (hsv2rgb(hue, 1, 1)), (self.x, self.y), (x2, y2))
                self.x, self.y = x2, y2
            elif char == '+':
                self.theta += self.angle
            elif char == '-':
                self.theta -= self.angle
            elif char == '[':
                self.positions.append({'x': self.x, 'y': self.y, 'theta': self.theta})
            elif char == ']':
                position = self.positions.pop()
                self.x, self.y, self.theta = position['x'], position['y'], position['theta']
            hue += 0.00005


def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.mouse.set_visible(False)

    fractal = LSystem(axiom, rules, angle, start, length, ratio)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_SPACE]:
                screen.fill((0, 0, 0))
                fractal.draw(screen)
                fractal.generate()
            if keystate[pygame.K_ESCAPE]:
                pygame.quit()
        pygame.display.update()


main()

# Crystal:            python fractals.py fractals/crystal.txt 600 900 100 0.5
# Dragon-curve:       python fractals.py fractals/dragon-curve.txt 960 540 200 0.75
# Hilberts-curve:     python fractals.py fractals/hilberts-curve.txt 0 1080 100 0.75
# Koch-snowflake:     python fractals.py fractals/koch-snowflake.txt 1200 900 100 0.5
# Peano-Gosper-curve: python fractals.py fractals/peano-gosper-curve.txt 600 280 200 0.5
# Plant:              python fractals.py fractals/plant.txt 960 1000 100 0.6
# Rings:              python fractals.py fractals/rings.txt 750 300 50 0.5
# Sierpinski-sieve:   python fractals.py fractals/sierpinski-sieve.txt 1200 950 400 0.5
# Sierpinski-curve:   python fractals.py fractals/sierpinski-curve.txt 600 500 200 0.5
# Tree:               python fractals.py fractals/tree.txt 960 950 250 0.5
