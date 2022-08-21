from manim import *
import math


class Svc_Part_3(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-1,100,10],
            axis_config={"include_tip": False}
        )

        labels = ax.get_axis_labels(x_label="Weight", y_label="y")

        self.play(FadeIn(ax, labels))
        data_points = [2,2.2,3,3.1,6,6.1,6.4,6.7,6.8,6.9,8.9,9.5,9.9]
        data_points_left = [2,2.2,3,3.1]
        data_points_mid = [6,6.1,6.4,6.7,6.8,6.9]
        data_points_right = [8.9,9.5,9.9]

        data_points_manim_left_vg = VGroup(*[Dot(ax.coords_to_point(x,0)).scale(1.5) for x in data_points_left])
        data_points_manim_mid_vg = VGroup(*[Dot(ax.coords_to_point(x,0)).scale(1.5) for x in data_points_mid])
        data_points_manim_right_vg = VGroup(*[Dot(ax.coords_to_point(x, 0)).scale(1.5) for x in data_points_right])

        # Orignal divide Line
        divide_line = Line(ax.coords_to_point(5,5),ax.coords_to_point(5,-5))

        # self.play(Create(ax, labels))
        self.play(FadeIn(data_points_manim_left_vg), FadeIn(data_points_manim_mid_vg),FadeIn(data_points_manim_right_vg))
        self.play(data_points_manim_left_vg.animate.set_color(RED),data_points_manim_mid_vg.animate.set_color(GREEN),data_points_manim_right_vg.animate.set_color(RED))


        self.play(Create(divide_line.set_color(YELLOW)))
        self.wait(1)
        self.play(divide_line.animate.shift(LEFT*2))
        self.wait(1)
        self.play(divide_line.animate.shift(RIGHT * 5))
        self.wait(1)
        self.play(divide_line.animate.shift(LEFT*3))
        self.wait(1)

        # Confustion
        conf = Text("What to do now?")
        conf.shift(UP)
        self.play(ShowCreationThenFadeOut(conf))
        self.wait(1)

        svm = Text('Support Vector Machine')
        self.play(ShowCreationThenFadeOut(svm.shift(UP*2)))
        self.play(FadeOut(divide_line))

        ####################################################################################
        # Adding y axis
        labels_new = ax.get_axis_labels(x_label="Weight", y_label=MathTex(r"Weight^2"))
        self.play(ReplacementTransform(labels,labels_new))
        self.wait(1)
        ####################################################################################

        # Y squared points
        data_points_left = [2,2.2,3,3.1]
        data_points_mid = [6,6.1,6.4,6.7,6.8,6.9]
        data_points_right = [8.9,9.5,9.9]

        data_points_manim_left_vg_new = VGroup(*[Dot(ax.coords_to_point(x,x**2),color=RED).scale(1.5) for x in data_points_left])
        data_points_manim_mid_vg_new = VGroup(*[Dot(ax.coords_to_point(x,x**2),color=GREEN).scale(1.5) for x in data_points_mid])
        data_points_manim_right_vg_new = VGroup(*[Dot(ax.coords_to_point(x,x**2),color=RED).scale(1.5) for x in data_points_right])

        self.play(ReplacementTransform(data_points_manim_left_vg,data_points_manim_left_vg_new),ReplacementTransform(data_points_manim_mid_vg,data_points_manim_mid_vg_new),ReplacementTransform(data_points_manim_right_vg,data_points_manim_right_vg_new))
        self.wait(2)
        # Margin Line
        line = Line(ax.coords_to_point(2.8,0),ax.coords_to_point(10,90)).set_color(YELLOW)
        self.play(Create(line))
        self.wait(2)

        # Examples
        red_example = Dot(ax.coords_to_point(5,50))
        green_example = Dot(ax.coords_to_point(8, 20))

        self.play(Create(red_example))
        self.play(Flash(red_example))
        self.play(red_example.animate.set_color(RED))
        self.play(FadeOut(red_example))

        self.play(Create(green_example))
        self.play(Flash(green_example))
        self.play(green_example.animate.set_color(GREEN))
        self.play(FadeOut(green_example))
        self.wait(1)

        self.play(FadeOut(line))
        self.wait(2)

        # But why x^2
        but_y = Text(r"But why Weight^2")
        but_y.shift(UP*2)
        self.play(ShowCreationThenFadeOut(but_y))
        self.wait(1)


        # Y cubed points
        data_points_left = [2,2.2,3,3.1]
        data_points_mid = [6,6.1,6.4,6.7,6.8,6.9]
        data_points_right = [8.9,9.5,9.9]

        data_points_manim_left_vg_new_v2 = VGroup(*[Dot(ax.coords_to_point(x,x**3),color=RED).scale(1.5) for x in data_points_left])
        data_points_manim_mid_vg_new_v2 = VGroup(*[Dot(ax.coords_to_point(x,x**3),color=GREEN).scale(1.5) for x in data_points_mid])
        data_points_manim_right_vg_new_v2 = VGroup(*[Dot(ax.coords_to_point(x,x**3),color=RED).scale(1.5) for x in data_points_right])


        # Changing y axis
        labels_new_v2 = ax.get_axis_labels(x_label="Weight", y_label=MathTex(r"Weight^3"))

        self.play(ReplacementTransform(data_points_manim_left_vg_new,data_points_manim_left_vg_new_v2),ReplacementTransform(data_points_manim_mid_vg_new,data_points_manim_mid_vg_new_v2),ReplacementTransform(data_points_manim_right_vg_new,data_points_manim_right_vg_new_v2),ReplacementTransform(labels_new,labels_new_v2))
        self.wait(3)

        # pi/4 * sqroot of points
        data_points_left = [2,2.2,3,3.1]
        data_points_mid = [6,6.1,6.4,6.7,6.8,6.9]
        data_points_right = [8.9,9.5,9.9]

        data_points_manim_left_vg_new_v3 = VGroup(*[Dot(ax.coords_to_point(x,(3.14/4*math.sqrt(x))),color=RED).scale(1.5) for x in data_points_left])
        data_points_manim_mid_vg_new_v3 = VGroup(*[Dot(ax.coords_to_point(x,(3.14/4*math.sqrt(x))),color=GREEN).scale(1.5) for x in data_points_mid])
        data_points_manim_right_vg_new_v3 = VGroup(*[Dot(ax.coords_to_point(x,(3.14/4*math.sqrt(x))),color=RED).scale(1.5) for x in data_points_right])

        # Changing y axis
        labels_new_v3 = ax.get_axis_labels(x_label="Weight", y_label=MathTex(r"\frac{pi}{4} \times \sqrt{x}"))
        self.play(ReplacementTransform(data_points_manim_left_vg_new_v2,data_points_manim_left_vg_new_v3),ReplacementTransform(data_points_manim_mid_vg_new_v2,data_points_manim_mid_vg_new_v3),ReplacementTransform(data_points_manim_right_vg_new_v2,data_points_manim_right_vg_new_v3),ReplacementTransform(labels_new_v2,labels_new_v3))
        self.wait(3)

        # Changing back to orignal
        data_points_left = [2,2.2,3,3.1]
        data_points_mid = [6,6.1,6.4,6.7,6.8,6.9]
        data_points_right = [8.9,9.5,9.9]

        # Adding y axis
        labels_orignal = ax.get_axis_labels(x_label="Weight", y_label=MathTex(r"Weight^2"))

        data_points_manim_left_vg_orignal = VGroup(*[Dot(ax.coords_to_point(x,x**2),color=RED).scale(1.5) for x in data_points_left])
        data_points_manim_mid_vg_orignal = VGroup(*[Dot(ax.coords_to_point(x,x**2),color=GREEN).scale(1.5) for x in data_points_mid])
        data_points_manim_right_vg_orignal = VGroup(*[Dot(ax.coords_to_point(x,x**2),color=RED).scale(1.5) for x in data_points_right])

        self.play(ReplacementTransform(data_points_manim_left_vg_new_v3,data_points_manim_left_vg_orignal),ReplacementTransform(data_points_manim_mid_vg_new_v3,data_points_manim_mid_vg_orignal),ReplacementTransform(data_points_manim_right_vg_new_v3,data_points_manim_right_vg_orignal),ReplacementTransform(labels_new_v3,labels_orignal))
        self.wait(3)

        kernel = Text("Kerel functions")
        kernel.shift(UP)
        self.play(Write(kernel))
        self.play(FadeOut(kernel))

        # Back to 1D
        data_points_left = [2,2.2,3,3.1]
        data_points_mid = [6,6.1,6.4,6.7,6.8,6.9]
        data_points_right = [8.9,9.5,9.9]

        data_points_manim_left_vg_1d = VGroup(*[Dot(ax.coords_to_point(x,0),color=RED).scale(1.5) for x in data_points_left])
        data_points_manim_mid_vg_1d = VGroup(*[Dot(ax.coords_to_point(x,0),color=GREEN).scale(1.5) for x in data_points_mid])
        data_points_manim_right_vg_1d = VGroup(*[Dot(ax.coords_to_point(x, 0),color=RED).scale(1.5) for x in data_points_right])

        labels_1d = ax.get_axis_labels(x_label="Weight", y_label="y")

        self.play(ReplacementTransform(data_points_manim_left_vg_orignal,data_points_manim_left_vg_1d),ReplacementTransform(data_points_manim_mid_vg_orignal,data_points_manim_mid_vg_1d),ReplacementTransform(data_points_manim_right_vg_orignal,data_points_manim_right_vg_1d),ReplacementTransform(labels_orignal,labels_1d))

        # Polynomial
        poly_text = Text("Polynomial Kernel Function")
        poly_text.shift(UP*2)
        self.play(Write(poly_text))
        self.play(Unwrite(poly_text))

