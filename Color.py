from manim import *

class C(Scene):
    def construct(self):
        a=ValueTracker(0)
        square=always_redraw(lambda:(Square(side_length=100)).set_color(color='#'+3*f"0+{a}"))
        a.increment_value(1)
        self.add(square)
        self.play(a.animate.set_value(9),runtime=5)