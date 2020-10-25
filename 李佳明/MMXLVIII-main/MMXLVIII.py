import turtle, random


class BackGround(turtle.Turtle):  # 定义一个类，用来画除了数字方块之外的图形
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()

    def draw_block(self):
        self.shape('bg.gif')  # 画出背景方块
        for i in allpos:
            self.goto(i)
            self.stamp()
    def judge(self):  # 游戏失败及达成2048的提示文字
        global flag_win, flag_win_lose_text
        self.color('red')
        judge = 0  # 判断是否还有位置可以移动
        for i in block_dic.values():
            for j in block_dic.values():
                if i.num == 0 or i.num == j.num and i.distance(j) == 100:
                    judge += 1
        if judge == 0:  # 无位置可移动，游戏失败
            self.write('☠☠☠☠☠\n☠☠☠☠☠\n☠☠☠☠☠', align='center', font=('Segoe UI Emoji', 30, 'bold'))
            flag_win_lose_text = False
        if flag_win is True:  # 此条件让2048达成的判断只能进行一次
            for k in block_dic.values():
                if k.num == 2048:  # 游戏达成
                    flag_win = False
                    self.write('♥♥♥♥♥\n♥♥♥♥♥', align='center', font=('Segoe UI Emoji', 30, 'bold'))
                    flag_win_lose_text = False

    def win_lose_clear(self):  # 游戏失败及达成2048提示文字clear
        global flag_win_lose_text
        self.clear()
        flag_win_lose_text = True
class Block(turtle.Turtle):  # 数字方块类
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.num = 0

    def draw(self):
        self.clear()
        dic_draw = {2: '#80C3C0', 4: '#19A1AF', 8: '#2590B0',
                    16: '#117399', 32: '#16547F', 64: '#3300CC',
                    128: '#000099', 256: '#FF6699', 512: '#CC6699',
                    1024: '#FF3366', 2048: '#990033'}
        if self.num > 0:  # 数字大于0，画出方块
            self.color(f'{dic_draw[self.num]}')  # 选择颜色
            self.begin_fill()
            self.goto(self.xcor()+48, self.ycor()+48)   #a+48,a+48
            self.goto(self.xcor()-96, self.ycor())      #a-48,a+48
            self.goto(self.xcor(), self.ycor()-96)      #a-48,a-48
            self.goto(self.xcor()+96, self.ycor())      #a+48,a-48
            self.goto(self.xcor(), self.ycor()+96)      #a+48,a+48
            self.end_fill()
            self.goto(self.xcor()-48, self.ycor()-68)   #a,a-20
            if self.num > 1:  # 按照数字选择数字的颜色
                self.color('white')
            self.write(f'{self.num}', align='center', font=('华文琥珀', 27, 'bold'))
            self.goto(self.xcor(), self.ycor()+20)      #a，a


class Game():
    def init(self):
        back = BackGround()   # 实例画出游戏的背景
        back.draw_block()
        for i in allpos:  # 画出16个海龟对应16个数字块
            block = Block()
            block.goto(i)
            block_dic[i] = block
        game.grow()

    def restart(self):  # 重开游戏的方法
        global score, flag_win_lose_text
        score = 0
        for i in block_dic.values():
            i.num = 0
            i.clear()
        win_lose_text.clear()
        game.grow()
        flag_win_lose_text = True  # 此flag为游戏达成或失败出现提示语后的判断，要提示语被clear后才能继续move

    def grow(self):  # 随机出现一个2或4的数字块
        block_list = []
        for i in allpos:
            if block_dic[i].num == 0:
                block_list.append(block_dic[i])  # 挑出空白方块的海龟
        turtle_choice = random.choice(block_list)  # 随机选中其中一个海龟
        turtle_choice.num = random.choice([2, 2, 2, 2, 4])  # 赋属性num=2/4
        turtle_choice.draw()
        win_lose_text.judge()
        ms.update()

    def move_up(self):
        allpos1 = allpos[::4]  # 切片为四列
        allpos2 = allpos[1::4]
        allpos3 = allpos[2::4]
        allpos4 = allpos[3::4]
        self.move_move(allpos1, allpos2, allpos3, allpos4)

    def move_down(self):
        allpos1 = allpos[-4::-4]
        allpos2 = allpos[-3::-4]
        allpos3 = allpos[-2::-4]
        allpos4 = allpos[-1::-4]
        self.move_move(allpos1, allpos2, allpos3, allpos4)

    def move_left(self):
        allpos1 = allpos[:4]
        allpos2 = allpos[4:8]
        allpos3 = allpos[8:12]
        allpos4 = allpos[12:16]
        self.move_move(allpos1, allpos2, allpos3, allpos4)

    def move_right(self):
        allpos1 = allpos[-1:-5:-1]
        allpos2 = allpos[-5:-9:-1]
        allpos3 = allpos[-9:-13:-1]
        allpos4 = allpos[-13:-17:-1]
        self.move_move(allpos1, allpos2, allpos3, allpos4)

    def move_move(self, allpos1, allpos2, allpos3, allpos4):
        if flag_win_lose_text is True:
            count1 = self.move(allpos1)  # 四列或四行依次移动
            count2 = self.move(allpos2)
            count3 = self.move(allpos3)
            count4 = self.move(allpos4)
            if count1 or count2 or count3 or count4:  # 判断是否有方块移动，有才能继续出现新的数字块
                self.grow()

    def move(self, pos_list):
        num_list = []  # 为某一列或行的数字块海龟的坐标
        for i in pos_list:
            num_list.append(block_dic[i].num)  #  把这些海龟的NUM形成list
        new_num_list, count = self.list_oper(num_list)  #  只是list_oper的方法形成新的list
        for j in range(len(new_num_list)):  # 把新的list依次赋值给对应的海龟.num属性并调用draw()方法
            block_dic[pos_list[j]].num = new_num_list[j]
            block_dic[pos_list[j]].draw()
        return count

    def list_oper(self, num_list):  # num_list的操作，假设其为【2,0,2,2】
        global score
        count = True
        temp = []
        new_temp = []
        for j in num_list:
            if j != 0:
                temp.append(j)  # temp=[2,2,2]
        flag = True
        for k in range(len(temp)):
            if flag:
                if k < len(temp)-1 and temp[k] == temp[k+1]:
                    new_temp.append(temp[k]*2)
                    flag = False
                    score += temp[k]
                else:
                    new_temp.append(temp[k])  # new_temp=[4,2]
            else:
                flag = True
        for i in range(len(num_list)-len(new_temp)):
            new_temp.append(0)  # new_temp=[4,2,0,0]
        if new_temp == num_list:
            count = False  # 此变量判断num_list没有变化，数字块无移动
        return(new_temp, count)


if __name__ == '__main__':
    ms = turtle.Screen()  # 主窗口的设置
    ms.setup(430, 430, 400, 50)
    ms.bgcolor('white')
    ms.title('MMXLVIII')
    ms.tracer(0)
    ms.register_shape('bg.gif')
    block_dic = {}  # 放数字方块海龟的字典，位置坐标为key,对应海龟为value
    allpos = [(-150, 150), (-50, 150), (50, 150), (150, 150),
              (-150, 50), (-50, 50), (50, 50), (150, 50),
              (-150, -50), (-50, -50), (50, -50), (150, -50),
              (-150, -150), (-50, -150), (50, -150), (150, -150)]
    flag_win = True  # 达成2048的判断，让达成的文字仅出现一次
    flag_win_lose_text = True  # 用来判断失败或成功的提示文字是否有被清除，不清除不能继续移动方块
    score = 0
    win_lose_text = BackGround()
    game = Game()
    game.init()

    ms.listen()
    ms.onkey(game.move_up, 'Up')
    ms.onkey(game.move_down, 'Down')
    ms.onkey(game.move_left, 'Left')
    ms.onkey(game.move_right, 'Right')
    ms.onkey(win_lose_text.win_lose_clear, 'Return')
    ms.onkey(game.restart, 'space')

    ms.mainloop()

