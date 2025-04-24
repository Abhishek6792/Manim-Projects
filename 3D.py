from manim import *


class Proj_Line(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(60*DEGREES,30*DEGREES,zoom=1)
        #self.begin_ambient_camera_rotation(rate=0.7)
        L=8
        axes=ThreeDAxes(x_range=[-L,L,1],y_range=[-L,L,1],z_range=[-L+3,L-3,1],
        x_length=2*L,y_length=2*L,z_length=2*(L-3))

        self.add(axes)
        t=ValueTracker(0)
        l=3

        
        plane_0=Surface(lambda u,v: axes.c2p(0,u,v),
            u_range=[0,l],
            v_range=[0,l],
            resolution=1,
            fill_color=WHITE,
            checkerboard_colors= [WHITE, WHITE],
            fill_opacity= 0.7,
            stroke_color=None,
        )

        vp=MathTex('VP',stroke_width=0.5,stroke_color=BLACK).scale(0.7)
        vp.rotate(angle=PI/2,axis=UP).rotate(angle=PI/2,axis=RIGHT).move_to((l-0.5)*(UP+OUT))

        plane_1=always_redraw(lambda : Surface(
            lambda u,v : axes.c2p(u, v,(-u*np.sin((PI/2)*t.get_value()))/np.cos((PI/2)*t.get_value())),
            u_range=[0,l*np.cos((PI/2)*t.get_value())],
            v_range=[0,l],
            resolution=1,
            fill_color=WHITE,
            checkerboard_colors= [WHITE, WHITE],
            fill_opacity= 0.7,
            stroke_color=None,
        ))

        hp=always_redraw(lambda : MathTex('HP',stroke_width=0.5,stroke_color=BLACK).scale(0.7).
        rotate(PI/2,OUT).move_to((l-0.5)*(UP+np.cos(t.get_value()*PI/2)*RIGHT-np.sin(t.get_value()*PI/2)*OUT)))
        
        always_redraw(lambda:hp.rotate(angle=t.get_value()*PI/2,axis=UP))

        plane_2=always_redraw(lambda : Surface(
            lambda u,v : axes.c2p(u,(-u*np.sin((PI/2)*t.get_value()))/np.cos((PI/2)*t.get_value()),v),
            u_range=[0,l*np.cos((PI/2)*t.get_value())],
            v_range=[0,l],
            resolution=1,
            fill_color=WHITE,
            checkerboard_colors= [WHITE, WHITE],
            fill_opacity= 0.7,
            stroke_color=None,
        ))
        

        self.add(t)
        self.play(Write(plane_0),Write(vp),run_time=1.5)
        self.play(Write(plane_1),Write(hp),run_time=1.5)
        self.play(Write(plane_2),run_time=1.5)
        self.play(t.animate.set_value(1),t.animate.set_value(1),run_time=5)
        #self.stop_ambient_camera_rotation()
        self.wait()
        self.move_camera(phi=PI/2,theta=0,run_time=3)
        self.wait()