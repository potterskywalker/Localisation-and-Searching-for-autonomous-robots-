import numpy as np
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt

from matplotlib import animation, rc
from IPython.display import HTML, Image
import seaborn # for background grid
seaborn.set()

class ParticlesPlot:
    
    def __init__(self, world_size):
        rc('animation', html='html5')

        self.fig, self.ax = plt.subplots()
        self.frames = []
        self.scat = None
        self.robotLine = None
        self.world_size = world_size
        

    def render_anim(self, interval=400):    
        return animation.FuncAnimation(self.fig, self.update_frame, init_func=self.setup_plot,
                                       frames=self.frames, interval=interval, blit=True)    

    def capture(self, myrobot, particles, weights, landmarks, passDescription):
        """Records the frame for future animation
        Example: plot.capture(None, p, w, landmarks, "original")"""

        self.frames.append((myrobot, particles, weights, landmarks, passDescription))
    
    def setup_plot(self):
        axis = (-(self.world_size / 2.), self.world_size * 1.5)
        self.ax.set_xlim(axis)
        self.ax.set_ylim(axis)
        
        minX = float('inf')
        minY = float('inf')
        maxX = float('-inf')
        maxY = float('-inf')
        for frame in self.frames:
            particles = frame[1]
            for p in particles:
                minX = min(minX, p.x)
                maxX = max(maxX, p.x)
                
                minY = min(minY, p.y)
                maxY = max(maxY, p.y)

        self.ax.set_xlim((minX - 10., maxX + 10.))
        self.ax.set_ylim((minY - 10., maxY + 10.))
        
        return self.update_frame(self.frames[0])
        
    def update_frame(self, frame):
        myrobot, particles, weights, landmarks, passDescription = frame
        if passDescription:
            self.ax.set_xlabel(passDescription)
        
        x = []
        y = []
        area = []
        colors = []
        normalizedWeights = weights / np.linalg.norm(weights)
        for i, p in enumerate(particles):
            x.append(p.x)
            y.append(p.y)
            area.append(1)

        for l in landmarks:
            x.append(l[0])
            y.append(l[1])
            area.append(10)
            
        if myrobot is robot:
            x.append(myrobot.x)
            y.append(myrobot.y)
            area.append(15)
        elif myrobot is list:
            x.append(myrobot[0])
            x.append(myrobot[1])
            area.append(15)
        else:
            pos = get_position(particles)
            self.drawRobot(pos[0], pos[1], pos[2])
#             x.append(pos[0])
#             y.append(pos[1])
#             area.append(15)

        if self.scat:
            update = np.c_[x,y]
            self.scat.set_offsets(update)
        else:
            self.scat = self.ax.scatter(x, y, s=area)

        return self.scat, self.robotLine,
    
    def drawRobot(self, x, y, orientation, length = 10, width=5):

        endx = x + length * cos(orientation)
        endy = y + length * sin(orientation)

        lineX = [x, endx]
        lineY = [y, endy]
        if self.robotLine:
            self.robotLine.set_data(lineX, lineY)
        else:
            self.robotLine, = self.ax.plot(lineX, lineY, 'r-', linewidth=width)
