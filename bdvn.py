import turtle


win = turtle.Screen()
win.title("Vietnam map by Thanh Tung")
win.setup(width=800, height=800)


win.addshape("pen2.gif")  
pen = turtle.Turtle()
pen.shape("pen2.gif")
pen.speed(1)
pen.penup()


with open('vietnam.txt', 'r') as file:
    vietnams = file.readlines()

pen.color('red', 'red')
count = 0
for vietnam in vietnams:
    viet = vietnam.strip().split()
    if len(viet) == 2:
        pen.goto(float(viet[0]), float(viet[1]))
        if count == 0:
            pen.pendown()
            pen.begin_fill()
        count += 1

pen.end_fill()
pen.penup()

# Vẽ ngôi sao vàng
with open('saovang.txt', 'r') as file:
    saovangs = file.readlines()

pen.color("yellow", "yellow")
count = 0
for sao in saovangs:
    s = sao.strip().split()
    if len(s) == 2:  # Kiểm tra số lượng phần tử
        pen.goto(float(s[0]), float(s[1]))
        if count == 0:
            pen.pendown()
            pen.begin_fill()
        count += 1
pen.end_fill()
pen.penup()

# Vẽ các đảo từ tệp cacdao.txt
pen.color('red', 'red')
pen.pensize(2)
with open('cacdao.txt', 'r') as file:
    cacdao = file.readlines()

count = 0
for dao in cacdao:
    count += 1
    d = dao.strip().split()
    if len(d) == 2:  # Kiểm tra số lượng phần tử
        pen.goto(float(d[0]), float(d[1]))
        if count % 7 == 1:
            pen.pendown()
            pen.begin_fill()
        if count % 7 == 0:
            pen.end_fill()
            pen.penup()

pen.penup()

# Thêm tên các quần đảo Hoàng Sa và Trường Sa
pen.color('blue')  # Màu chữ

# Vẽ tên Hoàng Sa
pen.goto(200, 0)  # Tọa độ thử nghiệm cho Hoàng Sa
pen.write("Quần đảo\nHOÀNG SA", align="center", font=("Arial", 16, "bold"))

# Vẽ tên Trường Sa
pen.goto(200, -180)  # Tọa độ thử nghiệm cho Trường Sa
pen.write("Quần đảo\nTRƯỜNG SA", align="center", font=("Arial", 16, "bold"))

pen.color('red')
pen.goto(-50, -360)  # Tọa độ thử nghiệm cho Trường Sa
pen.write("HOÀNG SA, TRƯỜNG SA LÀ CỦA VIỆT NAM", align="center", font=("Arial", 16, "bold"))


pen.hideturtle()

# Đợi người dùng đóng cửa sổ
win.mainloop()