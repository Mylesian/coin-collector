import asyncio
import pygame, sys
import player as play
import coin

GRAVITY = 0.5
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 760
PLAYER_SPRITE = pygame.transform.scale(pygame.image.load("assets/player.png").convert_alpha(), (50, 50))
COIN_SPRITE = pygame.transform.scale(pygame.image.load("assets/coin.png").convert_alpha(), (25, 25))

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pink Slime Coins")

async def main():
    clock = pygame.time.Clock()
    player = play.Player(50, 700 - 28.125, PLAYER_SPRITE)
    platforms = [pygame.Rect(0, 700, 1200, 60),
                 pygame.Rect(200, 600, 100, 25),
                 pygame.Rect(450, 550, 100, 25),
                 pygame.Rect(275, 440, 100, 25),
                 pygame.Rect(275, 335, 100, 25),
                 pygame.Rect(700, 570, 400, 25)]
    coins =     [coin.Coin(250, 570, COIN_SPRITE),
                 coin.Coin(325, 305, COIN_SPRITE),
                 coin.Coin(800, 540, COIN_SPRITE),
                 coin.Coin(1000, 540, COIN_SPRITE),
                 coin.Coin(900, 450, COIN_SPRITE)]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((194, 252, 255))
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            player.move_left()
        if pressed[pygame.K_RIGHT]:
            player.move_right()
        if not (pressed[pygame.K_RIGHT] or pressed[pygame.K_LEFT]):
            player.reset_velocity_x()
        if pressed[pygame.K_UP]:
            player.jump()
            
        player.y += player.velocity.y
        player.x += player.velocity.x
        
        player.check_touches(platforms)
        player.clamp_walls()
        
        if not player.on_ground:
            player.velocity.y += GRAVITY
            
        for i in player.collidelistall(coins):
            coins.remove(coins[i])
        
        for plat in platforms:
            pygame.draw.rect(screen, (105, 247, 114), plat)
        for c in coins:
            screen.blit(c.sprite, (c.x - c.r, c.y - c.r))
        screen.blit(player.sprite, (player.x, player.y - 21.875))
        
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)
    
    
    pygame.quit()
    sys.exit()

asyncio.run(main())
