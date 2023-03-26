from manim import *


class FractionSplitAnimation(Scene):
    def construct(self):
        step_time = 2.8
        w, h = config.frame_width, config.frame_height
        pl = w / 24
        align_left = w / 2 - pl
        mr = 0.2

        # 起始标题
        title = Text('动画演示分数裂项方法的应用', font_size=64)
        self.play(Write(title, run_time=step_time))
        self.play(FadeOut(title, run_time=step_time))

        # 题目1
        q1_str = (
                r'\text{题目: }' +
                ' + '.join(
                    [
                        rf'\frac{{ 1 }}{{ {i} \times {i + 1} }}'
                        for i in range(1, 4)
                    ] +
                    [r'\ldots'] +
                    [
                        rf'\frac{{ 1 }}{{ {i} \times {i + 1} }}'
                        for i in range(2021, 2023)
                    ]
                )
        )
        q1 = MathTex(q1_str, tex_template=TexTemplateLibrary.ctex, font_size=32, should_center=False)
        q1.set_x(
            q1.width / 2
            - align_left
        ).set_y(3)
        self.play(Create(q1, run_time=step_time))

        # 解答1
        a1_pre = MathTex(r'\text{解：原式}', tex_template=TexTemplateLibrary.ctex, font_size=32)
        a1_pre.set_x(
            a1_pre.width / 2
            - align_left
        ).set_y(2)
        self.play(Create(a1_pre, run_time=step_time))

        a1_1_1 = MathTex(r'= \frac{ 1 }{ 1 \times 2 }', tex_template=TexTemplateLibrary.ctex, font_size=32)
        a1_1_1.set_x(
            a1_1_1.width / 2
            - align_left
            + a1_pre.width + mr
        ).set_y(2)
        self.play(Create(a1_1_1, run_time=step_time))

        a1_1_2 = MathTex(r'= \frac{2 - 1}{ 1 \times 2 }', tex_template=TexTemplateLibrary.ctex, font_size=32)
        a1_1_2.set_x(
            a1_1_2.width / 2
            - align_left
            + a1_pre.width + mr
        ).set_y(2)
        a1_1_2_shadow = a1_1_2.copy()
        self.play(TransformMatchingTex(a1_1_1, a1_1_2, run_time=step_time))

        a1_1_3 = MathTex(r'+ \,\, \frac{ 1 }{ 2 \times 3 }', tex_template=TexTemplateLibrary.ctex, font_size=32)
        a1_1_3.set_x(
            a1_1_3.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_1_2.width + mr
        ).set_y(2)
        self.play(Create(a1_1_3, run_time=step_time))

        a1_1_4 = MathTex(r'+ \,\, \frac{ 3 - 2 }{ 2 \times 3 }', tex_template=TexTemplateLibrary.ctex, font_size=32)
        a1_1_4.set_x(
            a1_1_4.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_1_2.width + mr
        ).set_y(2)
        a1_1_4_shadow = a1_1_4.copy()
        self.play(TransformMatchingTex(a1_1_3, a1_1_4, run_time=step_time))

        a1_1_5 = MathTex(r'+ \,\, \frac{ 1 }{ 3 \times 4 }', tex_template=TexTemplateLibrary.ctex, font_size=32)
        a1_1_5.set_x(
            a1_1_5.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_1_2.width + mr
            + a1_1_4.width + mr
        ).set_y(2)
        self.play(Create(a1_1_5, run_time=step_time))

        a1_1_6 = MathTex(r'+ \,\, \frac{ 4 - 3 }{ 3 \times 4 }', tex_template=TexTemplateLibrary.ctex, font_size=32)
        a1_1_6.set_x(
            a1_1_6.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_1_2.width + mr
            + a1_1_4.width + mr
        ).set_y(2)
        a1_1_6_shadow = a1_1_6.copy()
        self.play(TransformMatchingTex(a1_1_5, a1_1_6, run_time=step_time))

        a1_1_7 = MathTex(r'+ \,\, \ldots', tex_template=TexTemplateLibrary.ctex, font_size=32)
        a1_1_7.set_x(
            a1_1_7.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_1_2.width + mr
            + a1_1_4.width + mr
            + a1_1_6.width + mr
        ).set_y(2)
        self.play(Create(a1_1_7, run_time=step_time))

        a1_1_8 = MathTex(r'+ \,\, \frac{ 1 }{ 2021 \times 2022 }', tex_template=TexTemplateLibrary.ctex, font_size=32)
        a1_1_8.set_x(
            a1_1_8.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_1_2.width + mr
            + a1_1_4.width + mr
            + a1_1_6.width + mr
            + a1_1_7.width + mr
        ).set_y(2)
        self.play(Create(a1_1_8, run_time=step_time))

        a1_1_9 = MathTex(r'+ \,\, \frac{ 2022 - 2021 }{ 2021 \times 2022 }', tex_template=TexTemplateLibrary.ctex,
                         font_size=32)
        a1_1_9.set_x(
            a1_1_9.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_1_2.width + mr
            + a1_1_4.width + mr
            + a1_1_6.width + mr
            + a1_1_7.width + mr
        ).set_y(2)
        a1_1_9_shadow = a1_1_9.copy()
        self.play(TransformMatchingTex(a1_1_8, a1_1_9, run_time=step_time))

        a1_1_10 = MathTex(r'+ \,\, \frac{ 1 }{ 2022 \times 2023 }', tex_template=TexTemplateLibrary.ctex, font_size=32)
        a1_1_10.set_x(
            a1_1_10.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_1_2.width + mr
            + a1_1_4.width + mr
            + a1_1_6.width + mr
            + a1_1_7.width + mr
            + a1_1_9.width + mr
        ).set_y(2)
        self.play(Create(a1_1_10, run_time=step_time))

        a1_1_11 = MathTex(r'+ \,\, \frac{ 2023 - 2022 }{ 2022 \times 2023 }', tex_template=TexTemplateLibrary.ctex,
                          font_size=32)
        a1_1_11.set_x(
            a1_1_11.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_1_2.width + mr
            + a1_1_4.width + mr
            + a1_1_6.width + mr
            + a1_1_7.width + mr
            + a1_1_9.width + mr
        ).set_y(2)
        a1_1_11_shadow = a1_1_11.copy()
        self.play(TransformMatchingTex(a1_1_10, a1_1_11, run_time=step_time))

        a1_2_2 = MathTex(r'= \frac{ 1 }{ 1 } - \frac{ 1 }{ 2 }', tex_template=TexTemplateLibrary.ctex, font_size=32)
        a1_2_2.set_x(
            a1_2_2.width / 2
            - align_left
            + a1_pre.width + mr
        ).set_y(1)
        self.play(TransformMatchingTex(a1_1_2_shadow, a1_2_2, run_time=step_time))

        a1_2_4 = MathTex(r'+ \,\, \frac{ 1 }{ 2 } - \frac{ 1 }{ 3 }', tex_template=TexTemplateLibrary.ctex,
                         font_size=32)
        a1_2_4.set_x(
            a1_2_4.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_2_2.width + mr
        ).set_y(1)
        self.play(TransformMatchingTex(a1_1_4_shadow, a1_2_4, run_time=step_time))

        a1_2_6 = MathTex(r'+ \,\, \frac{ 1 }{ 3 } - \frac{ 1 }{ 4 }', tex_template=TexTemplateLibrary.ctex,
                         font_size=32)
        a1_2_6.set_x(
            a1_2_6.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_2_2.width + mr
            + a1_2_4.width + mr
        ).set_y(1)
        self.play(TransformMatchingTex(a1_1_6_shadow, a1_2_6, run_time=step_time))

        a1_2_7 = MathTex(r'+ \,\, \ldots', tex_template=TexTemplateLibrary.ctex, font_size=32)
        a1_2_7.set_x(
            a1_2_7.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_2_2.width + mr
            + a1_2_4.width + mr
            + a1_2_6.width + mr
        ).set_y(1)
        self.play(Create(a1_2_7, run_time=step_time))

        a1_2_9 = MathTex(r'+ \,\, \frac{ 1 }{ 2021 } - \frac{ 1 }{ 2022 }', tex_template=TexTemplateLibrary.ctex,
                         font_size=32)
        a1_2_9.set_x(
            a1_2_9.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_2_2.width + mr
            + a1_2_4.width + mr
            + a1_2_6.width + mr
            + a1_2_7.width + mr
        ).set_y(1)
        self.play(TransformMatchingTex(a1_1_9_shadow, a1_2_9, run_time=step_time))

        a1_2_11 = MathTex(r'+ \,\, \frac{ 1 }{ 2022 } - \frac{ 1 }{ 2023 }', tex_template=TexTemplateLibrary.ctex,
                          font_size=32)
        a1_2_11.set_x(
            a1_2_11.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_2_2.width + mr
            + a1_2_4.width + mr
            + a1_2_6.width + mr
            + a1_2_7.width + mr
            + a1_2_9.width + mr
        ).set_y(1)
        self.play(TransformMatchingTex(a1_1_11_shadow, a1_2_11, run_time=step_time))

        a1_3_1 = MathTex(r'= 1', tex_template=TexTemplateLibrary.ctex, font_size=32)
        a1_3_1.set_x(
            a1_3_1.width / 2
            - align_left +
            a1_pre.width + mr
        ).set_y(0)
        self.play(Create(a1_3_1, run_time=step_time))

        a1_3_2 = MathTex(r'- \,\, \frac{ 1 }{ 2 } + \frac{ 1 }{ 2 }', tex_template=TexTemplateLibrary.ctex,
                         font_size=32)
        a1_3_2.set_x(
            a1_3_2.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_3_1.width + mr
        ).set_y(0)
        self.play(FadeIn(a1_3_2, run_time=step_time))
        self.play(FadeOut(a1_3_2, run_time=step_time))

        a1_3_3 = MathTex(r'- \,\, \frac{ 1 }{ 3 } + \frac{ 1 }{ 3 }', tex_template=TexTemplateLibrary.ctex,
                         font_size=32)
        a1_3_3.set_x(
            a1_3_3.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_3_1.width + mr
            + a1_3_2.width + mr
        ).set_y(0)
        self.play(FadeIn(a1_3_3, run_time=step_time))
        self.play(FadeOut(a1_3_3, run_time=step_time))

        a1_3_4 = MathTex(r'- \,\, \frac{ 1 }{ 4 } + \frac{ 1 }{ 4 }', tex_template=TexTemplateLibrary.ctex,
                         font_size=32)
        a1_3_4.set_x(
            a1_3_4.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_3_1.width + mr
            + a1_3_2.width + mr
            + a1_3_3.width + mr
        ).set_y(0)
        self.play(FadeIn(a1_3_4, run_time=step_time))
        self.play(FadeOut(a1_3_4, run_time=step_time))

        # a1_3_5 = MathTex(r'+ \,\, \ldots', tex_template=TexTemplateLibrary.ctex,
        #                  font_size=32)
        # a1_3_5.set_x(
        #     a1_3_3.width / 2
        #     - align_left
        #     + a1_pre.width + mr
        #     + a1_3_1.width + mr
        #     + a1_3_2.width + mr
        #     + a1_3_3.width + mr
        #     + a1_3_4.width + mr
        # ).set_y(0)
        # self.play(FadeIn(a1_3_5, run_time=step_time))
        # self.play(FadeOut(a1_3_5, run_time=step_time))

        a1_3_6 = MathTex(r'- \,\, \frac{ 1 }{ 2021 } + \frac{ 1 }{ 2021 }', tex_template=TexTemplateLibrary.ctex,
                         font_size=32)
        a1_3_6.set_x(
            a1_3_6.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_3_1.width + mr
            + a1_3_2.width + mr
            + a1_3_3.width + mr
            + a1_3_4.width + mr
            # + a1_3_5.width + mr
        ).set_y(0)
        self.play(FadeIn(a1_3_6, run_time=step_time))
        self.play(FadeOut(a1_3_6, run_time=step_time))

        a1_3_7 = MathTex(r'- \,\, \frac{ 1 }{ 2022 } + \frac{ 1 }{ 2022 }', tex_template=TexTemplateLibrary.ctex,
                         font_size=32)
        a1_3_7.set_x(
            a1_3_7.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_3_1.width + mr
            + a1_3_2.width + mr
            + a1_3_3.width + mr
            + a1_3_4.width + mr
            # + a1_3_5.width + mr
            + a1_3_6.width + mr
        ).set_y(0)
        self.play(FadeIn(a1_3_7, run_time=step_time))
        self.play(FadeOut(a1_3_7, run_time=step_time))

        a1_3_8 = MathTex(r'- \,\, \frac{ 1 }{ 2023 }', tex_template=TexTemplateLibrary.ctex,
                         font_size=32)
        a1_3_8.set_x(
            a1_3_8.width / 2
            - align_left
            + a1_pre.width + mr
            + a1_3_1.width + mr
            + a1_3_2.width + mr
            + a1_3_3.width + mr
            + a1_3_4.width + mr
            # + a1_3_5.width + mr
            + a1_3_6.width + mr
            + a1_3_7.width + mr
        ).set_y(0)
        self.play(Create(a1_3_8, run_time=step_time))
        a1_3_8_path = Line(
            [
                a1_3_8.width / 2
                - align_left
                + a1_pre.width + mr
                + a1_3_1.width + mr
                + a1_3_2.width + mr
                + a1_3_3.width + mr
                + a1_3_4.width + mr
                # + a1_3_5.width + mr
                + a1_3_6.width + mr
                + a1_3_7.width + mr,
                0, 0
            ],
            [
                a1_3_8.width / 2
                - align_left
                + a1_pre.width + mr
                + a1_3_1.width + mr,
                0, 0
            ]
        )
        self.play(MoveAlongPath(a1_3_8, a1_3_8_path, run_time=step_time))

        a1_4_1 = MathTex(r'= \frac{ 2022 }{ 2023 }', tex_template=TexTemplateLibrary.ctex, font_size=32)
        a1_4_1.set_x(
            a1_4_1.width / 2
            - align_left
            + a1_pre.width + mr
        ).set_y(-1)
        self.play(Create(a1_4_1, run_time=step_time))

        self.wait(step_time)

        # 一键三连图标
        thumb = SVGMobject(file_name='./svg/thumb.svg', height=0.5, width=0.5,
                           stroke_width=2, stroke_color=YELLOW
                           ).set_x(-1).set_y(-3)
        coin = SVGMobject(file_name='./svg/coin.svg', height=0.5, width=0.5,
                          stroke_width=2, stroke_color=YELLOW
                          ).set_x(0).set_y(-3)
        fav = SVGMobject(file_name='./svg/fav.svg', height=0.5, width=0.5,
                         stroke_width=2, stroke_color=YELLOW
                         ).set_x(1).set_y(-3)
        self.play(Indicate(thumb, run_time=step_time / 2))
        self.play(Indicate(coin, run_time=step_time / 2))
        self.play(Indicate(fav, run_time=step_time / 2))

        # 延迟结束
        self.wait(step_time)


if __name__ == '__main__':
    with tempconfig(dict(
            quality='fourk_quality',
            frame_width=16,
            frame_height=9,
            frame_rate=60,
            resolution='1080p',
            output_file='fraction_split_animation.mp4'
    )):
        print(config.frame_width, config.frame_height)
        movie = FractionSplitAnimation()
        movie.render()
