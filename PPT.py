from manim import *

class PPT(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(60*DEGREES,30*DEGREES,zoom=1)
        #self.begin_ambient_camera_rotation(rate=0.5)
        L,l=5,6
        axes=ThreeDAxes(x_range=[-L,L,1],y_range=[-L,L,1],z_range=[-L,L,1],
        x_length=2*L,y_length=2*L,z_length=2*L)

        cube=Cube(side_length=2,fill_opacity=0.8)#.move_to(RIGHT+UP+OUT)
        Diag=Line(start=[-1,-1,-1],end=[1,1,1],stroke_opacity=0.5)
        Ent_cube=VGroup(cube,Diag)
        Ent_cube.rotate(angle=45*DEGREES,axis=Z_AXIS)#.shift((np.sqrt(2)-1)*(RIGHT+UP))
        
        plane_0=Surface(lambda u,v: axes.c2p(0,u,v),
            u_range=[0,l],
            v_range=[0,l],
            resolution=1,
            fill_color=WHITE,
            checkerboard_colors= [WHITE, WHITE],
            fill_opacity= 0.7,
            stroke_color=None,)
        #self.add(plane_0)
        self.add(Surface(lambda u,v:axes.c2p(np.sqrt(2),u+v,0),
        u_range=[-l,l],
        v_range=[-l,l],
        resolution=1,
        fill_color=WHITE,
        checkerboard_colors= [WHITE, WHITE],))
        self.add(axes)
        self.add(Ent_cube)
        self.add(cube)
        self.play(Rotate(Ent_cube,angle=(-np.arctan(1/(np.sqrt(2)))),axis=X_AXIS),run_time=5)
        self.wait()
        self.move_camera(90*DEGREES,0)
        self.wait()
        #self.stop_ambient_camera_rotation()
    