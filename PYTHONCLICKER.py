#pgzero
import random

WIDTH = 1500
HEIGHT = 900

TITLE = "Dungeons & Dragons"
FPS = 30

#objetos
background = Actor("background")
background.scale = 2.0
char = Actor('char',(150,650))
char.scale = 1.0
enemy = Actor('enemy',(1200,650))
enemy.scale = 0.5
bonus_1 = Actor('bonus_1',(200,150))
bonus_1.scale = 0.5
bonus_2 = Actor('bonus_1',(200,360))
#pode ter problema aqui sksksksk
button_menu = Actor('bonus_1',(750,500))
button_menu.scale = 0.1
button_game = Actor("bonus_1", (750, 280))
button_game.scale = 0.15
button_gallery = Actor("bonus_1", (750, 580))
button_gallery.scale = 0.15
win = Actor('win')
win.scale = 0.5

#coleçao
enemy_gallery = Actor('enemy', (300, 400))
enemy_gallery.scale = 2.0
enemy_2 = Actor('enemy_2', (500, 400))
enemy_2.scale = 0.5
enemy_3 = Actor('enemy_3', (700, 400))
enemy_3.scale = 0.5
enemy_4 = Actor('enemy_4', (900, 400))
enemy_4.scale = 0.5
enemy_5 = Actor('enemy_5', (1200, 400))
enemy_5.scale = 0.5
enemy_6 = Actor('enemy_6', (1100, 400))
enemy_6.scale = 0.5                                      

#recompensas
price1 = 15
price2 = 200
game_win = False

#variáveis
count = 0
hp = 100
damage = 1
mode = 'menu'

#graficos
def draw():
    global hp, game_win

    screen.clear()

    if mode == 'game':

        background.draw()
        char.draw()
        enemy.draw()

        #vida/pontos
        screen.draw.text(str(hp), center=(1200,450), color="#DC143C", fontsize=50, background="#FFE4B5")
        screen.draw.text(str(count), center=(1450,100), color="black", fontsize=70)

        #bonus
        bonus_1.draw()
        screen.draw.text("1 de dano a cada 3s", center=(200,130), color="black", fontsize=25)
        screen.draw.text(str(price1), center=(200,170), color="black", fontsize=30)

        bonus_2.draw()
        screen.draw.text("5 pontos a cada 3s", center=(200,340), color="black", fontsize=25)
        screen.draw.text(str(price2), center=(200,380), color="black", fontsize=30)

        #tela de vitória
        if game_win:
            win.draw()
            screen.draw.text("Parabéns, você derrotou todos os dragões!", center=(750,150), color="black", fontsize=60)
            button_menu.draw()
            screen.draw.text("Voltar ao menu", center=(750,500), color="black", fontsize=70)

    elif mode == 'menu':

        win.draw()

        button_game.draw()
        screen.draw.text("Jogar", center=(750,280), color="black", fontsize=25)

        button_gallery.draw()
        screen.draw.text("coleção", center=(750,580), color="black", fontsize=25)

    elif mode == 'collection':

        win.draw()

        enemy_gallery.draw()
        enemy_2.draw()
        enemy_3.draw()
        enemy_4.draw()
        enemy_5.draw()


#logica do jogo
def update(dt):
    global hp, game_win

    if mode != "game":
        return

    if game_win:
        return

    if hp <= 0 and enemy.image == "enemy":
        hp = 10
        enemy.image = "enemy_2"

    elif hp <= 0 and enemy.image == "enemy_2":
        hp = 10
        enemy.image = "enemy_3"

    elif hp <= 0 and enemy.image == "enemy_3":
        hp = 10
        enemy.image = "enemy_4"

    elif hp <= 0 and enemy.image == "enemy_4":
        hp = 10
        enemy.image = "enemy_5"

    elif hp <= 0 and enemy.image == "enemy_5":
        game_win = True


#funçoes dos bonus
def for_bonus_1():
    global hp
    hp -= 1


def for_bonus_2():
    global count
    count += 5


#mouse
def on_mouse_down(button, pos):
    global count, damage, hp, price1, price2, game_win, mode

    if game_win:
        if button_menu.collidepoint(pos):
            reset_game()
        return

    if button == mouse.LEFT:

        if mode == "game":

            if enemy.collidepoint(pos):
                count += 1
                hp -= damage

                if hp < 0:
                    hp = 0

                enemy.y = 700
                animate(enemy, tween="bounce_end", duration=0.5, y=650)

            elif bonus_1.collidepoint(pos):
                if count >= price1:
                    clock.schedule_interval(for_bonus_1,3)
                    count -= price1
                    price1 *= 2

            elif bonus_2.collidepoint(pos):
                if count >= price2:
                    clock.schedule_interval(for_bonus_2,3)
                    count -= price2
                    price2 *= 2

        elif mode == "menu":

            if button_game.collidepoint(pos):
                mode = "game"

            elif button_gallery.collidepoint(pos):
                mode = "collection"


def reset_game():
    global hp, count, game_win, mode

    hp = 100
    count = 0
    enemy.image = "enemy"
    game_win = False
    mode = "menu"
