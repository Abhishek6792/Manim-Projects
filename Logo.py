from manim import *
        
class Logo(Scene):
    def construct(self):
        self.camera.background_color = '#fdd8b7'
        l=MathTex("i ",'\in ',"\mathbb{C}",color=BLACK)
        L=MathTex("i","\mathbb{C}",'\phi',r"\int",r"\forall", "h",
                  r"\in","\mathcal{D}","\mathbb{R}","\phi","\mathbb{N}",color=BLACK)
        L[3].scale_to_fit_height(0.65)

        lL=VGroup(l,L).scale(2)   #scaling for appropriate resolutions
         
        L[3].next_to(L[2],buff=0.05),L[4:6].next_to(L[3],buff=0.05)
        L[6].next_to(L[5],buff=0.05),L[7:].next_to(L[6],buff=0.05)
        L.move_to(ORIGIN)
        L[5].set_color(GREEN_D),L[7].set_color(RED)
        L[2].set_color(DARK_BLUE),L[-2].set_color(DARK_BLUE)

        self.wait()
        self.play(Write(l),run_time=1.5)

        self.play(l[0].animate.move_to(L[0]),
        l[1].animate.move_to(L[6]),
        l[2].animate.move_to(L[1]),run_time=2)

        self.play(Write(VGroup(L[2:6],L[7:])),run_time=2)
        self.wait()