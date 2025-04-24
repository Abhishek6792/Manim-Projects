from manim import *

class PPT(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(60*DEGREES,30*DEGREES,zoom=1)

        L,l=5,6
        axes=ThreeDAxes(x_range=[-L,L,1],y_range=[-L,L,1],z_range=[-L,L,1],
        x_length=2*L,y_length=2*L,z_length=2*L)

        points=[[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],
        [-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]
        face=[[0,1,2,3],[4,5,6,7],0,1]

        square=Polyhedron(points)
        self.add(axes)
        self.add(square)