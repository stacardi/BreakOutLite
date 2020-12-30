import time
class Game:
    def __init__(self, canvas, score, color_end_text, size_end_text):
        self.canvas = canvas
        self.color_end_text = color_end_text
        self.size_end_text = size_end_text
        self.score = score

        self.game_started = False
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)
        self.ball_hit_bottom = False

    def start_game(self, event):
        self.game_started = True
    
    def game_over(self):
        self.canvas.create_text(250, 120, text='Game over :(', font=('Courier', self.size_end_text), fill='red')
    

    
    def game_run(self, ball, paddle, tk, COLOR_END_TEXT):
        i = 10
        while not self.ball_hit_bottom:
            if self.game_started == True:
                ball.draw(COLOR_END_TEXT)
                paddle.draw()
            
            if self.score.score == i:
                if i <= 30:
                    ball.more_speed()
                    paddle.more_speed()
                    i += 10

            tk.update_idletasks()
            tk.update()

            time.sleep(0.01)
            self.ball_hit_bottom = ball.hit_bottom
        self.game_over()
        tk.update_idletasks()
        tk.update()
        time.sleep(3)
    