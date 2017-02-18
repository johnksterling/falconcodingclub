import turtle


def interior_angle(num_sides):
    return (num_sides-2)*180/num_sides


def draw_shape(num_sides):
    angle = interior_angle(sides)
    for i in range(sides):
        color_index = i % 6
        t.pencolor(colors[color_index])
        t.forward(50)
        t.left(180-angle)

colors = ['light blue', 'blue', 'dark blue', 'purple', 'green', 'orange', 'red']
sides = int(input('How many sides?'))
t = turtle.Pen()
t.pendown()
for i in range(36):
    draw_shape(sides)
    t.right(10)
