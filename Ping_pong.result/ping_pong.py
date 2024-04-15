from pygame import *
init()

size = [800, 600]
FPS = 60
run = True
score = 0

speed_x = 5
speed_y = 5

move_up1 = False
move_down1 = False

move_up2 = False
move_down2 = False


window = display.set_mode(size)
clock = time.Clock()
display.set_caption("Ping Pong")


bg = transform.scale(image.load("bg.jpg"), size)


class Sprite():
    def __init__(self, width, height, x, y, picture):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.rect = Rect(self.x, self.y, width, height)
        self.image = transform.scale(image.load(picture), (self.width, self.height))

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

    


washer = Sprite(95, 95, 300, 200, "washer.png")
stick1 = Sprite(280, 300, -140, 150, "stick1.png")
stick2 = Sprite(280, 300, 640, 150, "stick2.png")


while run:
    for e in event.get():
        key_press = key.get_pressed()
        if key_press[K_ESCAPE]:
            run = False
        if e.type == QUIT:
            run = False


        if key_press[K_w]:
            move_up1 = True
        else:
            move_up1 = False
        if key_press[K_s]:
            move_down1 = True
        else:
            move_down1 = False


        if key_press[K_UP]:
            move_up2 = True
        else:
            move_up2 = False
        if key_press[K_DOWN]:
            move_down2 = True
        else:
            move_down2 = False
        

    window.blit(bg, (0, 0))

    washer.draw()
    stick1.draw()
    stick2.draw()   


    washer.rect.x += speed_x
    washer.rect.y += speed_y


    if score == 10:
        speed_x = 7
        speed_y = 7


    #границы
    if washer.rect.x >= 710:
        speed_x *= -1
    if washer.rect.x <= 0:
        speed_x *= -1
    if washer.rect.y >= 505:
        speed_y *= -1        
    if washer.rect.y <=  0:
        speed_y *= -1  


    if move_up1 and stick1.rect.y >= 0:
        stick1.rect.y -= 5
    if move_down1 and stick1.rect.y <= 280:
        stick1.rect.y += 5
    if move_up2 and stick2.rect.y >= 0:
        stick2.rect.y -= 5
    if move_down2 and stick2.rect.y <= 280:
        stick2.rect.y += 5

    
    if washer.colliderect(stick1.rect):
        speed_x *= -1
        score += 1
    if washer.colliderect(stick2.rect):
        speed_x *= -1
        score += 1


    display.update()
    clock.tick(FPS)