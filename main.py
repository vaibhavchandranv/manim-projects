from manim import *
import numpy as np

class yesbanana(Scene):
    def construct(self):

        WHITE_TEXT = WHITE
        CYAN = "#00ffff"
        NEON_GREEN = "#39ff14"

        # intro
        title = Text("happy father's day!", font_size=64, color=WHITE_TEXT)
        subtitle = Text("this is how much i love you", font_size=40, color=WHITE_TEXT).next_to(title, DOWN)
        subsubtitle = Text("(and it's still not close)", font_size=40, color=WHITE_TEXT).next_to(subtitle, DOWN)

        self.play(FadeIn(title, shift=UP))
        self.play(FadeIn(subtitle, shift=UP))
        self.play(FadeIn(subsubtitle, shift=UP))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(subsubtitle))

        # axes
        axes = Axes(
            x_range=[0, 3.5, 1],
            y_range=[0, 120, 20],
            tips=False,
            axis_config={"color": WHITE_TEXT}
        ).scale(0.9).shift(UP * 0.3)

        # steeper exponential (visual impact)
        graph = axes.plot(lambda x: np.exp(1.3 * x), color=NEON_GREEN)

        label = Text(
            "love grows like e^(x).",
            font_size=34,
            color=WHITE_TEXT
        ).to_edge(UP)

        self.play(Create(axes))
        self.play(Create(graph))
        self.play(FadeIn(label))
        self.wait(1.5)

        # infinity statement (kept inside frame)
        infinity = MathTex(
            r"\lim_{x \to \infty} e^{x} = \infty",
            color=WHITE_TEXT
        ).scale(1.15)

        infinity.next_to(axes.c2p(2.2, 70), UP * 0.2)

        self.play(Write(infinity))
        self.wait(2)

        self.play(FadeOut(VGroup(axes, graph, label, infinity)))

        # gratitude section (white)
        line1 = Text(
            "i'm really grateful for everything you've done for me",
            font_size=32,
            color=WHITE_TEXT
        )

        line2 = Text(
            "for letting me explore my interests while keeping me grounded",
            font_size=28,
            color=WHITE_TEXT
        ).next_to(line1, DOWN)

        line3 = Text(
            "and for helping me grow into a better person over the years",
            font_size=28,
            color=WHITE_TEXT
        ).next_to(line2, DOWN)

        self.play(FadeIn(line1))
        self.play(FadeIn(line2))
        self.play(FadeIn(line3))
        self.wait(3)

        self.play(FadeOut(VGroup(line1, line2, line3)))

        # final message (wrapped, cyan, clean)
        final_message = VGroup(
            Text(
                "happy father's day to someone",
                font_size=34,
                color=CYAN
            ),
            Text(
                "the rest of the world could only wish for.",
                font_size=34,
                color=CYAN
            )
        ).arrange(DOWN, center=True)

        self.play(FadeIn(final_message))
        self.wait(3)

        self.play(FadeOut(final_message))