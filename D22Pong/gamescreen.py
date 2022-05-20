from turtle import Screen

class GameScreen(Screen):
    def __init__(self):
        super().__init__()
        self.setup(width=700, height=700)
        self.bgcolor('black')
        self.title('PingPong')
