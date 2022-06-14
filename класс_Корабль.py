class Dot:                             #обьявление координат
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):                  #проверка на равенство. возможность сравнивать
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"
    
class Ship:                #задаем координаты корабля через class Dot (bow), длину (l), горизонталь (o=0) или вертикаль (o=1)
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l): #в зависимости от указанной длины карабля (l) отработает цикл for и присвоит координаты x  и y
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:      # если заданный параметр o=0 то меняться будет координата x на единицу, т.е. наш корабль будет горизонтальным
                cur_x += i

            elif self.o == 1:    #если заданный параметр o=1 то меняться будет координата y на единицу, т.е. наш корабль будет вертикальным
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots
        
      def shooten(self, shot):  #вводим "выстрел". в shot будем указывает координату, в которую "стреляем" через заданный класс Dot
        return shot in self.dots
    
a=Ship(Dot(1,1),3,1)
print(a.dots)
print(a.shooten(Dot(2,5)))
