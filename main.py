import tkinter as tk
import os
import random


def move_object_to_right():
    """
    function f(x) = y = -a * x ** 2 + k
    :return:
    """
    global x, a, h, final_poz, fruit, fruit_image_l, y, condition, fruit_image, bomb, bomb_status

    y = -a * x ** 2 + h
    if y > -100 and condition == "whole":
        fruit.place_configure(x=int(x) + 400, y=1000 - int(y))

        if final_poz > 0:
            x += 10
        else:
            x -= 10
        root.after(18, move_object_to_right)
    elif condition == "whole":
        x = -random.choice([item for item in range(-500, -300)] + [item for item in range(300, 500)])
        y = 1000
        final_poz = -x
        h = random.choice(range(800, 1000))
        a = h / (x ** 2)
        condition = "whole"

        fruit_image = random.choice(fruit_image_l)
        if fruit_image == bomb_image:
            bomb = True
            bomb_status = 'start'
        else:
            bomb = False
        fruit = tk.Label(root, image=fruit_image, bg="#DA990F")
        fruit.place_configure(x=int(x) + 400, y=1000)
        root.after(10, move_object_to_right)


def half_fruit_falling():
    global x, y, fruit_bot, fruit_top, final_poz, h, a, condition, x_r, fruit, fruit_image, bomb, bomb_status
    if 1000 - int(y) < 1200:
        x += 5
        x_r -= 5
        y -= 20
        fruit_top.place(x=x_r + 400, y=1000 - int(y))
        fruit_bot.place(x=x + 400, y=1000 - int(y) + 98)
        root.after(18, half_fruit_falling)
    else:
        fruit_top.destroy()
        fruit_bot.destroy()
        x = -random.choice([item for item in range(-500, -300)] + [item for item in range(300, 500)])
        y = 1000
        final_poz = -x
        h = random.choice(range(800, 1000))
        a = h / (x ** 2)
        condition = "whole"

        fruit_image = random.choice(fruit_image_l)
        if fruit_image == bomb_image:
            bomb = True
            bomb_status = 'start'
        else:
            bomb = False
        fruit = tk.Label(root, image=fruit_image, bg="#DA990F")
        fruit.place_configure(x=int(x) + 400, y=1000)
        root.after(10, move_object_to_right)


def label_hover(event):
    global condition, x, y, fruit_bot, fruit_top, x_r, score, bomb, heart_left, heart_right, heart_l_x, heart_l_y, \
        heart_r_x, heart_r_y, lives
    if condition == "whole" and bomb:
        condition = 'cut'
        fruit.place_configure(y=1400)
        boom_lv_1()
        heart_left.place(y=50, x=400)
        heart_right.place(y=60, x=500)
        heart_l_x = -100
        heart_l_y = 950
        heart_r_x = 0
        heart_r_y = 960

        root.after(500, lose_heart_animation)
        lives -= 1
        root.title(f"YOUR SCORE: {score}        YOUR LIVES: {'❤' * lives}")
    elif condition == "whole":
        score += 1
        root.title(f"YOUR SCORE: {score}        YOUR LIVES: {'❤' * lives}")
        fruit.place_configure(y=1400)
        condition = 'cut'
        fruit_top = tk.Label(root, image=get_image(fruit_image)[0], bg="#DA990F", borderwidth=0)
        fruit_bot = tk.Label(root, image=get_image(fruit_image)[1], bg="#DA990F", borderwidth=0)
        fruit_top.place(x=x + 400, y=1000 - int(y))
        fruit_bot.place(x=x + 400, y=1000 - int(y) + 98)
        x_r = x
        half_fruit_falling()


def get_image(main_image):
    list_of_images = [[watermelon_image, watermelon_top_image, watermelon_bot_image],
                      [lemon_image, lemon_top_image, lemon_bot_image],
                      [apple_image, apple_top_image, apple_bot_image]]
    for item in list_of_images:
        if item[0] == main_image:
            return item[1], item[2]
    else:
        return bomb_image, bomb_image

def boom_lv_1():
    global x, y, bomb_status, explosion
    explosion.destroy()
    if bomb_status == 'start':
        x += 50

    explosion = tk.Label(root, image=explosion_lv_1, borderwidth=0)
    explosion.place(x=int(x) + 400, y=1000 - int(y))
    if bomb_status == 'start':
        x -= 30
        root.after(10, boom_lv_2)
    else:
        explosion.destroy()
        print('gata')


def boom_lv_2():
    global x, y, bomb_status, explosion
    explosion.destroy()
    explosion = tk.Label(root, image=explosion_lv_2, borderwidth=0)
    explosion.place(x=int(x) + 400, y=1000 - int(y))
    if bomb_status == 'start':
        x -= 30
        root.after(18, boom_lv_3)
    else:
        x += 30
        root.after(18, boom_lv_1)


def boom_lv_3():
    global x, y, bomb_status, explosion
    explosion.destroy()
    explosion = tk.Label(root, image=explosion_lv_3, borderwidth=0)
    explosion.place(x=int(x) + 400, y=1000 - int(y))
    if bomb_status == 'start':
        x -= 30
        root.after(18, boom_lv_4)
    else:
        x += 30
        root.after(18, boom_lv_2)


def boom_lv_4():
    global x, y, bomb_status, explosion
    explosion.destroy()
    explosion = tk.Label(root, image=explosion_lv_4, borderwidth=0)
    explosion.place(x=int(x) + 400, y=1000 - int(y))
    if bomb_status == 'start':
        x -= 30
        root.after(18, boom_lv_5)
    else:
        x += 30
        root.after(18, boom_lv_3)


def boom_lv_5():
    global x, y, bomb_status, explosion
    explosion.destroy()
    explosion = tk.Label(root, image=explosion_lv_5, borderwidth=0)
    explosion.place(x=int(x) + 400, y=1000 - int(y))
    if bomb_status == 'start':
        x -= 30
        root.after(18, boom_lv_6)
    else:
        x += 30
        root.after(18, boom_lv_4)


def boom_lv_6():
    global x, y, bomb_status, explosion
    explosion.destroy()
    explosion = tk.Label(root, image=explosion_lv_6, borderwidth=0)
    explosion.place(x=int(x) + 400, y=1000 - int(y))
    bomb_status = "finish"
    x += 30
    root.after(18, boom_lv_5)


def lose_heart_animation():
    global heart_left, heart_right, heart_l_x, heart_l_y, heart_r_x, heart_r_y, condition, x, y, fruit_bot, fruit_top, \
        final_poz, h, a, condition, x_r, fruit, fruit_image, bomb, bomb_status, lives
    if heart_r_x < 320:
        heart_r_x += 10
        heart_r_y = -0.01 * (heart_r_x ** 2) + 960
        heart_right.place(x=int(heart_r_x) + 500, y=1000 - int(heart_r_y))
        heart_l_x -= 10
        heart_l_y = -0.01 * (heart_l_x ** 2) + 960
        heart_left.place(x=int(heart_l_x) + 500, y=1000 - int(heart_l_y))
        root.after(18, lose_heart_animation)
    else:
        if lives != 0:
            x = -random.choice([item for item in range(-500, -300)] + [item for item in range(300, 500)])
            y = 1000
            final_poz = -x
            h = random.choice(range(800, 1000))
            a = h / (x ** 2)
            condition = "whole"

            fruit_image = random.choice(fruit_image_l)
            if fruit_image == bomb_image:
                bomb = True
                bomb_status = 'start'
            else:
                bomb = False
            fruit = tk.Label(root, image=fruit_image, bg="#DA990F")
            fruit.place_configure(x=int(x) + 400, y=1000)
            root.after(10, move_object_to_right)
        else:
            print("game over")
def start_game():
    global game_stage
    root.bind('<Enter>', label_hover)


root = tk.Tk()
root.geometry("1000x1000")
root.configure(bg="#DA990F")


main_path = os.getcwd()
os.chdir('images')
watermelon_image = tk.PhotoImage(file="watermelon.png")
watermelon_top_image = tk.PhotoImage(file="watermelon_top.png")
watermelon_bot_image = tk.PhotoImage(file="watermelon_bot.png")
apple_image = tk.PhotoImage(file="apple.png")
apple_top_image = tk.PhotoImage(file="apple_top.png")
apple_bot_image = tk.PhotoImage(file="apple_bot.png")
lemon_image = tk.PhotoImage(file="Lemon.png")
lemon_top_image = tk.PhotoImage(file="Lemon_top.png")
lemon_bot_image = tk.PhotoImage(file="Lemon_bot.png")
bomb_image = tk.PhotoImage(file="Bomb.png")
heart_left_image = tk.PhotoImage(file="heart_l.png")
heart_right_image = tk.PhotoImage(file="heart_r.png")
explosion_lv_1 = tk.PhotoImage(file="explosion_lv_1.png")
explosion_lv_2 = tk.PhotoImage(file="explosion_lv_2.png")
explosion_lv_3 = tk.PhotoImage(file="explosion_lv_3.png")
explosion_lv_4 = tk.PhotoImage(file="explosion_lv_4.png")
explosion_lv_5 = tk.PhotoImage(file="explosion_lv_5.png")
explosion_lv_6 = tk.PhotoImage(file="explosion_lv_6.png")
os.chdir(main_path)


fruit_image_l = [watermelon_image, apple_image, lemon_image, bomb_image]

game_stage = 'menu'
score = 0

# 1st fruit
x_r = 0
y = 1000
fruit_image = random.choice(fruit_image_l)
if fruit_image == bomb_image:
    bomb = True
    bomb_status = 'start'
else:
    bomb = False
x = -random.choice([item for item in range(-500, -300)] + [item for item in range(300, 500)])
final_poz = -x
h = random.choice(range(800, 1000))
a = h / (x ** 2)
condition = 'whole'
heart_l_x = -100
heart_l_y = 950
heart_r_x = 0
heart_r_y = 960
lives = 3
root.title(f"YOUR SCORE: {score}        YOUR LIVES: {'❤' * lives}")


fruit = tk.Label(root, image=fruit_image, bg="#DA990F")
fruit_top = tk.Label(root, image=get_image(fruit_image)[0], bg="#DA990F", borderwidth=0)
fruit_bot = tk.Label(root, image=get_image(fruit_image)[1], bg="#DA990F", borderwidth=0)
explosion = tk.Label(root, image=explosion_lv_2, borderwidth=0)
heart_left = tk.Label(root, image=heart_left_image, borderwidth=0)
heart_right = tk.Label(root, image=heart_right_image, borderwidth=0)
fruit.place(x=300, y=1000)

fruit_2 = tk.Label(root, image=watermelon_image, bg="#DA990F")
fruit_2.place(x=300, y=1000)


button = tk.Button(root, text="press", command=lambda: [move_object_to_right(), button.destroy(), start_game()])
button.place(x=100, y=100)




root.mainloop()