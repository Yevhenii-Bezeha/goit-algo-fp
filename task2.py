import turtle
import math


def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return

    t.forward(branch_length)
    t.left(45)
    draw_pythagoras_tree(t, branch_length / math.sqrt(2), level - 1)

    t.right(90)
    draw_pythagoras_tree(t, branch_length / math.sqrt(2), level - 1)

    t.left(45)
    t.backward(branch_length)


def main():
    level = int(input("Enter recursion depth: "))
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.goto(0, -200)
    t.down()

    draw_pythagoras_tree(t, 100, level)

    screen.mainloop()


if __name__ == "__main__":
    main()
