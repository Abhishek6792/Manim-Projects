from manim import *

class tan(Scene):
    def construct(self):
        self.camera.background_color = '#fdd8b7'
        t=np.sqrt(np.tan(PI/12))

        # POINTS 
        A,B,C=[(-t),0,0],[t,0,0],[0,(1/t),0]
        D,E=[t*np.sin(PI/3),np.sin(PI/12),0],[-2*np.cos(PI/12)+t,np.sin(PI/12),0]

        vertices=(A,B,C)

        Triangle=Polygon(*vertices,stroke_color=DARK_BLUE,
        stroke_opacity=1.0,stroke_width=10)
        
        # ANGLES
        ang_kwrargs={'radius':0.2,'color':BLACK,'stroke_width':8}
        ABC=Angle(Line(B,C),Line(B,A),**ang_kwrargs)
        CAB=Angle(Line(A,B),Line(A,C),**ang_kwrargs)
        BCA=Angle(Line(C,A),Line(C,B),**ang_kwrargs)
        ang=VGroup(ABC,CAB,BCA)

        #TEXT
        A_t,V_A_t=MathTex("A",color=BLACK).scale(0.7),MathTex("75^{\circ}",color=BLACK)
        A_t.next_to(A,LEFT,buff=0.01)
        V_A_t.scale(0.3).next_to(A,np.cos(5*PI/24)*RIGHT+np.sin(5*PI/24)*UP,buff=0.22)

        B_t,V_B_t=MathTex("B",color=BLACK).scale(0.7),MathTex("75^{\circ}",color=BLACK)
        B_t.next_to(B,RIGHT,buff=0.01)
        V_B_t.scale(0.3).next_to(B,np.cos(5*PI/24)*LEFT+np.sin(5*PI/24)*UP,buff=0.22)

        C_t,V_C_t=MathTex("C",color=BLACK).scale(0.7),MathTex("15^{\circ}",color=BLACK)
        C_t.next_to(C,RIGHT+UP,buff=0.01)
        V_C_t.scale(0.25).next_to(C,DOWN,buff=0.3)

        Txt=VGroup(A_t,B_t,C_t)
        for i in Txt: i.scale(0.5)
        Txt.add(V_A_t,V_B_t,V_C_t)
        
        #TRIANGLE
        tri_mobj=VGroup(Triangle,ang,Txt).scale(6).shift(5*DOWN)
        

        brace_AC=BraceBetweenPoints((Triangle.get_vertices())[2],(Triangle.get_vertices())[0],color=BLACK)
        brace_BC=BraceBetweenPoints(Triangle.get_corner(RIGHT+DOWN),Triangle.get_corner(UP),color=BLACK)
        brace_AC_label=MathTex(r'2',color=BLACK).scale(2).next_to(brace_AC.get_center(),2*LEFT).shift(0.05*UP)
        brace_BC_label=MathTex(r'2',color=BLACK).scale(2).next_to(brace_BC.get_center(),2*RIGHT).shift(0.05*UP)
        
        #Speech
        speech=('Draw an isoceles triangle of equal',
        'side being 2 and equal angle being','75^{\circ}')
        s_1=Tex(speech[0],color=BLACK).scale(1.8).to_edge(edge=LEFT+30*DOWN)
        s_2=Tex(speech[1],color=BLACK).scale(1.8).to_edge(edge=LEFT+28*DOWN)
        


        #Rendered Part Code----------------------------------------
        self.wait
        #Writing Part
        self.play(Write(s_1))
        self.play(Write(s_2))
        self.play(Write(MathTex(speech[2],color=BLACK)
        .next_to(s_2,DOWN).shift(0.1*(UP+2*RIGHT)).scale(1.8).to_edge(edge=LEFT+26*DOWN)))

        #Creating
        self.play(Create(Triangle),run_time=5)
        self.play(Write(Txt[0:3]),run_time=3)
        self.play(Create(ang[0:2]),Write(Txt[0:2]),run_time=2)

        self.play(FadeIn(brace_AC),FadeIn(brace_BC),run_time=1)
        self.play(Write(brace_AC_label),Write(brace_BC_label))
        self.wait()
    