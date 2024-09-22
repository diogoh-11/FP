import sys
from ezgraphics import GraphicsWindow

def circle(canvas, x, y, r):
   """Draw a filled circle with center (x, y) and radius r."""
   canvas.drawOval(x-r, y-r, 2*r, 2*r)

# Draw a Mickey fractal with n levels.
# n=1 produces a circle, n=2 produces a familiar face.
def mickeyFractal(canvas, x, y, r, n):
   # The largest circle has center (x, y) and radius r.
   circle(canvas, x, y, r)
   
   if n > 1:
        left_ear_x = x - int(r * 1.5)
        left_ear_y = y - r

        right_ear_x = x + int(r * 0.5)
        right_ear_y = y - r

        # Draw smaller circles (ears) outside the main circle
        mickeyFractal(canvas, left_ear_x, left_ear_y, r // 2, n-1)  # Left ear
        mickeyFractal(canvas, right_ear_x, right_ear_y, r // 2, n-1)  # Right ear 

def main():
   UNIT = 32

   win = GraphicsWindow(4*UNIT, 4+3*UNIT)
   canvas = win.canvas()
   canvas.setColor("cyan")
   canvas.setOutline("black")

   n = int(sys.argv[1])
   mickeyFractal(canvas, 2*UNIT, 2*UNIT, UNIT, n)
 
   win.wait()

main()