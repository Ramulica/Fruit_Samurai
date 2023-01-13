import tkinter as tk
import os
import random



def move_object_to_right():
    """
    function f(x) = y = -a * x ** 2 + k
    :return:
    """
    global x, a, h, final_poz, fruit, fruit_image_l, angle, y, y_m, x_m

    y = -a * x ** 2 + h
    if y > -100:
        fruit.place_configure(x=int(x) + 400, y=1000 - int(y))

        if final_poz > 0:
            x += 10
        else:
            x -= 10
        root.after(18, move_object_to_right)
    else:
        x = -random.choice([item for item in range(-500, -300)] + [item for item in range(300, 500)])
        y = 1000
        final_poz = -x
        h = random.choice(range(800, 1000))
        a = h / (x ** 2)
        angle = 0
        fruit = tk.Label(root, image=random.choice(fruit_image_l), bg="#DA990F")
        fruit.place_configure(x=int(x) + 400, y=1000)
        root.after(1000, move_object_to_right)



def move_object_to_right_2():
    """
    function f(x) = y = -a * x ** 2 + k
    :return:
    """
    global x_2, a_2, h_2, final_poz_2, fruit_2, fruit_image_l, x_m, y_m

    y_2 = -a_2 * x_2 ** 2 + h_2
    if y_2 > -100:
        fruit_2.place_configure(x=int(x_2) + 425, y=1000 - int(y_2))
        if final_poz_2 > 0:
            x_2 += 10
        else:
            x_2 -= 10

        root.after(18, move_object_to_right_2)
    else:
        x_2 = -random.choice([item for item in range(-500, -300)] + [item for item in range(300, 500)])
        final_poz_2 = -x_2
        h_2 = random.choice(range(800, 1000))
        a_2 = h_2 / (x_2 ** 2)
        fruit_2 = tk.Label(root, image=random.choice(fruit_image_l), bg="#DA990F")
        fruit_2.place_configure(x=int(x) + 400, y=1000)
        root.after(3000, move_object_to_right_2)







# 1st fruit
y = 1000
x_m, y_m = 0, 0
angle = 0
x = -random.choice([item for item in range(-500, -300)] + [item for item in range(300, 500)])
final_poz = -x
h = random.choice(range(800, 1000))
a = h / (x ** 2)


# 2nd fruit
angle_2 = 0
x_2 = -random.choice([item for item in range(-500, -300)] + [item for item in range(300, 500)])
final_poz_2 = -x_2
h_2 = random.choice(range(800, 1000))
a_2 = h_2 / (x_2 ** 2)



root = tk.Tk()
root.geometry("1000x1000")
root.configure(bg="#DA990F")


main_path = os.getcwd()
os.chdir('images')
watermelon_image = tk.PhotoImage(file="watermelon.png")
watermelon_top_image = tk.PhotoImage(file="watermelon_top.png")
watermelon_bot_image = tk.PhotoImage(file="watermelon_bot.png")
apple_image = tk.PhotoImage(file="apple.png")
lemon_image = tk.PhotoImage(file="Lemon.png")
bomb_image = tk.PhotoImage(file="Bomb.png")
os.chdir(main_path)
fruit_image_l = [watermelon_image, apple_image, lemon_image, bomb_image]


fruit = tk.Label(root, image=watermelon_image, bg="#DA990F")
fruit.place(x=300, y=1000)

fruit_2 = tk.Label(root, image=watermelon_image, bg="#DA990F")
fruit_2.place(x=300, y=1000)

button = tk.Button(root, text="press", command=lambda: [move_object_to_right(), move_object_to_right_2()])
button.place(x=100, y=100)



root.mainloop()