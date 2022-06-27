from mailbox import NoSuchMailboxError
from re import L
from this import d
from turtle import update
from unittest import result
from manim import *
import itertools as it

from numpy import integer
class ParticulasVibrando(VGroup):
    CONFIG={
        'amplitude':1,
        'junggling_rate':1,
    }
    def __init__(self, group, **kwargs):
        VGroup.__init__(self, **kwargs)
        for mob in group.submobjects:
            mob.direction_factor = rotate_vector(RIGHT, np.random.random()*np.pi*2)
            mob.amplitude=self.CONFIG['amplitude']*np.random.random()
            mob.vibrate_frequency = self.CONFIG['amplitude']*np.random.random()
            self.add(mob)
        # group.arrange(RIGHT, buff=.5)
        self.add_updater(lambda m,dt:m.update(dt))
    def update(self, dt):
        for mob in self.submobjects:
            mob.vibrate_frequency += np.random.random()*TAU
            mob.shift(self.CONFIG['amplitude']*mob.direction_factor*np.sin(mob.vibrate_frequency)*dt)
class ProvingAgain(Scene):
    CONFIG={
        'mob_number':8,
        'colors':[RED, GREEN, BLUE, YELLOW, ORANGE, PINK, PURPLE, TEAL],
    }
    def construct(self):
        color_triangle=it.cycle(self.CONFIG['colors'])
        elements=ParticulasVibrando(VGroup(*[Triangle(color=next(color_triangle)) for _ in range(self.CONFIG['mob_number'])]))
        elements.arrange(RIGHT, buff=.5)
        elements.set_width(12)
        points=self.point_to_vertices(elements)
        self.add(elements,points)
        self.wait(10)
    def point_to_vertices(self,mobs):
        dots=VGroup()
        dot1=Dot().add_updater(lambda m,dt:m.move_to(mobs[0].points[0]))
        dots.add(dot1)
        dot2=Dot().add_updater(lambda m,dt:m.move_to(mobs[1].points[0]))
        dots.add(dot2)
        dot3=Dot().add_updater(lambda m,dt:m.move_to(mobs[2].points[0]))
        dots.add(dot3)
        dot4=Dot().add_updater(lambda m,dt:m.move_to(mobs[3].points[0]))
        dots.add(dot4)
        dot5=Dot().add_updater(lambda m,dt:m.move_to(mobs[4].points[0]))
        dots.add(dot5)
        dot6=Dot().add_updater(lambda m,dt:m.move_to(mobs[5].points[0]))
        dots.add(dot6)
        dot7=Dot().add_updater(lambda m,dt:m.move_to(mobs[6].points[0]))
        dots.add(dot7)
        dot8=Dot().add_updater(lambda m,dt:m.move_to(mobs[7].points[0]))
        dots.add(dot8)
        line1=Line().add_updater(lambda m,dt:m.put_start_and_end_on(dot1.get_center(),dot2.get_center()))
        dots.add(line1)
        line2=Line().add_updater(lambda m,dt:m.put_start_and_end_on(dot2.get_center(),dot3.get_center()))
        dots.add(line2)
        line3=Line().add_updater(lambda m,dt:m.put_start_and_end_on(dot3.get_center(),dot4.get_center()))
        dots.add(line3)
        line4=Line().add_updater(lambda m,dt:m.put_start_and_end_on(dot4.get_center(),dot5.get_center()))
        dots.add(line4)
        line5=Line().add_updater(lambda m,dt:m.put_start_and_end_on(dot5.get_center(),dot6.get_center()))
        dots.add(line5)
        line6=Line().add_updater(lambda m,dt:m.put_start_and_end_on(dot6.get_center(),dot7.get_center()))
        dots.add(line6)
        line7=Line().add_updater(lambda m,dt:m.put_start_and_end_on(dot7.get_center(),dot8.get_center()))
        dots.add(line7)
        number_of_lines1=DecimalNumber(0,num_decimal_places=1).add_updater(lambda m,dt:m.set_value(line1.get_length()))
        number_of_lines1.add_updater(
            lambda t: t.next_to(line1, UP, buff=.1)
        )
        dots.add(number_of_lines1)
        number_of_lines2=DecimalNumber(0,num_decimal_places=1).add_updater(lambda m,dt:m.set_value(line2.get_length()))
        number_of_lines2.add_updater(
            lambda t: t.next_to(line2, UP, buff=.1)
        )
        dots.add(number_of_lines2)
        number_of_lines3=DecimalNumber(0,num_decimal_places=1).add_updater(lambda m,dt:m.set_value(line3.get_length()))
        number_of_lines3.add_updater(
            lambda t: t.next_to(line3, UP, buff=.1)
        )
        dots.add(number_of_lines3)
        number_of_lines4=DecimalNumber(0,num_decimal_places=1).add_updater(lambda m,dt:m.set_value(line4.get_length()))
        number_of_lines4.add_updater(
            lambda t: t.next_to(line4, UP, buff=.1)
        )
        dots.add(number_of_lines4)
        number_of_lines5=DecimalNumber(0,num_decimal_places=1).add_updater(lambda m,dt:m.set_value(line5.get_length()))
        number_of_lines5.add_updater(
            lambda t: t.next_to(line5, UP, buff=.1)
        )
        dots.add(number_of_lines5)
        number_of_lines6=DecimalNumber(0,num_decimal_places=1).add_updater(lambda m,dt:m.set_value(line6.get_length()))
        number_of_lines6.add_updater(
            lambda t: t.next_to(line6, UP, buff=.1)
        )
        dots.add(number_of_lines6)
        number_of_lines7=DecimalNumber(0,num_decimal_places=1).add_updater(lambda m,dt:m.set_value(line7.get_length()))
        number_of_lines7.add_updater(
            lambda t: t.next_to(line7, UP, buff=.1)
        )
        dots.add(number_of_lines7)
        result=VGroup(
            Text('result'),
            MathTex('='),
            Integer(
                line1.get_length()+line2.get_length()+line3.get_length()+line4.get_length()+line5.get_length()+line6.get_length()+line7.get_length()
            ).add_updater(
                lambda t: t.set_value(line1.get_length()+line2.get_length()+line3.get_length()+line4.get_length()+line5.get_length()+line6.get_length()+line7.get_length())
            )
        ).arrange(RIGHT,buff=.5).to_edge(UP,buff=1)
        dots.add(result)
        return dots