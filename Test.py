from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

class Resume(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        logo=SVGMobject('D:\Manim_projects\python-logo-only.svg')
        logo[0].rotate(angle=180*DEGREES)
        logo[0].set_color_by_gradient(['#306998','#5a9fd4']).rotate(-180*DEGREES)
        logo[1].rotate(angle=180*DEGREES)
        logo[1].set_color_by_gradient(['#ffd43b','#ffe873']).rotate(-180*DEGREES)

        txt=Text("python",font="Flux",color='#646464',stroke_width=0,
                 stroke_color="#646464",font_size=50).next_to(logo,RIGHT)
        self.play(Write(logo),run_time=5)
        self.play(Write(txt),run_time=1)
        self.wait()
class img(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        s_1=SVGMobject('D:\Manim_projects\svg_1.svg',stroke_width=0.0).scale_to_fit_height(height=self.camera.frame_height())
        s_2=SVGMobject('D:\Manim_projects\svg_2.svg')        
        self.play(Write(s_1),run_time=5)
        #self.play(Write(s_2))
        self.wait()
class Name(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        name=Text("ABHISHEK PRASAD",color=BLACK).scale(1.275).move_to(UP+4*RIGHT)
        self.play(Write(AddTextLetterByLetter(name),run_time=2.5))
        self.wait(1)
        self.play(FadeOut(name))

class Quiz(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        name=Text("Quiz",color=BLACK,font='Consolas').scale(4).move_to(UP+4*RIGHT)
        self.play(Create(name),run_time=2.5)
        self.wait(1)
        self.play(FadeOut(name))

class Greet(Scene):
    def construct(self):
        self.camera.background_color = "#c4de97"
        name=Tex("Thank You",color=BLACK).scale(5)
        self.play(Write(name),run_time=2.5)
        self.wait(1)
        self.play(FadeOut(name))

class Lan(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        name_1=Tex("English",color=BLACK).scale(1.275).move_to(UP+4*RIGHT)
        name_2=Tex("Hindi",color=BLACK).scale(1.275).move_to(UP+4*RIGHT).next_to(name_1,DOWN)
        name_3=Tex("Bengali",color=BLACK).scale(1.275).move_to(UP+4*RIGHT).next_to(name_2,DOWN)
        self.play(Write(name_1),Write(name_2),Write(name_3),run_time=2)
        self.wait(1)
        self.play(Unwrite(name_1),Unwrite(name_2),Unwrite(name_3))
class SurfaceExample(ThreeDScene):
    def construct(self):
        surface = Surface(
            lambda x, y: np.array([x, y, np.sin(x + y)]),
            u_range=(-5, 5),
            v_range=(-5, 5),
            checkerboard_colors=[],
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.add(surface)
    

class IntersectionSurfaces(ThreeDScene):
    def construct(self):
        # Define the surfaces as functions
        def surface1(x, y):
            return x**2 + y**2

        def surface2(x, y):
            return np.sqrt(x**2 + y**2)

        # Create 3D axes
        axes = ThreeDAxes()

        # Create the surfaces
        surface1_graph = self.get_surface(surface1, color=BLUE)
        surface2_graph = self.get_surface(surface2, color=RED)

        # Add surfaces and axes to the scene
        self.add(axes, surface1_graph, surface2_graph)

        # Find the points of intersection
        intersection_points = []
        resolution = 100  # Adjust this for smoother intersection

        for x in np.linspace(-3, 3, resolution):
            for y in np.linspace(-3, 3, resolution):
                if abs(surface1(x, y) - surface2(x, y)) < 0.1:
                    intersection_points.append((x, y, max(surface1(x, y), surface2(x, y))))

        # Create points at the intersection
        intersection_dots = [Dot(point=(x, y, z), color=YELLOW) for x, y, z in intersection_points]

        # Animate the intersection dots
        self.play(*[Create(dot) for dot in intersection_dots])

        # Wait for a few seconds to observe the result
        self.wait(5)

    def get_surface(self, func, color):
        surface = Surface(
            lambda u, v: np.array([u, v, func(u, v)]),
            u_range=[-3,3],v_range=[-3,3],
            resolution=(20, 20),
            checkerboard_colors=[color, color]
        )
        return surface

class GridUnderFunction(Scene):
    def construct(self):
        # Create the number plane
        plane = NumberPlane()

        # Create the function graph
        function_graph = self.get_function_graph()

        # Add the plane and graph to the scene
        self.add(plane, function_graph)

        # Play the animation
        self.wait(2)

    def get_function_graph(self):
        # Define the function you want to plot
        func = lambda x: np.sin(x)

        # Create the graph
        graph = FunctionGraph(func, x_range=[-5,5])

        # Set the color and style of the graph
        graph.set_color(RED)
        graph.set_stroke(width=2)

        return graph


class rect(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.add(text)
        self.play(ShowPassingFlash(SurroundingRectangle(text)))

class Proof(Scene):
    def construct(self):
        self.camera.background_color = '#fdd8b7'
        f,g=r"f\left(x\right)",r"g\left(x\right)"
        u,v="u","v"
        def color_code_formula(x):
            for i in range(len(x)):
                if x[i].get_tex_string()==u or x[i].get_tex_string()==f:
                    x[i].set_color(PURE_RED)
                elif x[i].get_tex_string()==v or x[i].get_tex_string()==g:
                    x[i].set_color(DARK_BLUE)
                    
        template=TexTemplate()
        template.add_to_preamble(r"\usepackage{mathtools}")
        self.wait()
        heading=Tex("Integration By Parts",color=BLACK,stroke_width=0.1)
        FORMULA=MathTex(r"\int",f,g,r"dx",r"=",f,r"\int",g,r"dx-\int{\left(\frac{d}{dx}",f,
                        r"\int",g,r"dx\right)}dx",color=BLACK)
        self.play(Write(heading),run_time=2)
        self.play(heading[0].animate.move_to([0,3,0]))
        color_code_formula(FORMULA)
        self.play(Write(FORMULA),run_time=(5))
        self.wait()
        self.play(FadeOut(FORMULA,heading))

class Proof(VoiceoverScene):
    def construct(self):
        self.camera.background_color = '#fdd8b7'
        self.set_speech_service(CoquiService(model_name="tts_models/en/ljspeech/tacotron2-DDC_ph",
                                             transcription_model="base"))
        self.add_voiceover_text("Q e d")

class IBP(ThreeDScene,VoiceoverScene):
    def construct(self):
        self.camera.background_color = '#fdd8b7'
        self.set_speech_service(CoquiService())
   
        heading=Tex("Integration By Parts","?",color=BLACK,stroke_width=0.1)
        
        with self.voiceover(text='Integration By Parts. What is it?'):
            self.play(Write(heading),run_time=2)
            
        self.play(
            Unwrite(heading[1],run_time=0.5),
            heading[0].animate.move_to([0,3,0])
            )
        f,g=r"f\left(x\right)",r"g\left(x\right)"
        formula_0=MathTex(r"\int_{ }^{ }",f,g,r"dx",color=BLACK)
        formula_0[1].set_color(PURE_RED)
        formula_0[2].set_color(DARK_BLUE)
        formula_0.scale(0.9)
        
        formula_1=MathTex(r"\int",f,g,r"dx",r"=",f,r"\int",g,r"dx-\int\frac{d}{dx}",r"\left(",f,r"\right)",
                        r"\left(\int",g,r"dx\right)dx",color=BLACK)
        formula_1.scale(0.9)
        for i in (1,5,10):
            formula_1[i].set_color(PURE_RED)
        for i in (2,7,-2):
            formula_1[i].set_color(DARK_BLUE)
            
        formula=VGroup(formula_0,formula_1)   
         
        with self.voiceover(text="Its a formula or method for finding the integral of product of two functions."):
            self.wait(3)
            self.play(Write(formula[0].scale(2).move_to(ORIGIN)),run_time=2)
        
        self.play(formula[0].animate.scale(0.5).move_to(formula[1][0:4]))
            
        with self.voiceover(text="Its formula looks something like this."):
            self.play(Write(formula[1][4::]), run_time=3)
        

        
        with self.voiceover(text="""It kindof looks scary, if you are seeing it for the first time.
                            The goal of this vedio, is to have a visual and intuitive idea
                            of each components in the formula.A DISCLAIMER before starting, the 
                            visual understanding of the formula does not actually help while solving
                            a integral of products of two funtions. The reason for making a vedio on
                            this formula is just for fun and a love for intuitive understanding of 
                            Mathematics. So I hope by the end of the vedio, you could see the each 
                            term of the big formula inside your head.
                            """):
            self.wait(2)