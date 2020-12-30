from tkinter import *
from PIL import Image, ImageTk
import time
from settings import *
from objects import *
from game import*

tk = Tk()

tk.title(GAME_NAME)
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)

canvas = Canvas(tk, width=WIDTH, height=HEiGHT, highlightthickness=0)
back_ground = ImageTk.PhotoImage(Image.open('image.png').resize((WIDTH, HEiGHT)))
canvas.create_image(WIDTH / 2, HEiGHT / 2, image=back_ground)

canvas.pack()
tk.update()

paddle = Paddle(canvas, COLOR_PADDLE, PADDLE_WIDTH, PADDLE_HEIGHT)
score = Score(canvas, COLOR_SCORE, FONT_SIZE)
ball = Ball(canvas, paddle, score, COLOR_BAll, BALL_WIDTH, BALL_HEIGHT)
game = Game(canvas, score, COLOR_END_TEXT, SIZE_END_TEXT)

game.game_run(ball, paddle, tk, COLOR_END_TEXT)
