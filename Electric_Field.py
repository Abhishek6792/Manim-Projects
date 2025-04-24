from manim import *

class E_field(Scene):
    def construct(self):
        def func(pos):
            x=pos[0]
            y=pos[1]
            k=1
            l=3
            
            # "+" charge coordinate:[-3,0] , "-" charge coordinate:[3,0]
            #r_1=distance between '+' and [x,y] ,r_2=distance between '-' and [x,y]

            r_1,r_2=(np.sqrt((l+x)**2+y**2)),(np.sqrt((l-x)**2+y**2))   
            E_x=(k)*(((l+x)/(r_1)**3)-((l-x)/(r_2)**3))      # x component of electric field
            E_y=(k)*(y)*((1/(r_1)**3)+(1/(r_2)**3))          # y component of electric field
            E=np.sqrt((E_x)**2+(E_y)**2)
    
            return(((E_x)*RIGHT+(E_y)*UP)/E)                 # returns a unit vector
        
    
        C=StreamLines(func,x_range=[-15.1,15.1,0.3],y_range=[-9.1,9.1,0.3],
        stroke_width=1,max_anchors_per_line=500,padding=1,dt=0.05,
        virtual_time=3,noise_factor=0)

        self.add(C)
        C.start_animation(warm_up=False, flow_speed=1)
        self.wait(C.virtual_time / C.flow_speed)