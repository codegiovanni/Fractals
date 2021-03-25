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
                pygame.draw.line(screen, (hsv2rgb(hue, 1, 1)), (self.x, self.y), (x2, y2), 2)
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

# Adrian-Mariano-Doily             python fractals.py fractals/Adrian_Mariano_Doily.txt 1350 350 110 0.5
# Anthony-Hanmer-ADH231a           python fractals.py fractals/Anthony_Hanmer_ADH231a.txt 960 1000 50 0.52
# Anthony-Hanmer-ADH256a           python fractals.py fractals/Anthony_Hanmer_ADH256a.txt 650 850 50 0.55
# Anthony-Hanmer-ADH258a           python fractals.py fractals/Anthony_Hanmer_ADH258a.txt 700 950 80 0.4
# Board                            python fractals.py fractals/board.txt 500 1000 100 0.52
# Box-fractal                      python fractals.py fractals/box-fractal.txt 1400 1000 100 0.52
# Classic-Sierpinski-curve         python fractals.py fractals/classic-sierpinski-curve.txt 1150 750 30 0.5
# Cross                            python fractals.py fractals/cross.txt 950 250 250 0.5
# Crystal:                         python fractals.py fractals/crystal.txt 580 920 100 0.5
# Dragon-curve:                    python fractals.py fractals/dragon-curve.txt 960 540 200 0.75
# Hilbert-curve                    python fractals.py fractals/hilbert-curve.txt 1920 1080 250 0.67
# Hilbert-curve-II                 python fractals.py fractals/hilbert-curve-II.txt 0 1080 50 0.7
# Koch-snowflake:                  python fractals.py fractals/koch-snowflake.txt 1200 900 100 0.5
# Krishna-anklets                  python fractals.py fractals/krishna-anklets.txt 1400 550 60 0.8
# Levy-curve                       python fractals.py fractals/levy-curve.txt 1100 750 70 0.8
# Moore-curve                      python fractals.py fractals/moore-curve.txt 1000 1080 50 0.8
# no_name                          python fractals.py fractals/no_name.txt 960 1020 120 0.51
# Peano-curve                      python fractals.py fractals/peano-curve.txt 0 1080 70 0.7
# Peano-Gosper-curve:              python fractals.py fractals/peano-gosper-curve.txt 600 280 200 0.5
# Pentaplexity                     python fractals.py fractals/pentaplexity.txt 550 850 150 0.5
# Plant:                           python fractals.py fractals/plant.txt 960 1000 100 0.6
# Quadratic-Gosper                 python fractals.py fractals/quadratic-gosper.txt 1920 1080 70 0.61
# Quadratic-Koch-island            python fractals.py fractals/quadratic-koch-island.txt 950 850 50 0.5
# Quadratic-snowflake              python fractals.py fractals/quadratic-snowflake.txt 500 1000 50 0.52
# Rings:                           python fractals.py fractals/rings.txt 700 250 60 0.5
# Sierpinski-arrowhead             python fractals.py fractals/sierpinski-arrowhead.txt 1300 1000 90 0.7
# Sierpinski-carpet                python fractals.py fractals/sierpinski-carpet.txt 500 1020 50 0.6
# Sierpinski-curve:                python fractals.py fractals/sierpinski-curve.txt 500 550 200 0.52
# Sierpinski-sieve:                python fractals.py fractals/sierpinski-sieve.txt 1200 950 400 0.5
# Terdragon-curve                  python fractals.py fractals/terdragon-curve.txt 400 500 200 0.7
# Three-dragon-curve               python fractals.py fractals/three-dragon-curve.txt 600 550 40 0.88
# Tiles                            python fractals.py fractals/tiles.txt 900 800 30 0.75
# Tree:                            python fractals.py fractals/tree.txt 960 950 250 0.5
# Triangle                         python fractals.py fractals/triangle.txt 1000 250 60 0.8
# Twin-dragon-curve                python fractals.py fractals/twin-dragon-curve.txt 1000 250 90 0.8
# William-McWorter-Maze01          python fractals.py fractals/William_McWorter_Maze01.txt 1100 750 50 0.8
# William-McWorter-Moore           python fractals.py fractals/William_McWorter_Moore.txt 900 350 100 0.5
# William-McWorter-Pentant         python fractals.py fractals/William_McWorter_Pentant.txt 1000 120 90 0.39
# William-McWorter-Pentl           python fractals.py fractals/William_McWorter_Pentl.txt 1400 400 90 0.5
