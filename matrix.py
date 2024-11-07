from manim import *

# Configure the quality and preview settings
config.media_width = "75%"
config.video_dir = "./videos"

class SimpleScene(Scene):
    def construct(self):
        circle = Circle(radius=2, color=BLUE)
        dot = Dot()
        
        self.add(circle, dot)
        self.play(dot.animate.move_to(circle.point_from_proportion(0)))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.wait()