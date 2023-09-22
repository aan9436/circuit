import arcade
from circuit import *
from element import *

from arcade import draw_line,draw_circle_outline,draw_text,set_background_color,color,start_render,run
import math
w=800
h=600

class Draw(arcade.Window):
    def __init__(self):
        super().__init__(w, h, "Circuit")
        self.setup()
    def setup(self):
        self.series()
        set_background_color(color.WHITE)
    def on_draw(self):
        start_render()
        if self.dic:
            r=self.dic["radius"]
            l1,l2,l3,l4=self.dic["lst"]
            x=600
            y=450
            for i in l1:
                # print(i[1] + r, i[2])
                draw_line(x, y, i[1] + r, i[2], color.BLACK, 1)
                self.draw(r,i[0],i[1],i[2],i[3])

                x=i[1]-r
                break

            draw_line(x, y, 200,450, color.BLACK, 1)
            x=200
            y=450
            for i in l2:
                # print(i[1] + r, i[2])
                draw_line(x, y, i[1], i[2]+r, color.BLACK, 1)
                self.draw(r,i[0],i[1],i[2],i[3])
                y=i[2]-r
                break

            draw_line(x, y,200,150, color.BLACK, 1)
            x=200
            y=150
            for i in l3:
                # print(i[1] + r, i[2])
                draw_line(x, y, i[1] - r, i[2], color.BLACK, 1)
                self.draw(r,i[0],i[1],i[2],i[3])
                x=i[1]+r
                break

            draw_line(x, y, 600, 150, color.BLACK, 1)
            x=600
            y=150
            for i in l4:
                # print(i[1] + r, i[2])
                draw_line(x, y, i[1], i[2]-r, color.BLACK, 1)
                self.draw(r,i[0],i[1],i[2],i[3])
                y=i[2]+r
                break

            draw_line(x, y, 600,450, color.BLACK, 1)
    def bg(self):

        draw_line(0,h//2+h//4,w,h//2+h//4,color.GRAY,1)
        draw_line(w//2+w//4,0,w//2+w//4,h,color.GRAY,1)
        draw_line(0,h//4,w,h//4,color.GRAY,1)
        draw_line(w//4,0,w//4,h,color.GRAY,1)
        draw_line(0,h//2,w,h//2,color.GRAY,2)
        draw_line(w//2,0,w//2,h,color.GRAY,2)
    def draw_power(self,x,y,name,r):
        draw_line(x-0.2*r,y,x-r,y,color.BLACK,r//11)
        draw_line(x-0.2*r,y-r,x-0.2*r,y+r,color.BLACK,r//11)
        draw_line(x+0.2*r,y-0.6*r,x+0.2*r,y+0.6*r,color.BLACK,r//11)
        draw_line(x+0.2*r,y,x+r,y,color.BLACK,r//11)
        draw_text(name,x+0.2*r,y+0.8*r,color.BLACK,1.5*r//len(name))
    def draw_light(self,x,y,name,r):
        draw_circle_outline(x,y,r,color.BLACK,r//11)
        draw_line(x+r*0.6*math.sin(math.radians(-45)),y+r*0.6*math.cos(math.radians(-45)),x+r*0.6*math.sin(math.radians(135)),y+r*0.6*math.cos(math.radians(135)),color.BLACK,r//11)
        draw_line(x+r*0.6*math.sin(math.radians(45)),y+r*0.6*math.cos(math.radians(45)),x+r*0.6*math.sin(math.radians(-135)),y+r*0.6*math.cos(math.radians(-135)),color.BLACK,r//11)
        draw_text(name,x+0.5*r,y+r,color.BLACK,1.5*r//max(len(name),3))
    def series(self):
        circuit = Circuit("main")  # 创建电路“main”
        s = OnePoleSwitch("s")  # 创建单刀开关“s”
        circuit.add(s)  # 把开关“s”添加到电路“main”下
        l = Light("L")  # 创建灯泡“L”
        s.add(l)  # 把灯泡“l1”添加到开关“l”下
        self.dic=circuit.to_series()
    def draw(self,r,n,x,y,name):
        if n=="power":
            self.draw_power(x,y,name,r)
        elif n=="light":
            self.draw_light(x,y,name,r)
        else:
            pass

if __name__=="__main__":
    draw=Draw()
    run()