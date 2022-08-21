from manim import *


class Svc_Part_1(Scene):
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

        #  Orignal divide Line
        divide_line = Line(ax.coords_to_point(5,0.5),ax.coords_to_point(5,-0.5))

        #Introductory Text
        intro = Text("Support Vector Classifiers")
        self.play(ShowCreationThenFadeOut(intro))


        self.play(FadeIn(ax, labels))
        self.play(FadeIn(data_points_manim_left_vg), FadeIn(data_points_manim_right_vg))
        self.wait(2)
        self.play(data_points_manim_left_vg.animate.set_color(RED),data_points_manim_right_vg.animate.set_color(GREEN))
        self.wait(2)

        threshold = Text("Threshold")
        threshold.next_to(divide_line,UP*2)
        self.play(Write(threshold))
        self.play(FadeIn(divide_line))
        self.play(divide_line.animate.set_color(YELLOW))
        self.play(FadeOut(threshold))
        self.play(divide_line.animate.shift(LEFT))
        self.play(divide_line.animate.shift(RIGHT * 2))
        self.play(divide_line.animate.shift(LEFT))

        ###############################################################################################################
        # Adding new test data
        data_left = Dot(ax.coords_to_point(4, 2))
        data_right = Dot(ax.coords_to_point(7.3, 2))

        arrow_left = Arrow(start=ax.coords_to_point(4, -1.5), end=ax.coords_to_point(4, 0.1))
        arrow_right = Arrow(start=ax.coords_to_point(7.3, -1.5), end=ax.coords_to_point(7.3, 0.1))

        self.play(FadeIn(data_left))
        self.play(Flash(data_left))
        self.play(data_left.animate.move_to(ax.coords_to_point(4, 0)))
        self.play(FadeIn(arrow_left))
        self.play(data_left.animate.set_color(RED), arrow_left.animate.set_color(RED))
        self.play(FadeOut(arrow_left), FadeOut(data_left))

        self.play(FadeIn(data_right))
        self.play(Flash(data_right))
        self.play(data_right.animate.move_to(ax.coords_to_point(7.3,0)))
        self.play(FadeIn(arrow_right))
        self.play(data_right.animate.set_color(GREEN),arrow_right.animate.set_color(GREEN))
        self.play(FadeOut(arrow_right),FadeOut(data_right))
        ###############################################################################################################
        # New problematic data point
        problem_data = Dot(ax.coords_to_point(5.1, 2))
        arrow_mid = Arrow(start=ax.coords_to_point(5.1, -1.5), end=ax.coords_to_point(5.1, 0.1))

        self.play(FadeIn(problem_data))
        self.play(Flash(problem_data))
        self.play(problem_data.animate.move_to(ax.coords_to_point(5.1, 0)))
        self.play(FadeIn(arrow_mid))
        self.play(problem_data.animate.set_color(GREEN), arrow_mid.animate.set_color(GREEN))
        self.wait(2)

        # Boxes
        box = SurroundingRectangle(data_points_manim_left_vg, color=WHITE, buff=MED_LARGE_BUFF)
        self.play(Create(box))

        self.play(problem_data.animate.set_color(RED), arrow_mid.animate.set_color(RED))
        self.play(FadeOut(box))
        self.play(FadeOut(arrow_mid))
        self.play(FadeOut(problem_data))
        self.play(FadeOut(divide_line))
        ###############################################################################################################
        # Making case for threshold being in between edges of clusters
        self.play(data_points_manim_left_vg[:-1].animate.set_color(WHITE),data_points_manim_right_vg[1:].animate.set_color(WHITE))
        self.wait(2)


        # Creating 2nd divide line in mid of edges of clusters
        divide_line_second = Line(ax.coords_to_point(5.95,0.5),ax.coords_to_point(5.95,-0.5)).set_color(YELLOW)
        self.play(Create(divide_line_second))
        self.wait(1)
        self.play(divide_line_second.animate.shift(LEFT))
        self.play(divide_line_second.animate.shift(RIGHT*2))
        self.play(divide_line_second.animate.shift(LEFT))
        self.wait(1)

        # Adding new test point
        test_data_point_left = Dot(ax.coords_to_point(5.3,2))
        test_arrow_left = Arrow(start=ax.coords_to_point(5.3,-1.5),end=ax.coords_to_point(5.3,0.1))
        space_left = DashedLine(start=ax.coords_to_point(5.3, -0.5), end=ax.coords_to_point(4.8, -0.5),color=YELLOW)
        space_right = DashedLine(start=ax.coords_to_point(5.3, -0.8), end=ax.coords_to_point(7.1, -0.8),color=YELLOW)

        self.play(FadeIn(test_data_point_left))
        self.play(Flash(test_data_point_left))
        self.play(test_data_point_left.animate.move_to(ax.coords_to_point(5.3,0)))
        self.play(FadeIn(test_arrow_left))
        self.play(test_data_point_left.animate.set_color(RED),test_arrow_left.animate.set_color(RED))
        self.play(FadeOut(test_arrow_left))
        self.play(Create(space_left))
        self.play(Create(space_right))
        self.wait(1)
        self.play(FadeOut(space_left,space_right))
        self.play(FadeOut(test_data_point_left))

        #Margin
        margin_left = DashedLine(start=ax.coords_to_point(5.95,-1),end= ax.coords_to_point(4.8,-1))
        margin_right = DashedLine(start=ax.coords_to_point(5.95, -1.2), end=ax.coords_to_point(7.1, -1.2))
        self.play(Create(margin_left),Create(margin_right))

        # Brackets
        b1 = Brace(margin_left)
        b1text = b1.get_text("Margin")
        self.play(Create(b1),Write(b1text))
        self.wait(1)
        self.play(FadeOut(b1,b1text,margin_left,margin_right))
        self.wait(1)


        ###############################################################################################################
        # divide line left
        self.play(divide_line_second.animate.move_to(ax.coords_to_point(5.3)))

        # New small margin
        small_margin_left = DashedLine(start=ax.coords_to_point(5.3, -1), end=ax.coords_to_point(4.8, -1))
        self.play(Create(small_margin_left))
        b2 = Brace(small_margin_left)
        b2text = b2.get_text("Margin")
        self.play(Create(b2),Write(b2text.set_color(RED)))
        self.wait(1)
        self.play(FadeOut(b2, b2text, small_margin_left))


        # Back to orignal margin
        self.play(divide_line_second.animate.move_to(ax.coords_to_point(5.95)))
        self.play(Create(margin_left),Create(margin_right))

        # Maximum Margin Classifier
        max_mar_clas_arrow = Arrow(start=ax.coords_to_point(5.5,2.5),end=ax.coords_to_point(5.9,0.5))
        max_mar_clas_text = Text("Maximum Margin Classifier", font_size=40).next_to(max_mar_clas_arrow,UP)

        # New small margin
        b_max = Brace(margin_left)
        b_max_text = b_max.get_text("Maximum Margin")
        self.play(Create(b_max), Write(b_max_text.set_color(GREEN)))
        self.wait(1)
        self.play(FadeOut(b_max, b_max_text))
        self.play(Create(max_mar_clas_arrow),FadeIn(max_mar_clas_text))
        self.play(FadeOut(margin_left, margin_right))
        self.play(FadeOut(max_mar_clas_arrow, max_mar_clas_text))
        self.play(FadeOut(divide_line_second))
        self.wait(2)

        ###############################################################################################################
        # Back to orignal
        self.play(data_points_manim_left_vg.animate.set_color(RED),data_points_manim_right_vg.animate.set_color(GREEN))

        # New data
        self.play(data_points_manim_left_vg[-1].animate.move_to(ax.coords_to_point(6.5)))
        self.wait(1)

        # New divide Line 6.8
        divide_line_thrid = Line(ax.coords_to_point(6.8,0.5),ax.coords_to_point(6.8,-0.5)).set_color(YELLOW)
        self.play(Create(divide_line_thrid))

        # Margin
        small_margin_left = DashedLine(start=ax.coords_to_point(6.8,-1),end= ax.coords_to_point(6.5,-1))
        self.play(Create(small_margin_left))

        # Brackets
        b3 = Brace(small_margin_left)
        b3text = b3.get_text("Margin")
        self.play(Create(b3text), Write(b3.set_color(GREEN)))
        self.play(FadeOut(b3,b3text,small_margin_left))
        self.wait(1)

        # New probelematic point
        problem_data = Dot(ax.coords_to_point(6.3, 2))
        arrow_problem = Arrow(start=ax.coords_to_point(6.3,-1.5),end=ax.coords_to_point(6.3,0.1))

        self.play(FadeIn(problem_data))
        self.play(Flash(problem_data))
        self.play(problem_data.animate.move_to(ax.coords_to_point(6.3, 0)))
        self.play(FadeIn(arrow_problem))
        self.play(problem_data.animate.set_color(RED),arrow_problem.animate.set_color(RED))
        self.wait(1)

        # Box
        box_right = Polygon(ax.coords_to_point(6.1,-1.5),ax.coords_to_point(9,-1.5),ax.coords_to_point(9,1.5),ax.coords_to_point(6.1,1.5))
        box_left = Polygon(ax.coords_to_point(2, -1.5), ax.coords_to_point(4.9, -1.5), ax.coords_to_point(4.9, 1.5),ax.coords_to_point(2, 1.5))
        self.play(Create(box_right))
        self.play(Create(box_left))
        self.wait(1)
        self.play(problem_data.animate.set_color(GREEN),arrow_problem.animate.set_color(GREEN))
        self.play(FadeOut(box_left,box_right))
        self.play(FadeOut(problem_data,arrow_problem))
        self.wait(1)

        # Making data transform for soft margin
        self.play((data_points_manim_left_vg[:-2]+data_points_manim_left_vg[-1]).animate.set_color(WHITE))
        self.play(data_points_manim_right_vg[1:].animate.set_color(WHITE))

        self.play(divide_line_thrid.animate.move_to(ax.coords_to_point(5.8, 0)))
        self.wait(1)
        self.play(Flash(data_points_manim_left_vg[-1]))
        self.play(data_points_manim_left_vg[-1].animate.set_color(RED))
        self.play(FadeIn(problem_data))
        self.play(Flash(problem_data))
        self.play(problem_data.animate.move_to(ax.coords_to_point(6.3, 0)))
        self.play(FadeIn(arrow_problem))
        self.play(problem_data.animate.set_color(GREEN), arrow_problem.animate.set_color(GREEN))
        self.play(FadeOut(problem_data,arrow_problem))


        # Soft Margin
        soft_margin_left = DashedLine(start=ax.coords_to_point(5.8,-1),end= ax.coords_to_point(4.5,-1))
        soft_margin_right = DashedLine(start=ax.coords_to_point(5.8,-1.2),end= ax.coords_to_point(7.1,-1.2))
        self.play(Create(soft_margin_left),Create(soft_margin_right))

        # Brackets
        b3 = Brace(soft_margin_left)
        b3text = b3.get_text("Soft Margin")
        self.play(Create(b3), Write(b3text))

        self.play(data_points_manim_left_vg[-1].animate.set_color(WHITE))
        self.play(FadeOut(b3,b3text,soft_margin_left,soft_margin_right))

        # We allowed for errors
        # error_text = Text("Important: We allowed for errors")
        error_text = MarkupText(f'Important<span fgcolor="{WHITE}">: We allowed for errors.</span>', color=GREEN)

        error_text.shift(UP*2)
        self.play(ShowCreationThenFadeOut(error_text))
        self.wait(1)

        # Running different scenarios
        self.play(data_points_manim_left_vg.animate.set_color(WHITE),data_points_manim_right_vg.animate.set_color(WHITE),data_points_manim_left_vg[2].animate.set_color(RED),data_points_manim_right_vg[4].animate.set_color(GREEN),divide_line_thrid.animate.move_to(ax.coords_to_point(5.5)))
        self.play(Flash(data_points_manim_left_vg[2]),Flash(data_points_manim_right_vg[4]))
        self.wait(1)
        self.play(data_points_manim_left_vg.animate.set_color(WHITE),data_points_manim_right_vg.animate.set_color(WHITE),data_points_manim_left_vg[3].animate.set_color(RED),data_points_manim_right_vg[1].animate.set_color(GREEN),divide_line_thrid.animate.move_to(ax.coords_to_point(5.3)))
        self.play(Flash(data_points_manim_left_vg[3]), Flash(data_points_manim_right_vg[1]))
        self.wait(1)
        self.play(data_points_manim_left_vg.animate.set_color(WHITE),data_points_manim_right_vg.animate.set_color(WHITE),data_points_manim_left_vg[5].animate.set_color(RED),data_points_manim_right_vg[5].animate.set_color(GREEN),divide_line_thrid.animate.move_to(ax.coords_to_point(6.45)))
        self.play(Flash(data_points_manim_left_vg[5]), Flash(data_points_manim_right_vg[5]))
        self.wait(1)
        self.play(data_points_manim_left_vg.animate.set_color(WHITE),data_points_manim_right_vg.animate.set_color(WHITE),data_points_manim_left_vg[5].animate.set_color(RED),data_points_manim_right_vg[0].animate.set_color(GREEN),divide_line_thrid.animate.move_to(ax.coords_to_point(5.8)))
        self.play(Flash(data_points_manim_left_vg[5]), Flash(data_points_manim_right_vg[0]))

        # Cross Validation
        error_text = MarkupText(f'Answer<span fgcolor="{WHITE}">: Cross Validation.</span>', color=GREEN)

        error_text.shift(UP * 2)
        self.play(ShowCreationThenFadeOut(error_text))
        self.wait(1)

        # Margins and brackets
        soft_margin_left = DashedLine(start=ax.coords_to_point(5.8,-1),end= ax.coords_to_point(4.5,-1))
        soft_margin_right = DashedLine(start=ax.coords_to_point(5.8,-1.2),end= ax.coords_to_point(7.1,-1.2))
        self.play(Create(soft_margin_left),Create(soft_margin_right))

        # Brackets
        b3 = Brace(soft_margin_left)
        b3text = b3.get_text("Soft Margin Classifier/Support Vector Classifier")
        self.play(Create(b3), Write(b3text))
        self.wait(2)
        self.play(FadeOut(b3,b3text,soft_margin_left,soft_margin_right))
        self.wait(5)












