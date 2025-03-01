class Monkey:
    def __init__(self):
        self.on_box = False

    def push_box(self):
        print("Monkey pushes the box.")
        self.on_box = True

    def grab_bananas(self):
        if self.on_box:
            print("Monkey grabs the bananas!")
        else:
            print("Monkey can't reach the bananas.")

monkey = Monkey()
monkey.push_box()
monkey.grab_bananas()