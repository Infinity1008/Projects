from manim import *


class GraphAreaPlot(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-1,1,1],
            y_length = 1,
            axis_config={"include_tip": False}
        )

        labels = ax.get_axis_labels(x_label="Weight", y_label="")

        # self.add(ax,labels)
        data_points = [2.1, 2.7, 2.9, 3.1, 3.7, 4.5, 4.8, 7.1, 7.5, 7.7, 8.1, 8.2, 8.4, 8.7]
        data_points_left = [2.1, 2.7, 2.9, 3.1, 3.7, 4.5, 4.8]
        data_points_right = [7.1, 7.5, 7.7, 8.1, 8.2, 8.4, 8.7]

        data_points_manim_left_vg = VGroup(*[Dot(ax.coords_to_point(x,0)).scale(1.5) for x in data_points_left])
        data_points_manim_right_vg = VGroup(*[Dot(ax.coords_to_point(x, 0)).scale(1.5) for x in data_points_right])

        data_points_manim_left_vg_color = VGroup(*[Dot(ax.coords_to_point(x,0)).set_color(RED).scale(1.5) for x in data_points_left])
        data_points_manim_right_vg_color = VGroup(*[Dot(ax.coords_to_point(x, 0)).set_color(GREEN).scale(1.5) for x in data_points_right])


        #  Orignal divide Line
        divide_line = Line(ax.coords_to_point(5,0.5),ax.coords_to_point(5,-0.5)).set_color(YELLOW)


        self.play(FadeIn(ax,labels))
        self.play(FadeIn(data_points_manim_left_vg),FadeIn(data_points_manim_right_vg))
        self.play(Transform(data_points_manim_left_vg,data_points_manim_left_vg_color))
        self.play(Transform(data_points_manim_right_vg, data_points_manim_right_vg_color))
        self.play(FadeIn(divide_line))
        self.play(divide_line.animate.shift(LEFT))
        self.play(divide_line.animate.shift(RIGHT*2))
        self.play(divide_line.animate.shift(LEFT))
        self.play(divide_line.animate.set_color(YELLOW))

        # Adding new test data
        data_left = Dot(ax.coords_to_point(4,2))
        data_right = Dot(ax.coords_to_point(7.3,2))

        arrow_left = Arrow(start=ax.coords_to_point(4,-1.5),end=ax.coords_to_point(4,0.1))
        arrow_right = Arrow(start=ax.coords_to_point(7.3,-1.5),end=ax.coords_to_point(7.3,0.1))

        self.play(FadeIn(data_left))
        self.play(data_left.animate.move_to(ax.coords_to_point(4,0)))
        self.play(FadeIn(arrow_left))
        self.play(data_left.animate.set_color(RED),arrow_left.animate.set_color(RED))
        self.play(FadeOut(arrow_left),FadeOut(data_left))


        self.play(FadeIn(data_right))
        self.play(data_right.animate.move_to(ax.coords_to_point(7.3,0)))
        self.play(FadeIn(arrow_right))
        self.play(data_right.animate.set_color(GREEN),arrow_right.animate.set_color(GREEN))
        self.play(FadeOut(arrow_right),FadeOut(data_right))

        # New problematic data point
        problem_data = Dot(ax.coords_to_point(5.1,2))
        arrow_mid = Arrow(start=ax.coords_to_point(5.1,-1.5),end=ax.coords_to_point(5.1,0.1))

        self.play(FadeIn(problem_data))
        self.play(problem_data.animate.move_to(ax.coords_to_point(5.1,0)))
        self.play(FadeIn(arrow_mid))
        self.play(problem_data.animate.set_color(GREEN),arrow_mid.animate.set_color(GREEN))


        # Boxes
        box = SurroundingRectangle(data_points_manim_left_vg,color=WHITE, buff=MED_LARGE_BUFF)
        self.play(Create(box))

        self.play(problem_data.animate.set_color(RED),arrow_mid.animate.set_color(RED))
        self.play(FadeOut(box))
        self.play(FadeOut(arrow_mid))
        self.play(FadeOut(problem_data))
        self.play(FadeOut(divide_line))

        # Making case for threshold being in between edges of clusters
        data_points_manim_left_vg_color_transparent = VGroup(*[Dot(ax.coords_to_point(x,0)).scale(1.5) for x in data_points_left[:-1]])
        data_points_manim_left_vg_color_transparent.add(Dot(ax.coords_to_point(data_points_left[-1],0),color=RED).scale(1.5))

        data_points_manim_right_vg_color_transparent = VGroup(Dot(ax.coords_to_point(data_points_right[0],0),color=GREEN).scale(1.5))
        data_points_manim_right_vg_color_transparent += VGroup(*[Dot(ax.coords_to_point(x, 0)).scale(1.5) for x in data_points_right[1:]])

        self.play(Transform(data_points_manim_left_vg_color, data_points_manim_left_vg_color_transparent))
        self.play(Transform(data_points_manim_right_vg_color, data_points_manim_right_vg_color_transparent))

        # Creating 2nd divide line in mid of edges of clusters
        divide_line_second = Line(ax.coords_to_point(5.95,0.5),ax.coords_to_point(5.95,-0.5)).set_color(YELLOW)
        self.play(Create(divide_line_second))
        self.play(divide_line_second.animate.shift(LEFT))
        self.play(divide_line_second.animate.shift(RIGHT*2))
        self.play(divide_line_second.animate.shift(LEFT))

        # Adding new test point
        test_data_point_left = Dot(ax.coords_to_point(5.3,2))
        test_arrow_left = Arrow(start=ax.coords_to_point(5.3,-1.5),end=ax.coords_to_point(5.3,0.1))
        space_left = DashedLine(start=ax.coords_to_point(5.3, -0.5), end=ax.coords_to_point(4.8, -0.5),color=YELLOW)
        space_right = DashedLine(start=ax.coords_to_point(5.3, -0.8), end=ax.coords_to_point(7.1, -0.8),color=YELLOW)

        self.play(FadeIn(test_data_point_left))
        self.play(test_data_point_left.animate.move_to(ax.coords_to_point(5.3,0)))
        self.play(FadeIn(test_arrow_left))
        self.play(test_data_point_left.animate.set_color(RED),test_arrow_left.animate.set_color(RED))
        self.play(FadeOut(test_arrow_left))
        self.play(Create(space_left))
        self.play(Create(space_right))
        self.play(FadeOut(space_left,space_right))
        self.play(test_data_point_left.animate.set_scale(2))
        self.play(FadeOut(test_data_point_left))

        # Margin
        margin_left = DashedLine(start=ax.coords_to_point(5.95,-1),end= ax.coords_to_point(4.8,-1))
        margin_right = DashedLine(start=ax.coords_to_point(5.95, -1.2), end=ax.coords_to_point(7.1, -1.2))
        self.play(Create(margin_left),Create(margin_right))

        # Brackets
        b1 = Brace(margin_left)
        b1text = b1.get_text("Margin")
        self.add(b1text)
        self.play(Create(b1))
        self.play(FadeOut(b1,b1text,margin_left,margin_right))

        # divide line left
        divide_line_second_left = Line(ax.coords_to_point(5.3, 0.5), ax.coords_to_point(5.3, -0.5)).set_color(YELLOW)
        self.play(Transform(divide_line_second,divide_line_second_left))

        # New small margin
        small_margin_left = DashedLine(start=ax.coords_to_point(5.3,-1),end= ax.coords_to_point(4.8,-1))
        self.play(Create(small_margin_left))
        b2 = Brace(small_margin_left)
        b2text = b2.get_text("Margin")
        self.add(b2text)
        self.play(Create(b2))
        self.play(FadeOut(b2, b2text, small_margin_left))

        # Back to orignal margin
        divide_line_orignal = Line(ax.coords_to_point(5.95,0.5),ax.coords_to_point(5.95,-0.5)).set_color(YELLOW)
        self.play(ReplacementTransform(divide_line_second,divide_line_orignal))
        self.play(Create(margin_left),Create(margin_right))

        # Maximum Margin Classifier
        max_mar_clas_arrow = Arrow(start=ax.coords_to_point(5.5,-2.5),end=ax.coords_to_point(5.9,0.5))
        max_mar_clas_text = Text("Maximum Margin Classifier", font_size=40).next_to(max_mar_clas_arrow,DOWN)
        self.play(Create(max_mar_clas_arrow),FadeIn(max_mar_clas_text))
        self.play(FadeOut(margin_left, margin_right))
        self.play(FadeOut(max_mar_clas_arrow, max_mar_clas_text))
        self.play(FadeOut(divide_line_orignal))
        self.wait(2)


        # Back to orignal
        data_points = [2.1, 2.7, 2.9, 3.1, 3.7, 4.5, 4.8, 7.1, 7.5, 7.7, 8.1, 8.2, 8.4, 8.7]
        data_points_left = [2.1, 2.7, 2.9, 3.1, 3.7, 4.5, 4.8]
        data_points_right = [7.1, 7.5, 7.7, 8.1, 8.2, 8.4, 8.7]
        data_points_manim_left_vg_color_new = VGroup(*[Dot(ax.coords_to_point(x,0)).set_color(RED).scale(1.5) for x in data_points_left])
        data_points_manim_right_vg_color_new = VGroup(*[Dot(ax.coords_to_point(x, 0)).set_color(GREEN).scale(1.5) for x in data_points_right])

        self.play(Transform(data_points_manim_left_vg_color_transparent, data_points_manim_left_vg_color_new))
        self.play(Transform(data_points_manim_right_vg_color_transparent, data_points_manim_right_vg_color_new))

        # New data
        data_points = [2.1, 2.7, 2.9, 3.1, 3.7, 4.5, 6.5, 7.1, 7.5, 7.7, 8.1, 8.2, 8.4, 8.7]
        data_points_left = [2.1, 2.7, 2.9, 3.1, 3.7, 4.5, 6.5]
        data_points_right = [7.1, 7.5, 7.7, 8.1, 8.2, 8.4, 8.7]

        data_points_manim_left_vg_color_new2 = VGroup(*[Dot(ax.coords_to_point(x,0)).set_color(RED).scale(1.5) for x in data_points_left])
        data_points_manim_right_vg_color_new2 = VGroup(*[Dot(ax.coords_to_point(x, 0)).set_color(GREEN).scale(1.5) for x in data_points_right])

        self.play(Transform(data_points_manim_left_vg_color_new, data_points_manim_left_vg_color_new2))
        self.play(Transform(data_points_manim_right_vg_color_new, data_points_manim_right_vg_color_new2))

        # New divide Line 6.8
        divide_line_thrid = Line(ax.coords_to_point(6.8,0.5),ax.coords_to_point(6.8,-0.5)).set_color(YELLOW)
        self.play(Create(divide_line_thrid))

        # Margin
        small_margin_left = DashedLine(start=ax.coords_to_point(6.8,-1),end= ax.coords_to_point(6.5,-1))
        self.play(Create(small_margin_left))

        # Brackets
        b3 = Brace(small_margin_left)
        b3text = b3.get_text("Margin")
        self.add(b3text)
        self.play(Create(b3))
        self.play(FadeOut(b3,b3text,small_margin_left))
        self.wait(2)

        # New probelematic point
        problem_data = Dot(ax.coords_to_point(6.3, 2))
        arrow_problem = Arrow(start=ax.coords_to_point(6.3,-1.5),end=ax.coords_to_point(6.3,0.1))

        self.play(FadeIn(problem_data))
        self.play(problem_data.animate.move_to(ax.coords_to_point(6.3, 0)))
        self.play(FadeIn(arrow_problem))
        self.play(problem_data.animate.set_color(RED),arrow_problem.animate.set_color(RED))

        # Box
        box_right = Polygon(ax.coords_to_point(6.1,-1.5),ax.coords_to_point(9,-1.5),ax.coords_to_point(9,1.5),ax.coords_to_point(6.1,1.5))
        box_left = Polygon(ax.coords_to_point(2, -1.5), ax.coords_to_point(4.9, -1.5), ax.coords_to_point(4.9, 1.5),ax.coords_to_point(2, 1.5))
        # 2.1, 2.7, 2.9, 3.1, 3.7, 4.5, 6.5
        self.play(Create(box_right))
        self.play(Create(box_left))
        self.play(problem_data.animate.set_color(GREEN),arrow_problem.animate.set_color(GREEN))
        self.play(FadeOut(box_left,box_right))
        self.play(FadeOut(problem_data,arrow_problem))
        self.wait(1)

        self.play((data_points_manim_left_vg_color_new2[:-1]+data_points_manim_left_vg_color_new2[-1]).animate.set_color(WHITE))
        self.play(data_points_manim_right_vg_color_new2[1:].animate.set_color(WHITE))

        self.play(divide_line_thrid.animate.move_to(ax.coords_to_point(5.8, 0)))

        self.play(data_points_manim_left_vg_color_new2[-1].animate.set_color(RED))

        temp_dot = Dot(ax.coords_to_point(6.1, 2))
        temp_arrow = Arrow(start=ax.coords_to_point(6.1, -1.5),end=ax.coords_to_point(6.1, 0.1))

        self.play(FadeIn(temp_dot))
        self.play(temp_dot.animate.move_to(ax.coords_to_point(6.1, 0)),Create(temp_arrow))
        self.play(temp_dot.animate.set_color(GREEN),temp_arrow.animate.set_color(GREEN))
        self.play(FadeOut(temp_arrow))

        # Polygon Box
        temp_box = Polygon(ax.coords_to_point(5.9,-1.5),ax.coords_to_point(8.8,-1.5),ax.coords_to_point(8.8,1.5),ax.coords_to_point(5.9, 1.5))
        self.play(Create(temp_box))
        self.play(FadeOut(temp_box))
        self.play(FadeOut(temp_dot))
        self.play(data_points_manim_left_vg_color_new2[-1].animate.set_color(WHITE))

        # Margin
        small_margin_left = DashedLine(start=ax.coords_to_point(5.8,-1),end= ax.coords_to_point(4.5,-1))
        small_margin_right = DashedLine(start=ax.coords_to_point(5.8, -1.2), end=ax.coords_to_point(7.1, -1.2))

        self.play(Create(small_margin_left),Create(small_margin_right))







