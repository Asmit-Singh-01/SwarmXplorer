import pygame
import random
from core.robot_agent import SwarmAgent
from config import ARENA_WIDTH, ARENA_HEIGHT, NUM_ROBOTS

pygame.init()
screen = pygame.display.set_mode((ARENA_WIDTH, ARENA_HEIGHT))
clock = pygame.time.Clock()

# Spawn Swarm
robots = [SwarmAgent(i, random.randint(50, 750), random.randint(50, 550)) for i in range(NUM_ROBOTS)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 20))

    # Get positions dict for Mesh update
    positions = {bot.id: bot.position for bot in robots}

    for bot in robots:
        bot.step(positions)
        
        # Draw Mesh Links
        for n_id in bot.mesh.neighbors:
            pygame.draw.line(screen, (0, 100, 255), bot.position, positions[n_id], 1)
            
        # Draw Robot Body
        pygame.draw.circle(screen, (0, 255, 150), bot.position.astype(int), 5)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
