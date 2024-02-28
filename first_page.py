
# star = turtle.Turtle()
# star.penup()
# star.begin_fill()
# star.color("red", "white")
# star.end_fill()
# star.pendown()


# i in range(5):
#    star.forward(130)
#   star.right(144)

# pen = turtle.Turtle()
# pen.color("red")
# pen.pensize(5)
# pen.speed(15)
# for i in range(2):
#    pen.circle(120)
#    pen.left(50)


# yıldan doğum yılını çıkarma
def yas(birinci, ikinci):
    age = birinci - ikinci
    print(f'{age}')

yas(1000,1500)


# kuvvet alma
def kuvvet_al(taban, ust):
    sonuc=1
    for i in range(ust):
        sonuc*=taban
    print(f'{taban} ve {sonuc}')
kuvvet_al(3,2)

def mutlak(sayı):
    if(sayı<0):
        sayı=-sayı
    print(f'{sayı}')
mutlak(100)

# def asalSayılariBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)

# sayi1 = int(input('sayı 1:'))
# sayi2 = int(input('sayı 2:'))
# asalSayılariBul(sayi1, sayi2)

# def tamBolenleriBul(sayi, sayi2):
#     for sayi in range(sayi, sayi2):
#         if