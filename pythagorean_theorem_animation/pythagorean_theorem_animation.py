from manim import *


class PythagoreanTheorem(Scene):
    def construct(self):
        step_time = 3.1
        scale_factor = 0.1

        # 定义起始标题
        title = Text('动画演示勾股定理的证明', font_size=64)

        # 定义直角三角形及直角符号
        right_triangle_pts = np.array([[-9, 0, 0], [16, 0, 0], [0, 12, 0]]) * scale_factor
        right_triangle = VGroup(
            Polygon(*right_triangle_pts, stroke_width=0, fill_color=BLUE, fill_opacity=1.0),
            RightAngle(
                Line(right_triangle_pts[2], right_triangle_pts[0]),
                Line(right_triangle_pts[2], right_triangle_pts[1]),
                length=2 * scale_factor,
                color=WHITE,
                stroke_width=2
            ),
        )

        # 定义直角三角形各边符号及变换用符号
        side_a = MathTex('a', font_size=32, z_index=9).set_x(-3 * scale_factor).set_y(6 * scale_factor)
        side_b = MathTex('b', font_size=32, z_index=9).set_x(6 * scale_factor).set_y(6 * scale_factor)
        side_c = MathTex('c', font_size=32, z_index=9).set_x(2 * scale_factor).set_y(1 * scale_factor)

        side_a_shadow = MathTex('a', font_size=32, z_index=9).set_x(-3 * scale_factor).set_y(6 * scale_factor)
        side_b_shadow = MathTex('b', font_size=32, z_index=9).set_x(6 * scale_factor).set_y(6 * scale_factor)
        side_c_shadow = MathTex('c', font_size=32, z_index=9).set_x(2 * scale_factor).set_y(1 * scale_factor)

        side_a_twin = MathTex('a', font_size=32, z_index=9).set_x(-5 * scale_factor).set_y(18 * scale_factor)
        side_b_twin = MathTex('b', font_size=32, z_index=9).set_x(-7 * scale_factor).set_y(30 * scale_factor)
        side_c_twin = MathTex('c', font_size=32, z_index=9).set_x(2 * scale_factor).set_y(26 * scale_factor)

        # 定义短边正方形
        square_3_pts = np.array([[-9, 0, 0], [0, 12, 0], [-12, 21, 0], [-21, 9, 0]]) * scale_factor
        square_3 = VGroup(
            Polygon(*square_3_pts, stroke_width=0, fill_color=PURPLE, fill_opacity=1.0),
            MathTex('a^2', font_size=32, z_index=9).set_x(-10.5 * scale_factor).set_y(10.5 * scale_factor),
        )

        # 定义长边正方形
        square_4_pts = np.array([[0, 12, 0], [16, 0, 0], [28, 16, 0], [12, 28, 0]]) * scale_factor
        square_4 = VGroup(
            Polygon(*square_4_pts, stroke_width=0, fill_color=GREEN, fill_opacity=1.0),
            MathTex('b^2', font_size=32, z_index=9).set_x(14 * scale_factor).set_y(14 * scale_factor),
        )

        # 定义斜边正方形
        square_5_pts = np.array([[-9, 0, 0], [-9, -25, 0], [16, -25, 0], [16, 0, 0]]) * scale_factor
        square_5 = VGroup(
            Polygon(*square_5_pts, stroke_width=0, fill_color=RED, fill_opacity=1.0),
            MathTex('c^2', font_size=32, z_index=9).set_x(3.5 * scale_factor).set_y(-10.5 * scale_factor),
        )

        # 定义三条虚线
        dash_3_pts = np.array([[-36, -11, 0], [3, 41, 0]]) * scale_factor
        dash_3 = DashedLine(*dash_3_pts, stroke_width=2)

        dash_4_pts = np.array([[52, -2, 0], [-4, 40, 0]]) * scale_factor
        dash_4 = DashedLine(*dash_4_pts, stroke_width=2)

        dash_0_pts = np.array([[0, 41, 0], [0, -29, 0]]) * scale_factor
        dash_0 = DashedLine(*dash_0_pts, stroke_width=2)

        # 定义移动用半透明直角三角形
        right_triangle_shadow = Polygon(*right_triangle_pts, stroke_width=0, fill_color=BLUE_A, fill_opacity=0.5)

        # 定义变换用半透明小正方形
        square_3_shadow = Polygon(*square_3_pts, stroke_width=0, fill_color=PURPLE_A, fill_opacity=0.5)

        # 定义变换用半透明小平行四边形
        parallelogram_3_pts = np.array([[-9, 0, 0], [0, 12, 0], [0, 37, 0], [-9, 25, 0]]) * scale_factor
        parallelogram_3 = VGroup(
            Polygon(*parallelogram_3_pts, stroke_width=0, fill_color=PURPLE_A, fill_opacity=0.5),
            MathTex('a^2', font_size=32, z_index=9).set_x(-4.5 * scale_factor).set_y(18.5 * scale_factor),
        )

        # 定义变换用半透明小长方形
        rectangle_3_pts = np.array([[-9, 0, 0], [0, 0, 0], [0, 25, 0], [-9, 25, 0]]) * scale_factor
        rectangle_3 = VGroup(
            Polygon(*rectangle_3_pts, stroke_width=0, fill_color=PURPLE_A, fill_opacity=0.5),
            MathTex('a^2', font_size=32, z_index=9).set_x(-4.5 * scale_factor).set_y(12.5 * scale_factor),
        )

        # 定义变换用下方半透明小长方形
        rectangle_3_drop_pts = np.array([[-9, -25, 0], [0, -25, 0], [0, 0, 0], [-9, 0, 0]]) * scale_factor
        rectangle_3_drop = VGroup(
            Polygon(*rectangle_3_drop_pts, stroke_width=0, fill_color=PURPLE_A, fill_opacity=0.5),
            MathTex('a^2', font_size=32, z_index=9).set_x(-4.5 * scale_factor).set_y(-16 * scale_factor),
        )

        # 定义变换用半透明大正方形
        square_4_shadow = Polygon(*square_4_pts, stroke_width=0, fill_color=GREEN_A, fill_opacity=0.5)

        # 定义变换用半透明大平行四边形
        parallelogram_4_pts = np.array([[0, 12, 0], [16, 0, 0], [16, 25, 0], [0, 37, 0]]) * scale_factor
        parallelogram_4 = VGroup(
            Polygon(*parallelogram_4_pts, stroke_width=0, fill_color=GREEN_A, fill_opacity=0.5),
            MathTex('b^2', font_size=32, z_index=9).set_x(8 * scale_factor).set_y(18.5 * scale_factor),
        )

        # 定义变换用半透明大长方形
        rectangle_4_pts = np.array([[0, 0, 0], [16, 0, 0], [16, 25, 0], [0, 25, 0]]) * scale_factor
        rectangle_4 = VGroup(
            Polygon(*rectangle_4_pts, stroke_width=0, fill_color=GREEN_A, fill_opacity=0.5),
            MathTex('b^2', font_size=32, z_index=9).set_x(8 * scale_factor).set_y(12.5 * scale_factor),
        )

        # 定义变换用半透明下方大长方形
        rectangle_4_drop_pts = np.array([[0, -25, 0], [16, -25, 0], [16, 0, 0], [0, 0, 0]]) * scale_factor
        rectangle_4_drop = VGroup(
            Polygon(*rectangle_4_drop_pts, stroke_width=0, fill_color=GREEN_A, fill_opacity=0.5),
            MathTex('b^2', font_size=32, z_index=9).set_x(8 * scale_factor).set_y(-16 * scale_factor),
        )

        # 定义勾股定理公式
        formula = MathTex('a^2 + b^2 = c^2', font_size=32).set_x(1 * scale_factor).set_y(-32 * scale_factor)

        # 定义一键三连图标
        thumb = SVGMobject(file_name='./svg/thumb.svg', height=0.5, width=0.5,
                           stroke_width=2, stroke_color=YELLOW
                           ).set_x(32 * scale_factor).set_y(-32 * scale_factor)
        coin = SVGMobject(file_name='./svg/coin.svg', height=0.5, width=0.5,
                          stroke_width=2, stroke_color=YELLOW
                          ).set_x(40 * scale_factor).set_y(-32 * scale_factor)
        fav = SVGMobject(file_name='./svg/fav.svg', height=0.5, width=0.5,
                         stroke_width=2, stroke_color=YELLOW
                         ).set_x(48 * scale_factor).set_y(-32 * scale_factor)

        # 绘制起始标题
        self.play(Write(title, run_time=step_time))
        self.play(FadeOut(title))

        # 绘制直角三角形
        self.play(Create(right_triangle, run_time=step_time))
        self.play(Write(side_a))
        self.play(Write(side_b))
        self.play(Write(side_c))

        # 绘制正方形
        self.play(Create(square_3, run_time=step_time))
        self.play(Create(square_4, run_time=step_time))
        self.play(Create(square_5, run_time=step_time))

        # 绘制虚线
        self.play(Create(dash_3, run_time=step_time))
        self.play(Create(dash_4, run_time=step_time))
        self.play(Create(dash_0, run_time=step_time))

        # 旋转移动直角三角形
        self.play(Transform(side_a_shadow, side_a_twin, run_time=step_time))
        self.play(Transform(side_b_shadow, side_b_twin, run_time=step_time))
        self.add(right_triangle_shadow)
        self.play(Rotate(right_triangle_shadow, angle=PI / 2, about_point=np.array([0, 12, 0]) * scale_factor))
        self.play(MoveAlongPath(right_triangle_shadow,
                                Line(*np.array([[6, 15.5, 0], [-6, 24.5, 0]]) * scale_factor),
                                run_time=step_time))
        self.play(Transform(side_c_shadow, side_c_twin, run_time=step_time))
        self.play(FadeOut(right_triangle_shadow, side_a_shadow, side_b_shadow, run_time=step_time))

        # 变换小正方形
        self.add(square_3_shadow)
        self.play(ReplacementTransform(square_3_shadow, parallelogram_3, run_time=step_time))
        self.play(ReplacementTransform(parallelogram_3, rectangle_3, run_time=step_time))
        self.play(ReplacementTransform(rectangle_3, rectangle_3_drop, run_time=step_time))

        # 变换大正方形
        self.add(square_4_shadow)
        self.play(ReplacementTransform(square_4_shadow, parallelogram_4, run_time=step_time))
        self.play(ReplacementTransform(parallelogram_4, rectangle_4, run_time=step_time))
        self.play(ReplacementTransform(rectangle_4, rectangle_4_drop, run_time=step_time))

        # 绘制公式
        self.play(Write(formula, run_time=step_time))

        # 绘制一键三连图标
        self.play(Indicate(thumb, run_time=step_time / 2))
        self.play(Indicate(coin, run_time=step_time / 2))
        self.play(Indicate(fav, run_time=step_time / 2))

        # 延迟结束
        self.wait(step_time * 2)


if __name__ == '__main__':
    with tempconfig(dict(
        quality='fourk_quality',
        frame_rate=60,
        resolution='1080p',
        output_file='pythagorean_theorem_animation.mp4'
    )):
        movie = PythagoreanTheorem()
        movie.render()
