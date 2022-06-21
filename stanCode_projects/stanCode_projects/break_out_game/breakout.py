"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics(ball_radius=10)
    global NUM_LIVES
    lives = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        graphics.ball.move(graphics.velocity_x(), graphics.velocity_y())
        graphics.rebound_or_remove()
        if graphics.get_count() == graphics.get_total_count():
            break
        if graphics.ball.x+graphics.ball.width > graphics.window.width:
            graphics.set_velocity_neg_x()
        if graphics.ball.x <= 0:
            graphics.set_velocity_neg_x()
        if graphics.ball.y <= 0:
            graphics.set_velocity_neg_y()
        if graphics.ball.y >= graphics.window.height:
            lives -= 1
            graphics.set_velocity_zero_x()
            graphics.set_velocity_zero_y()
            graphics.reset_ball()
            if lives == 0:
                graphics.set_velocity_zero_x()
                graphics.set_velocity_zero_y()
                graphics.window.add(graphics.game_over())
                break













#detect object and determine to remove or rebound






    # Add the animation loop here!


if __name__ == '__main__':
    main()
