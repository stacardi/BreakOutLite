import random


class Ball:
    def __init__(self, canvas, paddle, score, color, ball_width, ball_height):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.hit_bottom = False
        self.id = canvas.create_oval(10, 10, ball_width, ball_height, fill=color)
        self.canvas.move(self.id, 250, 100)
        self.speed_increased = 1
        

        starts = [-2, -1, 1, 2]
        random.shuffle(starts)

        self.x = starts[0]
        self.y = -2

        self.a = 1
        self.b = -1

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]:
                self.score.add_point()
                return True
        return False

    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = self.a

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        if self.hit_paddle(pos) == True:
            self.y = self.b

        if pos[0] <= 0:
            self.x = self.a

        if pos[2] >= self.canvas_width:
            self.x = self.b

    def more_speed(self):
        self.b = self.b * 2
        self.a = self.a * 2
        

class Paddle:

    def __init__(self, canvas, color, paddle_width, paddle_height):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, paddle_width, paddle_height, fill=color)

        start_1 = [40, 60, 120, 150, 180, 200]
        random.shuffle(start_1)

        self.start_pos_x = start_1[0]

        self.canvas.move(self.id, self.start_pos_x, 300)

        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        self.a = 2
        self.b = -2


        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)

    def turn_right(self, event):
        self.x = self.a

    def turn_left(self, event):
        self.x = self.b

    def start_game(self, event):
        self.game_started = True

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    
    def more_speed(self):
        self.b = self.b * 2
        self.a = self.a * 2

class Score:
    def __init__(self, canvas, color, font_size):
        self.canvas = canvas
        self.score = 0
        self.margin_top = (font_size - 10)
        self.id = canvas.create_text(450, self.margin_top, text=self.score, font=('Courier', font_size), fill=color)

    def add_point(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)