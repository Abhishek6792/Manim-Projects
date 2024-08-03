from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

class test(Scene):
    def construct(self):
        self.camera.background_color=GREY
        tan = MathTex(r"\tan(","15",r"^\circ)",r"\tan(","75",r"^\circ)").scale(1.5)
        tan[:3].shift(LEFT)
        tan[3:].shift(RIGHT)

        time=MathTex("75","-","15",r"\\=60\text{sec}",tex_environment="align*").scale(1.5)

        self.play(Write(tan))
        self.play(LaggedStart(
            AnimationGroup(
                tan.animate.to_edge(UP,buff=2),
                TransformFromCopy(tan[1],time[2]),
                TransformFromCopy(tan[4],time[0])),
            AnimationGroup(Write(time[1]),Write(time[-1])),lag_ratio=0.7)
        )
        self.wait(0.5)

        #tan(15)

        self.play(LaggedStart(FadeOut(time,tan[3:]),
                              tan[:3].animate.shift([-tan[:3].get_x(),0,0]),
                              lag_ratio=0.5))
        #triangle
        t=np.sqrt(np.tan(np.pi/12))

        A,B=Point([-t,0,0]),Point([t,0,0])
        C=Point([0,1/t,0])
        D=Point([t*np.sin(PI/3),np.sin(PI/12),0])
        points=Group(A,B,C,D)
        
        
        AB,BC,CA,AD=Line(A,B),Line(C,B),Line(C,A),Line(A,D)
        lines=VGroup(AB,BC,CA,AD)

        CAB=Angle(CA,AB,quadrant=(-1,1),other_angle=True,dot_radius=0,radius=0.25)
        ABC=Angle(AB,BC,quadrant=(-1,-1),other_angle=True,dot_radius=0,radius=0.25)
        BCA=Angle(BC,CA,other_angle=True,dot_radius=0)
        angles=VGroup(CAB,ABC,BCA)

        tri=Group(points,lines,angles).scale(4.5).shift(2*DOWN)

        A_label=MathTex("A").next_to(A,direction=0.5*DL)
        B_label=MathTex("B").next_to(B,direction=0.5*DR)
        C_label=MathTex("C").next_to(C,direction=0.5*UP)
        D_label=MathTex("D").next_to(D,direction=0.5*(UP*np.sin(np.radians(15))+RIGHT*np.cos(np.radians(15))))
        points_label=VGroup(A_label,B_label,C_label,D_label)

        ang_A=MathTex(r"75^\circ").next_to(A,direction=5*(UP*np.sin(np.radians(75/2))+RIGHT*np.cos(np.radians(75/2))))
        ang_B=MathTex(r"75^\circ").next_to(B,direction=5*(UP*np.sin(np.radians(75/2))+LEFT*np.cos(np.radians(75/2))))
        ang_C=MathTex(r"15^\circ").next_to(C,direction=8*DOWN)
        angle_lables= VGroup(ang_A,ang_B,ang_C)

        tri.add(points_label,angle_lables)
        self.play(AnimationGroup(Write(BC),Write(CA),GrowFromCenter(AB),run_time=2))
        self.add(tri[1:],points_label,angle_lables)
        self.play(Create(AD))


class final(VoiceoverScene):
    def construct(self):
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        self.set_speech_service(CoquiService(model_name="tts_models/en/vctk/vits", 
                                             transcription_model="medium", gpu=False))
        self.wait()
        with self.voiceover(text='''tan 15 degrees and tan 75 degrees in 60 seconds''') as tracker:
            tan = MathTex(r"\tan(","15",r"^\circ)",r"\tan(","75",r"^\circ)").scale(1.5)
            tan[:3].shift(LEFT)
            tan[3:].shift(RIGHT)

            time=MathTex("75","-","15",r"\\=60\text{sec}",tex_environment="align*").scale(1.5)

            self.play(Write(tan))
            self.play(LaggedStart(
                AnimationGroup(
                    tan.animate.to_edge(UP,buff=2),
                    TransformFromCopy(tan[1],time[2]),
                    TransformFromCopy(tan[4],time[0])),
                AnimationGroup(Write(time[1]),Write(time[-1])),lag_ratio=0.7)
            )
            self.wait(0.5)

            #tan(15)

            self.play(LaggedStart(FadeOut(time,tan[3:]),
                                  tan[:3].animate.shift([-tan[:3].get_x(),0,0]),
                                  lag_ratio=0.5))
        #triangle
        t=np.sqrt(np.tan(np.pi/12))

        A,B=Point([-t,0,0]),Point([t,0,0])
        C=Point([0,1/t,0])
        D=Point([t*np.sin(PI/3),np.sin(PI/12),0])
        points=Group(A,B,C,D)

        AB,BC,CA,AD=Line(A,B),Line(C,B),Line(C,A),Line(A,D)
        lines=VGroup(AB,BC,CA,AD)

        CAB=Angle(CA,AB,quadrant=(-1,1),other_angle=True,dot_radius=0,radius=0.25)
        ABC=Angle(AB,BC,quadrant=(-1,-1),other_angle=True,dot_radius=0,radius=0.25)
        BCA=Angle(BC,CA,other_angle=True,dot_radius=0)
        angles=VGroup(CAB,ABC,BCA)

        tri=Group(points,lines,angles).scale(4.5).shift(2*DOWN)

        A_label=MathTex("A").next_to(A,direction=0.5*DL)
        B_label=MathTex("B").next_to(B,direction=0.5*DR)
        C_label=MathTex("C").next_to(C,direction=0.5*UP)
        D_label=MathTex("D").next_to(D,direction=0.5*(UP*np.sin(np.radians(15))+RIGHT*np.cos(np.radians(15))))
        points_label=VGroup(A_label,B_label,C_label,D_label)

        ang_A=MathTex(r"75^\circ").next_to(A,direction=5*(UP*np.sin(np.radians(75/2))+RIGHT*np.cos(np.radians(75/2))))
        ang_B=MathTex(r"75^\circ").next_to(B,direction=5*(UP*np.sin(np.radians(75/2))+LEFT*np.cos(np.radians(75/2))))
        ang_C=MathTex(r"15^\circ").next_to(C,direction=8*DOWN)
        angle_lables= VGroup(ang_A,ang_B,ang_C)

        tri.add(points_label,angle_lables)
        
        with self.voiceover(text='''Make an isoceles triangle with the equal sides being of length 2, 
                            and equal angles being 75 degrees. Therefore the remaining angle will 
                            be, 180 minus, 75 plus 75, that is 30 degrees. Lets name it as A,B,C''') as tracker:
            #make triangle with MathTex 2 and angles and vertex_label
            self.play(Write(lines[:-1]))
            brace_BC=Brace(BC,RIGHT)
            length_BC=MathTex("2").next_to(brace_BC,direction=RIGHT)
            
            brace_CA=Brace(CA,LEFT)
            length_CA=MathTex("2").next_to(brace_CA,direction=LEFT)

            temp=VGroup(brace_BC,length_BC,brace_CA,length_CA)
            self.play(Write(temp))

            self.play(AnimationGroup(Write(CAB),Write(ABC),Write(ang_A),Write(ang_B)))

            self.play(Write(BCA),Write(ang_C))
            self.wait()
        with self.voiceover(text='''Now, drop a prependicular from A on the side B,C. Lets 
                            call the intersection as D. In triangle A, D, C, angle A, D, C is 90 
                            degrees and angle D, C, A is 30 degrees which means the remaining angle 
                            C, A, D will be 60 degrees, which makes the triangle A, D, C a 30, 60, 90 
                            right triangle.''') as tracker:
            self.wait()
# Run the scene with custom configurations
config.frame_width = 9
config.frame_height = 16
config.pixel_width = 720  # Adjust as needed
config.pixel_height = 1280  # Adjust as needed