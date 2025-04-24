from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

class Banner(Scene):
    def construct(self):
        self.camera.background_color = '#fdd8b7'
        _1=MathTex(r"\epsilon",r"\in" ,r"\{",r"\varepsilon",",",r"\epsilon",r"\}",color=BLACK).scale(2.5)
        _2=Tex("An ","e","l","e","m","e","nt Of",color=BLACK).scale(2.5)
        self.play(Write(_1),run_time=2)
        self.play(
            AnimationGroup(
                ReplacementTransform(VGroup(_1[2],_1[4],_1[6]),VGroup(_2[0],_2[2],_2[4],_2[6:]),run_time=2),
                AnimationGroup(
                    _1[0].animate.move_to(_2[3]),
                    _1[1].animate.move_to(_2[1].copy().shift(0.075*UP)),
                    _1[3].animate.move_to(_2[5]),
                    _1[5].animate.move_to(_2[3])
                )
            )
        )
        self.wait()
        
class logo(Scene):
    def construct(self):
        self.camera.background_color = '#fdd8b7'
        self.add(MathTex(r"\in",color=BLACK).scale(14))
        
class Thumbnail(Scene):
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
        heading=Tex("Integration By Parts",color=BLACK).scale(3.1).move_to([0,3,0])
        FORMULA=MathTex(r"\int",f,g,r"dx",color=BLACK).scale(3).shift(0.5*DOWN)
        color_code_formula(FORMULA)
        self.add(heading,FORMULA)
class Proof(VoiceoverScene):
    def construct(self):
        self.camera.background_color = '#fdd8b7'
        self.set_speech_service(CoquiService(model_name="tts_models/en/ljspeech/tacotron2-DDC_ph",
                                             transcription_model="large"))
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
        with self.voiceover(text='''The purpose of this video is to give a short derivation of Integration by Parts.''') as tracker:
            heading=Tex("Integration By Parts",color=BLACK,stroke_width=0.1)
            FORMULA=MathTex(r"\int",f,g,r"dx",r"=",f,r"\int",g,r"dx-\int{\left({{d(",f,r")}\over{dx}}",
                        r"\int",g,r"dx\right)}dx",color=BLACK)
            self.play(Write(heading),run_time=2)
            self.play(heading[0].animate.move_to([0,3,0]))
            color_code_formula(FORMULA)
            self.play(Write(FORMULA),run_time=(tracker.duration-4))
            self.wait()
            self.play(FadeOut(FORMULA,heading))
             
        with self.voiceover(text="""So, lets first start by defining U OF X TO BE U AND V OF X TO BE V."""):
            U=MathTex(r"u\left(x\right)",r"\coloneqq", "u",color=BLACK,tex_template=template).to_edge(edge=5*LEFT+UP)
            V=MathTex(r"v\left(x\right)",r"\coloneqq", "v",color=BLACK,tex_template=template).to_edge(edge=5*RIGHT+UP)
            U[2].set_color(PURE_RED)
            V[2].set_color(DARK_BLUE)
            self.wait(2.5)
            self.play(Write(U))
            self.wait(0.5)
            self.play(Write(V))
            
        formula=MathTex(r"{{d",r"\left(",u,v,r"\right)}",r"\over{dx}}",
                          r"=",u,r"{{d",v,r"}\over{dx}}","+",v,
                          r"{{d",u,r"}\over{dx}}",color=BLACK).move_to(4*LEFT+2*UP)
        color_code_formula(formula)     
                       
        with self.voiceover(text="""The derivation interestingly begins with inverse of integration operation  
                            , that is by<bookmark mark='1'/> differentiating the product of U and V."""):
            
            self.wait_until_bookmark("1")                
            self.play(
                Write(formula[0:2],run_time=1),
                Write(formula[4:6],run_time=1),
                TransformFromCopy(U[2],formula[2],run_time=2),
                TransformFromCopy(V[2],formula[3],run_time=2)
                )
            
        with self.voiceover(text="""Now, expand the derivative of the product of the functions <bookmark mark='2'/>
                            using the Product Rule.<bookmark mark='u'/>For the first term, multiply U with the 
                            derivative of V.<bookmark mark='v'/> And for the second term, multiply V with the derivative of U."""):
            temp_1=Tex("Product Rule",color=BLACK).shift(2*UP+3*RIGHT).scale(2)
            self.wait_until_bookmark("2")
            self.play(Write(formula[6],run_time=2),Write(temp_1))
            self.wait()
            self.wait_until_bookmark("u")
            self.play(
                TransformFromCopy(formula[0],formula[8]),
                TransformFromCopy(formula[2],formula[7]),
                TransformFromCopy(formula[3],formula[9]),
                TransformFromCopy(formula[5],(formula[10])),
                run_time=2)
            self.wait_until_bookmark("v")
            self.play(
                FadeOut(temp_1),
                TransformFromCopy(formula[6],(formula[11])),
                TransformFromCopy(formula[0],formula[-3]),
                TransformFromCopy(formula[2],formula[-2]),
                TransformFromCopy(formula[3],formula[-4]),
                TransformFromCopy(formula[5],(formula[-1])),
                run_time=2)
            
        self.wait()
        with self.voiceover(text="And then <bookmark mark='3'/>integrate both sides with respect to X."):
            formula_1=MathTex(r"\int",r"\left(",r"{{d",r"\left(",u,v,r"\right)}",r"\over{dx}}",r"\right)","dx",
                            r"=",r"\int",r"\left({",u,r"{{d",v,r"}\over{dx}}","+",v,
                            r"{{d",u,r"}\over{dx}}}",r"\right)","dx",color=BLACK).next_to(formula,DOWN).shift( 1.2*RIGHT)
            color_code_formula(formula_1)    
            self.play(
                TransformFromCopy(formula[0:6],formula_1[2:8]),
                TransformFromCopy(formula[7:],formula_1[13:22]),
                TransformFromCopy(formula[6],formula_1[10])
            ) 
            self.wait_until_bookmark("3")
            self.play(
                Write(formula_1[0:2]),Write(formula_1[8:10]),
                Write(formula_1[11:13]),Write(formula_1[22:]),
                run_time=2                
            )
        with self.voiceover(text="""The left side will give us back the <bookmark mark='4'/>function itself, as 
                            integration and differentiation are inverses of each other. <bookmark mark='5'/>
                            For the right side, just leave it as it is<bookmark mark='6'/> after unpacking.
                            <bookmark mark='C'/> Also not forgetting the constant C. As you can see there is
                            <bookmark mark='minus'/> a negative sign before the constant, we are taking it as negative 
                            , so that we can change it to positive later on. And it doesn't really matter, since it 
                            is a constant anyway."""):
            formula_2=MathTex(u,v,r"=",r"{\int",u,r"{{d",v,r"}\over{dx}}","dx",
                              "+",r"{\int",v,r"{{d",u,r"}\over{dx}}}","dx","-","C_1",
                              color=BLACK).move_to(formula_1)
            color_code_formula(formula_2)
            self.play(ShowPassingFlash(always_redraw(lambda :SurroundingRectangle(formula_1[0:10],color=PINK))))

            self.wait_until_bookmark("4")
            self.play(
                ReplacementTransform(formula_1[4:6],formula_2[0:2]),
                FadeOut(formula_1[0:4],formula_1[6:10])
                )
            
            self.wait_until_bookmark("5")
            self.play(ShowPassingFlash(SurroundingRectangle(formula_1[11:],color=PINK)))

            self.wait_until_bookmark("6")
            self.play(
                ReplacementTransform(formula_1[10],formula_2[2]),
                TransformFromCopy(formula_1[11],formula_2[3]),
                ReplacementTransform(formula_1[13:17],formula_2[4:8]),
                TransformFromCopy(formula_1[23],formula_2[8]),
                ReplacementTransform(formula_1[17],formula_2[9]),
                ReplacementTransform(formula_1[11],formula_2[10]),
                ReplacementTransform(formula_1[18:22],formula_2[11:15]),
                ReplacementTransform(formula_1[23],formula_2[15]),
                FadeOut(formula_1[12],formula_1[22])
                )
            self.wait_until_bookmark("C")
            self.play(Write(formula_2[-2:]))
            self.wait_until_bookmark("minus")
            self.play(ShowPassingFlash(SurroundingRectangle(formula_2[-2],color=PINK)))
            self.play(formula_2.animate.move_to(ORIGIN))
            
        with self.voiceover(text="""Now re-arranging everything.""") as tracker:
            formula_3=MathTex(r"{\int",u,r"{{d",v,r"}\over{dx}}","dx",r"=",u,v,
                              "-",r"{\int",v,r"{{d",u,r"}\over{dx}}}","dx","+","C_1",
                              color=BLACK).move_to(formula_2)
            color_code_formula(formula_3)
            
            self.play(
                ReplacementTransform(formula_2[:2],formula_3[7:9]),
                ReplacementTransform(formula_2[2],formula_3[6]),
                ReplacementTransform(formula_2[3:9],formula_3[:6]),
                ReplacementTransform(formula_2[9],formula_3[9]),
                ReplacementTransform(formula_2[10:16],formula_3[10:16]),
                ReplacementTransform(formula_2[-2],formula_3[-2]),
                ReplacementTransform(formula_2[-1],formula_3[-1]),
            )

        with self.voiceover(text="""By swapping V with derivative of U<bookmark mark='term'/>.And substituting 
                            the value of U <bookmark mark='in'/>and derivative of V <bookmark mark='out'/>with F of 
                            X, and G of X respectively.The equation starts looking very similar 
                            <bookmark mark='formula'/>to our end result.
                            """):
            formula_copy=FORMULA.copy().next_to(formula_3,DOWN)
            formula_3_similar=MathTex(r"{\int",u,r"{{d",v,r"}\over{dx}}","dx",r"=",u,v,
                              "-",r"{\int",r"{{d",u,r"}\over{dx}}}",v,"dx","+","C_1",
                              color=BLACK).move_to(formula_3)
            color_code_formula(formula_3_similar)
            self.wait_until_bookmark("term")
            self.play(
                ReplacementTransform(formula_3[:11],formula_3_similar[:11]),
                ReplacementTransform(formula_3[11],formula_3_similar[14]),
                ReplacementTransform(formula_3[12:15],formula_3_similar[11:14]),
                ReplacementTransform(formula_3[15:],formula_3_similar[15:])
                )
            formula_4=MathTex(r"{\int",f,g,"dx",r"=",f,v,
                              "-",r"{\int",r"{{d","(",f,r")",r"}\over{dx}}",v,"dx","+","C_1",
                              color=BLACK)
            color_code_formula(formula_4)
            

            U_f,V_g=MathTex(u,"=",f,color=BLACK),MathTex(r"{{d",v,r"}\over{dx}}","=",g,color=BLACK)
            for i in U_f,V_g:
                color_code_formula(i)
                
            U_f.shift([4,2.3,0])
            V_g.next_to(U_f,DOWN)
            self.wait_until_bookmark("in")
            self.play(Write(U_f[0]),Write(V_g[:3]))
            self.wait_until_bookmark("out")
            self.play(Write(U_f[1:]),Write(V_g[3:]))
            self.play(Unwrite(formula_3_similar[1:5]),Unwrite(formula_3_similar[7]),
                      Unwrite(formula_3_similar[12]))
            self.play(
                ReplacementTransform(formula_3_similar[0],formula_4[0]),
                ReplacementTransform(formula_3_similar[5],formula_4[3]),
                ReplacementTransform(formula_3_similar[6],formula_4[4]),
                ReplacementTransform(formula_3_similar[8:12],formula_4[6:10]),
                ReplacementTransform(formula_3_similar[13:],formula_4[13:])
                )
            list=[1,2,5,11]
            for i in range(4):
                if i==1:
                    self.play(TransformFromCopy(V_g[-1].copy(),formula_4[list[i]]),run_time=0.8)
                else:
                    if i==3:
                        self.play(Write(VGroup(formula_4[10],formula_4[12])),run_time=0.8)
                    self.play(TransformFromCopy(U_f[2].copy(),formula_4[list[i]]),run_time=0.8)
            self.wait_until_bookmark("formula")
            self.play(FadeIn(formula_copy))
            self.wait(2)
        with self.voiceover(text="""Our <bookmark mark='left'/>left side is completely done and for the right 
                            side we will solve for V in terms of <bookmark mark='g'/>G of X.
                            """):
            self.play(Unwrite(U),Unwrite(V),Unwrite(formula))
            self.wait_until_bookmark("left")
            self.play(ShowPassingFlashWithThinningStrokeWidth(SurroundingRectangle(formula_4[:5],color=PINK)))
            self.wait_until_bookmark("g")
            self.play(ShowPassingFlashWithThinningStrokeWidth(SurroundingRectangle(V_g[-1],color=PINK)))
            self.wait()
            self.play(FadeOut(formula_copy))
        
        with self.voiceover(text="""For solving V in terms of G. We will <bookmark mark='int'/>integrate both 
                            sides with respect to X. The <bookmark mark='left'/>left side will give us V back 
                            and the right side <bookmark mark='right'/>will be just in it's integral form. Many 
                            people after this step just substitue the V back, but we must not forget our 
                            <bookmark mark='const'/>constant which is obtained from solving the D V D X integral. 
                            So we will name it as<bookmark mark='two'/> C two, and THEN! substitute the entire value of V in the equation.  
                            """):
            formula_4_copy=formula_4.copy().to_edge(UP+LEFT)
            self.play(
                formula_4.animate.to_edge(UP+LEFT),
                Unwrite(U_f),
                V_g.animate.next_to(formula_4_copy,DOWN)
            )
            int_v=MathTex(r"\int",r"{{d",v,r"}\over{dx}}","dx","=",r"\int",g,"dx",color=BLACK).move_to(V_g)
            color_code_formula(int_v)
            self.wait_until_bookmark("int")
            self.play(
                ReplacementTransform(V_g[0:3],int_v[1:4]),
                ReplacementTransform(V_g[3],int_v[5]),
                ReplacementTransform(V_g[4],int_v[7]),
                Write(int_v[0]),Write(int_v[4]),Write(int_v[6]),Write(int_v[8])
            )
            v_as_g=MathTex(v,"=",r"\int",g,"dx","+","C","_2",color=BLACK).move_to(int_v)
            color_code_formula(v_as_g)
            
            self.wait_until_bookmark("left")
            self.play(ShowPassingFlashWithThinningStrokeWidth(SurroundingRectangle(int_v[0:5],color=PINK)))
            self.play(
                AnimationGroup(
                FadeOut(int_v[0:2],int_v[3:5]),
                ReplacementTransform(int_v[2],v_as_g[0]),
                lag_ratio=0.8)
            )
            self.wait_until_bookmark("right")
            self.play(ShowPassingFlashWithThinningStrokeWidth(SurroundingRectangle(int_v[6:],color=PINK)))
            self.play(
                ReplacementTransform(int_v[5:],v_as_g[1:5])
                )
            self.wait_until_bookmark("const")
            self.play(Write(v_as_g[5:7]))
            
            self.wait_until_bookmark("two")
            self.play(Write(v_as_g[7]))
            
            formula_5=MathTex(r"{\int",f,g,"dx",r"=",f,r"{\left(",r"\int",g,"dx","+","C","_2",r"\right)","-",
                              r"{\int",r"{{d","(",f,")",r"}\over{dx}}",r"{\left(",r"\int",g,"dx","+","C","_2",r"\right)",
                              "dx","+","C","_1",color=BLACK).scale(0.78)
            self.play(formula_4.animate.move_to(ORIGIN))
            color_code_formula(formula_5)
            self.play(
                AnimationGroup(
                    AnimationGroup(
                        ReplacementTransform(formula_4[0:6],formula_5[0:6]),
                        FadeOut(formula_4[6]),
                        ReplacementTransform(formula_4[7:14],formula_5[14:21]),
                        FadeOut(formula_4[14]),
                        ReplacementTransform(formula_4[15:],formula_5[29:])
                    ),AnimationGroup(Write(formula_5[6]),Write(formula_5[13]),Write(formula_5[21]),
                    Write(formula_5[28]))
                    ,lag_ratio=1.0
                )
            )
            self.play(
                ReplacementTransform(v_as_g.copy()[2:],formula_5[7:13]),
                ReplacementTransform(v_as_g[2:],formula_5[22:28]),
                FadeOut(v_as_g[:2])
            )
            self.play(formula_5.animate.shift(UP))
        with self.voiceover(text="""We are almost done with our derivation.Just a few cancellations left.
                            Now, we will expand each term seperately.The <bookmark mark='first'/>first term of our expression, will give 
                            the first term of our formula along with <bookmark mark='f_x'/>F of X times C two.
                            Similarly, the <bookmark mark='second'/>later term will give the last term of the formula along with 
                            <bookmark mark='complex_term'/> this term.
                            """):
            first_term=MathTex(f,r"\int",g,r"dx","+",f,"C_2",color=BLACK).next_to(formula_5,1.5*UP)
            second_term=MathTex("-",r"\int{",r"\left(",r"{{d","(",f,")",r"}\over{dx}}",r"\int",g,"dx",r"\right)","}dx","-",
                                r"\int{",r"{{d","(",f,")",r"}\over{dx}}","C_2}","dx",color=BLACK).next_to(formula_5,1.5*DOWN)
            color_code_formula(first_term)
            color_code_formula(second_term)
            self.wait_until_bookmark("first")
            self.play(
                TransformFromCopy(formula_5[5],first_term[5]),
                ReplacementTransform(formula_5[5],first_term[0]),
                ReplacementTransform(formula_5[7:11],first_term[1:5]),
                ReplacementTransform(formula_5[11:13],first_term[6]),
                FadeOut(formula_5[6],formula_5[13])
            )
            self.wait_until_bookmark("f_x")
            self.play(Indicate(first_term[5:],color=PINK))
            
            self.wait_until_bookmark("second")
            self.play(
                ReplacementTransform(formula_5[14],second_term[0]),
                TransformFromCopy(formula_5[15],second_term[1]),
                ReplacementTransform(formula_5[21],second_term[2]),
                TransformFromCopy(formula_5[16:21],second_term[3:8]),
                ReplacementTransform(formula_5[22:25],second_term[8:11]),
                ReplacementTransform(formula_5[28],second_term[11]),
                TransformFromCopy(formula_5[29],second_term[12]),
                ReplacementTransform(formula_5[25],second_term[13]),
                ReplacementTransform(formula_5[15],second_term[14]),
                ReplacementTransform(formula_5[16:21],second_term[15:20]),
                ReplacementTransform(formula_5[26:28],second_term[20]),
                ReplacementTransform(formula_5[29],second_term[21]),
                run_time=2
            )
            self.wait_until_bookmark("complex_term")
            self.play(Indicate(second_term[14:],color=PINK))
        
        with self.voiceover(text="""This term will give us f times C two with a constant C three.
                            f times C two is common with the above term with opposite sign, which means we 
                            <bookmark mark='cancel'/>can cancel them. And for the constants C one and C three 
                            <bookmark mark='combine'/>combine them in a single constant C, 
                            and <bookmark mark='arrange'/>arrange everything.
                            """):
            last_term=MathTex(f,"C_2","+","C","_3",color=BLACK).move_to(second_term[14:]).shift(MED_LARGE_BUFF*LEFT)
            color_code_formula(last_term)
            self.play(
                FadeOut(second_term[14:17],second_term[18:20],second_term[21]),
                ReplacementTransform(second_term[17],last_term[0]),
                ReplacementTransform(second_term[20],last_term[1]),
                Write(last_term[2:])
            )
            self.wait_until_bookmark("cancel")
            self.play(
                AnimationGroup(
                    AnimationGroup(
                        ShowCreationThenFadeOut(Cross(last_term[:2])[0]),
                        ShowCreationThenFadeOut(Cross(first_term[5:])[0])
                    ),
                FadeOut(last_term[:2],first_term[4:],second_term[13]),
                lag_ratio=0.90)
                )
                
            final_formula=MathTex(r"\int",f,g,r"dx",r"=",f,r"\int",g,r"dx","-",r"\int{",r"\left(",r"{{d","(",f,")",r"}\over{dx}}",
                        r"\int",g,r"dx",r"\right)}","dx","+","C",color=BLACK).scale(.95)
            color_code_formula(final_formula)
            self.wait_until_bookmark("combine")
            self.play(
                ReplacementTransform(VGroup(last_term[2:4],formula_5[-3:-1]),final_formula[-2:]),
                FadeOut(last_term[-1],formula_5[-1])
            )
            self.wait_until_bookmark("arrange")
            self.play(
                ReplacementTransform(formula_5[0:5],final_formula[0:5]),
                ReplacementTransform(first_term[0:4],final_formula[5:9]),
                ReplacementTransform(second_term[:13],final_formula[9:22])
            )
            self.wait_for_voiceover()
            self.wait()
            self.add_voiceover_text("q. e d")