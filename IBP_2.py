from manim import *

class ThreeD_0(ThreeDScene):
    def construct(self):
        self.camera.background_color = '#fdd8b7'
        l,x,y=5,0,0
        self.set_camera_orientation(60*DEGREES,-80*DEGREES,zoom=1,frame_center=((l+x/2)*RIGHT+(l+y/2)*UP))
        self.begin_ambient_camera_rotation(rate=0.4)
        axis=ThreeDAxes(x_range=(0,l,1),y_range=(0,l,1),z_range=(0,l,1)
                        ,x_length=l,y_length=l,z_length=l).set_color(BLACK).shift((l+x)*RIGHT+(l+y)*UP)
        
        self.play(Create(axis))
        
        SIN=lambda x: 3*np.sin(0.3*x)
        func_1=always_redraw(lambda:ParametricFunction(lambda u : axis.c2p(u,0,SIN(u)),
            t_range=[0,5]).set_color(DARK_BLUE).set_shade_in_3d(True))
        self.play(Write(func_1))
        
        plane=Square(side_length=5,color=BLACK,fill_opacity=.2,stroke_opacity=0)
        self.play(FadeIn(plane.move_to((l+x)*RIGHT+(l+y)*UP)))
        
        SQR=lambda x: 0.2*x**2+1
        func_2=always_redraw(lambda:ParametricFunction(lambda u,:axis.c2p(u,SQR(u),0),
            t_range=[0.01,4.39]).set_color(PURE_RED).set_shade_in_3d(True))
        self.play(Write(func_2))        
        
        def approx_volume(a,b,n):
            dx=(b-a)/(n)
            p0=VGroup(*list(VGroup(*list(Prism(dimensions=[dx,SQR(a+i*dx),SIN(a+i*dx)], stroke_width=0) for i in range(1,n+1)))))
            for i in range(1,n+1):
                p0[i-1].move_to(axis.c2p((a+i*dx)-0.5*dx,SQR((a+i*dx))/2,SIN(a+i*dx)/2))
            p0.set_color_by_gradient(PURE_RED,DARK_BLUE)
            p0.set_opacity(0.3)
            return(p0)

        self.play(Create(approx_volume(1,4,250)))
        #self.wait((2*PI/0.4)-5)
        self.stop_ambient_camera_rotation()

class Area(ThreeDScene):
    def construct(self):
        self.camera.background_color = '#fdd8b7'
        self.set_camera_orientation(60*DEGREES,-80*DEGREES,zoom=0.8)
        self.begin_ambient_camera_rotation(rate=0.7)
        axis=ThreeDAxes(x_range=(-5,5,1),y_range=(-5,5,1),z_range=(-2,5,1)
                        ,x_length=10,y_length=10,z_length=7).set_color(BLACK) 
        self.add(axis)
        
        
        SIN=lambda x: 3*np.sin(0.2*x)
        SQR=lambda x: 0.2*x**2+1
        
        x=ValueTracker(0)
        def rect_A():
            vertices=[
                [x.get_value(),0,0],
                [x.get_value(),0,SIN(x.get_value())],
                [x.get_value(),SQR(x.get_value()),SIN(x.get_value())],
                [x.get_value(),SQR(x.get_value()),0]
            ]
            return Polygon(*vertices,color=BLACK)
        rect_area = always_redraw(rect_A)
        self.add(rect_area)
        
        self.play(x.animate.set_value(5),run_time=5)
        self.stop_ambient_camera_rotation()
        
        
        func_1=Surface(lambda u,v : axis.c2p(u, v,SIN(u)),
            u_range=[0,5],
            v_range=[0,5],checkerboard_colors=[DARK_BLUE,DARK_BLUE],
            stroke_width=0.1,resolution=100)
        self.play(Write(func_1))
        
        
        func_2=Surface(lambda u,v :axis.c2p(u,SQR(u),v),
            u_range=[0,5],
            v_range=[0,3],checkerboard_colors=[PURE_RED,PURE_RED],
            stroke_width=0.1,resolution=100)
        self.play(Write(func_2))
        
class Volume(ThreeDScene):
    def construct(self):
        self.camera.background_color = '#fdd8b7'
        self.set_camera_orientation(60*DEGREES,-80*DEGREES,zoom=0.8)
        self.begin_ambient_camera_rotation(rate=0.4)
        axis=ThreeDAxes(x_range=(0,5,1),y_range=(0,5,1),z_range=(0,5,1)
                        ,x_length=5,y_length=5,z_length=5).set_color(BLACK) 
        axis.shift(2.5*(UP+RIGHT))
        self.play(Create(axis))
        
        SIN=lambda x: 3*np.sin(0.3*x)
        func_1=always_redraw(lambda:ParametricFunction(lambda u : axis.c2p(u,0,SIN(u)),
            t_range=[0,5]).set_color(DARK_BLUE).set_shade_in_3d(True))
        self.play(Write(func_1))
        
        plane=Square(side_length=5,color=BLACK,fill_opacity=.2,stroke_opacity=0)
        self.play(FadeIn(plane.move_to([2.5,2.5,0])))
        
        SQR=lambda x: 0.2*x**2+1
        func_2=always_redraw(lambda:ParametricFunction(lambda u,:axis.c2p(u,SQR(u),0),
            t_range=[0,4.39]).set_color(PURE_RED).set_shade_in_3d(True))
        self.play(Write(func_2))        
        
                
        def approx_volume(a,b,n):
            dx=(b-a)/(n)
            p0=VGroup()
            for i in range(1,n+1):
                vertices=[
                [a+i*dx,0,0],
                [a+i*dx,0,SIN(a+i*dx)],
                [a+i*dx,SQR(a+i*dx),SIN(a+i*dx)],
                [a+i*dx,SQR(a+i*dx),0]
                ]
                p0.add(Polygon(*vertices, stroke_width=0))    
            p0.set_color_by_gradient(PURE_RED,DARK_BLUE)
            p0.set_shade_in_3d(True)
            p0.set_opacity(0.5)
            return(p0)

        self.play(Create(approx_volume(1,4,500)))
        self.wait(3)
        #self.wait((2*PI/0.4)-5)
        self.stop_ambient_camera_rotation() 