from manim import *


class Svc_Part_2(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 20, 5],
            y_range=[0, 20, 5],
            axis_config={"include_tip": False}
        )

        labels = ax.get_axis_labels(x_label="Weight", y_label="Height")

        self.play(FadeIn(ax, labels))
        # x = [0.8,2,3,4.3,10,11,12,13,14,14.8,15.1,15.2,15.7,15.9,16.1]
        # y = [2,2,3,5,2,2.2,2.5,2.6,4,5,6,7.5,12,15,19]

        x1 = [0.8,2,3,4.3]
        y1 = [2,2,3,5]

        x2 = [10,11,12,13,14,14.8,15.1]
        y2 = [2,2.2,2.5,2.6,4,5,6]

        x3 = [15.2,15.7,15.9,16.1]
        y3 = [7.5,12,15,19]



        data_points_manim_left_vg = VGroup(*[Dot(ax.coords_to_point(i,j)).scale(1.5) for i,j in zip(x1,y1)])
        data_points_manim_mid_vg = VGroup(*[Dot(ax.coords_to_point(i,j)).scale(1.5) for i,j in zip(x2,y2)])
        data_points_manim_right_vg = VGroup(*[Dot(ax.coords_to_point(i,j)).scale(1.5) for i,j in zip(x3,y3)])


        self.play(FadeIn(data_points_manim_left_vg,data_points_manim_mid_vg,data_points_manim_right_vg))
        self.wait(1)
        self.play(data_points_manim_left_vg.animate.set_color(RED),data_points_manim_mid_vg.animate.set_color(GREEN),data_points_manim_right_vg.animate.set_color(RED))
        self.wait(1)

        # margin_line
        margin_line = Line(ax.coords_to_point(3,0),ax.coords_to_point(20,12.5)).set_color(YELLOW)
        self.play(Create(margin_line,run_time=2))
        self.wait(2)

        margin_line_up = DashedLine(ax.coords_to_point(3,0),ax.coords_to_point(20,12.5)).shift(UP*.7)
        margin_line_down = DashedLine(ax.coords_to_point(3,0),ax.coords_to_point(20,12.5)).shift(DOWN*.7)

        self.play(Create(margin_line_up,run_time=2),Create(margin_line_down,run_time=2))
        self.wait(1)



        # Lines from margin to threshold
        line_up = DashedLine(ax.coords_to_point(15.7,11.5),ax.coords_to_point(15.7,9.5)).set_color(YELLOW)
        line_down = DashedLine(ax.coords_to_point(15.1,6.5),ax.coords_to_point(15.1,9)).set_color(YELLOW)

        self.play(Create(line_up,run_time=1),Create(line_down,run_time=1))

        # Brackets
        b1 = Brace(line_up,RIGHT)
        b1text = b1.get_text("Margin")
        self.play(Create(b1))
        self.play(Write(b1text))
        self.play(FadeOut(b1, b1text))
        self.play(FadeOut(line_up, line_down))
        self.wait()

        # Support vector classifier
        svc_text = Text("Support vector classifier")
        svc_text.shift(UP*2)
        self.play(Write(svc_text))




