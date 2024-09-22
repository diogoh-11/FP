# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()

    # Use t.up(), t.down() and t.goto(x, y)

    # Put your code here
    coordenadas = open("drawing.txt", 'r')
    for line in coordenadas:

        if line.strip() == "UP":
            t.up()

        elif line.strip() == "DOWN":
            t.down()

        else:
            comando = (line.split())
            t.goto(int(comando[0]), int(comando[1]))

    # Wait until window is closed
    screen.mainloop()


if __name__ == "__main__":
    main()

