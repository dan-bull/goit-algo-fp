import turtle
import math

def draw_tree(t, branch_length, level, angle):
    if level == 0:
        return

    # Намалювати гілку
    t.forward(branch_length)

    # Ліва гілка
    t.left(angle)
    draw_tree(t, branch_length * math.cos(math.radians(angle)), level - 1, angle)

    # Повернутися назад
    t.right(2 * angle)
    draw_tree(t, branch_length * math.cos(math.radians(angle)), level - 1, angle)

    # Повернутися в початкове положення
    t.left(angle)
    t.backward(branch_length)

def main():
    # Запитати у користувача рівень рекурсії
    recursion_level = int(input("Вкажіть рівень рекурсії: "))

    # Налаштування turtle
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Повернути turtle вертикально вгору

    # Почати малювати дерево
    draw_tree(t, 100, recursion_level, 30)

    # Завершити малювання
    screen.mainloop()

if __name__ == "__main__":
    main()
