import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 760

class Player(pygame.Rect):
    def __init__(this, x, y, sprite):
        super().__init__(x, y, 50, 28.125)
        this.sprite = sprite
        this.speed = 5
        this.velocity = pygame.Vector2(0, 0)
        this.jump_strength = 11
        this.on_ground = False
        
    def move_left(this):
        this.velocity.x = -this.speed
    def move_right(this):
        this.velocity.x = this.speed
    def reset_velocity_x(this):
        this.velocity.x = 0
    def jump(this):
        if this.on_ground:
            this.velocity.y -= this.jump_strength
            this.on_ground = False
            
    def check_touches(this, platforms):
        touchlist = this.collidelistall(platforms)
        
        if touchlist == []:
            this.on_ground = False
            
        for i in touchlist:
            plat = platforms[i]
            
            if ((this.top + 1 > plat.top and this.top < plat.bottom) and
                (this.right < plat.right and this.right > plat.left)):
                last = this.topright - this.velocity
                scaled = pygame.math.Vector2(last)
                
                if last.y != 0:
                    scaled *= plat.bottom / last.y
                
                if scaled.magnitude_squared() > last.magnitude_squared():
                    this.right = plat.left
                    this.velocity.x = 0
                else:
                    this.top = plat.bottom
                    this.velocity.y = 0
            elif ((this.top + 1 > plat.top and this.top < plat.bottom) and
                  (this.left > plat.left and this.left < plat.right)):
                last = this.topleft - this.velocity
                scaled = pygame.math.Vector2(last)
                
                if last.y != 0:
                    scaled *= plat.bottom / last.y
                
                if scaled.magnitude_squared() > last.magnitude_squared():
                    this.left = plat.right
                    this.velocity.x = 0
                else:
                    this.top = plat.bottom
                    this.velocity.y = 0
            elif ((this.bottom > plat.top and this.bottom - 1 < plat.bottom) and
                  (this.right < plat.right and this.right > plat.left)):
                last = this.bottomright - this.velocity
                last.y -= 1
                scaled = pygame.math.Vector2(last)
                
                if last.y != 0:
                    scaled *= plat.top / last.y
                
                if scaled.magnitude_squared() < last.magnitude_squared():
                    this.right = plat.left
                    this.velocity.x = 0
                else:
                    this.bottom = plat.top
                    this.on_ground = True
                    this.velocity.y = 0
            elif ((this.bottom > plat.top and this.bottom - 1 < plat.bottom) and
                  (this.left > plat.left and this.left < plat.right)):
                last = this.bottomleft - this.velocity
                last.y -= 1
                scaled = pygame.math.Vector2(last)
                
                if last.y != 0:
                    scaled *= plat.top / last.y
                    
                if scaled.magnitude_squared() < last.magnitude_squared():
                    this.left = plat.right
                    this.velocity.x = 0
                else:
                    this.bottom = plat.top
                    this.on_ground = True
                    this.velocity.y = 0
            
    def clamp_walls(this):
        if this.left < 0:
            this.left = 0
        elif this.right > SCREEN_WIDTH:
            this.right = SCREEN_WIDTH
        
        if this.top < 0:
            this.top = 0
            this.velocity.y = 0
        elif this.bottom > SCREEN_HEIGHT:
            this.bottom = SCREEN_HEIGHT
            
