import random
#from button import Button
import pygame
import os
from pygame import mixer

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

#global constants
Screen_Height = 600
Screen_Width = 1100
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))

Running = [pygame.image.load(os.path.join("asset/Haziq/Run.png")),
           pygame.image.load(os.path.join("asset/Haziq/Run2.png"))]
Jumping = pygame.image.load(os.path.join("asset/Haziq/Jump.png"))
Ducking = [pygame.image.load(os.path.join("asset/Haziq/Ducking.png")),
           pygame.image.load(os.path.join("asset/Haziq/Ducking1.png"))]
ObstacleBig = [pygame.image.load(os.path.join("asset/Obstacle/obstacle.png")),
            pygame.image.load(os.path.join("asset/Obstacle/obstacle1.png")),
            pygame.image.load(os.path.join("asset/Obstacle/obstacle2.png"))]
ObstacleSmall = [pygame.image.load(os.path.join("asset/Obstacle/obstacle3.png")),
            pygame.image.load(os.path.join("asset/Obstacle/obstacle4.png")),
            pygame.image.load(os.path.join("asset/Obstacle/obstacle5.png"))]
UFO = [pygame.image.load(os.path.join("asset/Obstacle/obstacle6.png")),
       pygame.image.load(os.path.join("asset/Obstacle/obstacle7.png"))]
Cloud = pygame.image.load(os.path.join("asset/Others/cloud.png"))
Track = pygame.image.load(os.path.join("asset/Tiles/Track.png"))
Audio = pygame.image.load(os.path.join("asset/Others/download.png"))
Cutie = [pygame.image.load(os.path.join("asset/Cutie/1.png")),
         pygame.image.load(os.path.join("asset/Cutie/2.png")),
         pygame.image.load(os.path.join("asset/Cutie/3.png")),
         pygame.image.load(os.path.join("asset/Cutie/4.png")),
         pygame.image.load(os.path.join("asset/Cutie/5.png")),
         pygame.image.load(os.path.join("asset/Cutie/6.png")),
         pygame.image.load(os.path.join("asset/Cutie/7.png")),
         pygame.image.load(os.path.join("asset/Cutie/8.png")),
         pygame.image.load(os.path.join("asset/Cutie/9.png")),
         pygame.image.load(os.path.join("asset/Cutie/10.png")),
         pygame.image.load(os.path.join("asset/Cutie/11.png")),
         pygame.image.load(os.path.join("asset/Cutie/12.png")),
         pygame.image.load(os.path.join("asset/Cutie/13.png")),
         pygame.image.load(os.path.join("asset/Cutie/14.png")),
         pygame.image.load(os.path.join("asset/Cutie/15.png")),
         pygame.image.load(os.path.join("asset/Cutie/16.png")),
         pygame.image.load(os.path.join("asset/Cutie/17.png")),
         pygame.image.load(os.path.join("asset/Cutie/18.png")),
         pygame.image.load(os.path.join("asset/Cutie/19.png")),
         pygame.image.load(os.path.join("asset/Cutie/20.png")),
         pygame.image.load(os.path.join("asset/Cutie/21.png")),
         pygame.image.load(os.path.join("asset/Cutie/22.png")),
         pygame.image.load(os.path.join("asset/Cutie/23.png")),
         pygame.image.load(os.path.join("asset/Cutie/24.png")),
         pygame.image.load(os.path.join("asset/Cutie/25.png")),
         pygame.image.load(os.path.join("asset/Cutie/26.png")),
         pygame.image.load(os.path.join("asset/Cutie/27.png")),
         pygame.image.load(os.path.join("asset/Cutie/28.png"))]

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

class HaziqSaya:
    X_Position = 80
    Y_Position = 310
    Y_Pos_Duck = 327
    Jump_Velocity = 8.5

    def __init__(self):
        self.duck_img = Ducking
        self.run_img = Running
        self.jump_img = Jumping

        self.haziq_duck = False
        self.haziq_run = True
        self.haziq_jump = False

        self.step_index = 0
        self.jump_vel = self.Jump_Velocity
        self.image = self.run_img[0]
        self.haziq_rect = self.image.get_rect()
        self.haziq_rect.x = self.X_Position
        self.haziq_rect.y = self.Y_Position

    def update(self, userInput):
        if self.haziq_duck:
            self.duck()
        if self.haziq_run:
            self.run()
        if self.haziq_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_SPACE] and not self.haziq_jump:
            self.haziq_duck = False
            self.haziq_run = False
            self.haziq_jump = True
        elif userInput[pygame.K_DOWN] and not self.haziq_jump:
            self.haziq_duck = True
            self.haziq_run = False
            self.haziq_jump = False
        elif not (self.haziq_jump or userInput[pygame.K_DOWN]):
            self.haziq_duck = False
            self.haziq_run = True
            self.haziq_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.haziq_rect = self.image.get_rect()
        self.haziq_rect.x = self.X_Position
        self.haziq_rect.y = self.Y_Pos_Duck
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.haziq_rect = self.image.get_rect()
        self.haziq_rect.x = self.X_Position
        self.haziq_rect.y = self.Y_Position
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.haziq_jump:
            self.haziq_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.Jump_Velocity:
            self.haziq_jump = False
            self.jump_vel = self.Jump_Velocity

    def draw(self, Screen):
        Screen.blit(self.image, (self.haziq_rect.x, self.haziq_rect.y))

class Cute:
    X_Positions = 300
    Y_Positions = 10

    def __init__(self):
        self.cute_img = Cutie

        self.cute_animate = True

        self.step_index = 0
        self.image = self.cute_img[0]
        self.cute_rect = self.image.get_rect()
        self.cute_rect.x = self.X_Positions
        self.cute_rect.y = self.Y_Positions

    def update(self, userInput):
        if self.cute_animate:
            self.animate()

        if self.step_index >= 140:
            self.step_index = 0

    def animate(self):
        self.image = self.cute_img[self.step_index // 5]
        self.cute_rect = self.image.get_rect()
        self.cute_rect.x = self.X_Positions
        self.cute_rect.y = self.Y_Positions
        self.step_index += 1

    def draw(self, Screen):
        Screen.blit(self.image, (self.cute_rect.x, self.cute_rect.y))

class Cloud2:
    def __init__(self):
        self.x = Screen_Width + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = Cloud
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = Screen_Width + random.randint(2500, 3000)
            self.y = random.randint(50, 50)

    def draw(self, Screen):
        Screen.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = Screen_Width

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, Screen):
        Screen.blit(self.image[self.type], self.rect)

class SmallTree(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class LargeTree(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 322

class UFO2(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image,self.type)
        self.rect.y = 184
        self.index = 0

    def draw(self, Screen):
        if self.index >= 9:
            self.index = 0
        Screen.blit(self.image[self.index//5], self.rect)
        self.index += 1

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = HaziqSaya()
    cloud = Cloud2()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 420
    points = 0
    font = pygame.font.SysFont('calibri', 20)
    obstacles = []
    deathCount = 0

    def score():
        global  points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed +=1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        Screen.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = Track.get_width()
        Screen.blit(Track, (x_pos_bg, y_pos_bg))
        Screen.blit(Track, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            Screen.blit(Track, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        Screen.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(Screen)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallTree(ObstacleSmall))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeTree(ObstacleBig))
            elif random.randint(0, 2) == 2:
                obstacles.append((UFO2(UFO)))

        for obstacle in obstacles:
            obstacle.draw(Screen)
            obstacle.update()
            if player.haziq_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                deathCount += 1
                menu(deathCount)

        background()

        cloud.draw(Screen)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()

def menu(deathCount):
    global  points
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        Screen.fill((255, 255, 255))
        font = pygame.font.SysFont('calibri', 30)
        font2 = pygame.font.SysFont('calibri', 20)

        if deathCount == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
            inst = font2.render("Instruction: Press Space for jumping and down arrow for ducking. Please get 2000 points to get the gift", True, (0,0,0))
            instRect = inst.get_rect()
            instRect.center = (Screen_Width // 2, 350)
            Screen.blit(inst, instRect)
        elif deathCount > 0:
            if points < 2000:
                text = font.render("Press any Key to Start", True, (0, 0, 0))
                score = font.render("Your Score: " + str(points), True, (0, 0, 0))
                scoreRect = score.get_rect()
                scoreRect.center = (Screen_Width // 2, Screen_Height // 2 + 50)
                Screen.blit(score, scoreRect)
            else:
                Win()


        textRect = text.get_rect()
        textRect.center = (Screen_Width // 2, Screen_Height // 2)
        Screen.blit(text, textRect)
        Screen.blit(Running[0], (Screen_Width // 2 - 20, Screen_Height // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                main()
def Win():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        Screen.fill((255, 255, 255))
        font = pygame.font.SysFont('calibri', 30)
        font2 = pygame.font.SysFont('calibri', 20)

        text2 = font.render("Yeay you winnn!!", True, (0, 0, 0))
        textRect2 = text2.get_rect()
        textRect2.center = (Screen_Width // 2, 200)
        Screen.blit(text2, textRect2)
        score = font2.render("Your Score is > 2000",  True, (0, 0, 0))
        scoreRect = score.get_rect()
        scoreRect.center = (Screen_Width // 2, 250)
        Screen.blit(score, scoreRect)


        Mouse_Pos = pygame.mouse.get_pos()
        Greet = font.render("I have something for you hihi. Click button below!", True, (0, 0, 0))

        GreetRect = Greet.get_rect()
        GreetRect.center = (Screen_Width // 2, 300)
        Screen.blit(Greet, GreetRect)

        # button
        Click = Button(image=pygame.image.load("asset/Others/button.png"), pos=(Screen_Width // 2, 400),
                       text_input="Here's the gift", font=font, base_color="Black", hovering_color="Red")

        Click.changeColor(Mouse_Pos)
        Click.update(Screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Click.checkForInput(Mouse_Pos):
                    Gift()
        pygame.display.update()


def Gift():
    mixer.music.load("asset/Others/untuk haziq.wav")
    mixer.music.set_volume(1)
    mixer.music.play(-1)
    run = True
    font = pygame.font.SysFont('calibri', 30)
    font2 = pygame.font.SysFont('calibri', 11)
    clock = pygame.time.Clock()
    cutiepie = Cute()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        Screen.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        cutiepie.draw(Screen)
        cutiepie.update(userInput)

        clock.tick(15)

        Greet = font.render("Saya laa hadiahnya hihi!!", True, (0, 0, 0))

        GreetRect = Greet.get_rect()
        GreetRect.center = (Screen_Width // 2, 550)
        Screen.blit(Greet, GreetRect)

        text = font2.render("*Please use headphone", True, (0, 0, 0))

        TextRect = text.get_rect()
        TextRect.center = (Screen_Width // 2, 570)
        Screen.blit(text, TextRect)

        pygame.display.update()

def Sad():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        #Mouse_Pos = pygame.mouse.get_pos()

        Screen.fill((255, 255, 255))
        font = pygame.font.SysFont('calibri', 30)

        Greet = font.render("Sampai Hati :( ", True, (0, 0, 0))

        GreetRect = Greet.get_rect()
        GreetRect.center = (Screen_Width // 2, Screen_Height // 2)
        Screen.blit(Greet, GreetRect)
        pygame.display.update()

def secondPage():
    clock = pygame.time.Clock()
    FPS = 60

    Image = pygame.image.load(os.path.join("asset/Others/sheshawaotao2.png"))
    Image = pygame.transform.scale_by(Image, 0.1)

    chars = "_.,-=+:;cba|?0123456789$W#@"

    pygame.init()

    def map_to_range(value, from_x, from_y, to_x, to_y):
        return value * (to_y - to_x) / (from_y - from_x)

    def text(msg, size = 11):
        return pygame.font.SysFont('consolas', size).render(msg, True, (255, 255, 255))

    def imageToAscii(image: pygame.Surface):
        w, h = text('A').get_size()
        surf = pygame.Surface(((image.get_width() - 1) * 13 + w, (image.get_height() - 1) * 13 + h))
        image.lock()
        for i in range(image.get_width()):
            for j in range(image.get_height()):
                r, g, b, _ = image.get_at([i, j])
                k = (r + g + b) / 3
                index = round(map_to_range(k, 0, 255, 5, len(chars) - 1))
                t = text(chars[index])
                surf.blit(t, (i * 13, j * 13))
                # pygame.display.update()
        image.unlock()
        return surf

        # button
    def main_game():
        ascii_image = imageToAscii(Image)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            Mouse_Pos = pygame.mouse.get_pos()

            Screen.fill((255, 255, 255))
            Screen.blit(ascii_image,(0, 0))
            #pygame.display.update()
            clock.tick(FPS)

            font = pygame.font.SysFont('calibri', 30)
            Ques = font.render("Awak recognize tak ascii code atas tulis apa?", True, (0, 0, 0))

            QuesRect = Ques.get_rect()
            QuesRect.center = (Screen_Width // 2, 250)
            Screen.blit(Ques, QuesRect)

            YesBt = Button(image=pygame.image.load("asset/Others/button.png"), pos=(300, 350), text_input="Yess. Ok next game!",
                           font=font, base_color="Black", hovering_color="Red")
            NoBt = Button(image=pygame.image.load("asset/Others/button.png"), pos=(800, 350), text_input="Nope, I don't know",
                          font=font, base_color="Black", hovering_color="Red")

            #for button in [YesBt, NoBt]:
            for button in [YesBt, NoBt]:
                button.changeColor(Mouse_Pos)
                button.update(Screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if YesBt.checkForInput(Mouse_Pos):
                        menu(deathCount=0)
                    if NoBt.checkForInput(Mouse_Pos):
                        Sad()

            pygame.display.update()
    main_game()

def firstPage():
    run = True
    while run:
        Mouse_Pos = pygame.mouse.get_pos()

        Screen.fill((255, 255, 255))
        font = pygame.font.SysFont('calibri', 30)

        Greet = font.render("Hi Haziq Saya <3", True, (0, 0, 0))
        Ques = font.render("I have something for you but first, let's play game!", True, (0, 0, 0))

        GreetRect = Greet.get_rect()
        GreetRect.center = (Screen_Width // 2, 100)
        Screen.blit(Greet, GreetRect)

        QuesRect = Ques.get_rect()
        QuesRect.center = (Screen_Width // 2, 150)
        Screen.blit(Ques, QuesRect)
        #pygame.display.update()
        #button
        YesBt = Button(image= pygame.image.load("asset/Others/button.png"), pos=(300, 300), text_input= "Okay awak hihi", font = font, base_color = "Black", hovering_color="Red" )
        NoBt = Button(image= pygame.image.load("asset/Others/button.png") , pos=(800, 300), text_input= "Taknak laa", font = font, base_color = "Black", hovering_color="Red")

        for button in [YesBt, NoBt]:
            button.changeColor(Mouse_Pos)
            button.update(Screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if YesBt.checkForInput(Mouse_Pos):
                    secondPage()
                if NoBt.checkForInput(Mouse_Pos):
                    Sad()

        pygame.display.update()

#secondPage()
#menu(deathCount = 0)
Gift()
#firstPage()
#Win()