import pygame
import os
from my_sprite import my_sprite
from sprite_collection import sprite_collection
import random

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collection Demo")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

def create_demo_images():
    colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0)]
    filenames = []
    os.makedirs("images", exist_ok=True)
    for i, color in enumerate(colors, start=1):
        surf = pygame.Surface((50, 50))
        surf.fill(color)
        fname = f"images/demo{i}.png"
        pygame.image.save(surf, fname)
        filenames.append(fname)
    return filenames

image_files = create_demo_images()
sprites = sprite_collection()

def add_random_sprite():
    fname = random.choice(image_files)
    x = random.randint(0, WIDTH-50)
    y = random.randint(0, HEIGHT-50)
    sprites.add(my_sprite(fname, (x, y)))

for _ in range(4):
    add_random_sprite()

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                add_random_sprite()

    for s in sprites.get_collection():
        screen.blit(s.get_image(), s.loc)

    count_text = font.render(f"Sprites: {len(sprites)}", True, (255, 255, 255))
    screen.blit(count_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
