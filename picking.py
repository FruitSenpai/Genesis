from __future__ import print_function
import matplotlib.pyplot as plt
#from matplotlib.lines import Line2D
#from matplotlib.patches import Rectangle
#from matplotlib.text import Text
#from matplotlib.image import AxesImage
import numpy as np
from numpy.random import rand


if 1:  

    def line_picker(line, mouseevent):
        """
        find the points within a certain distance from the mouseclick in
        data coords and attach some extra attributes, pickx and picky
        which are the data points that were picked
        """
        if mouseevent.xdata is None:
            return False, dict()
        xdata = line.get_xdata()
        ydata = line.get_ydata()
        maxd = 0.05
        d = np.sqrt((xdata - mouseevent.xdata)**2. + (ydata - mouseevent.ydata)**2.)

        index = np.nonzero(np.less_equal(d, maxd))
        if len(index):
            pickx = np.take(xdata, index)
            picky = np.take(ydata, index)
            props = dict(index=index, pickx=pickx, picky=picky)
            return True, props
        else:
            return False, dict()

    def linePick(event):
        print('linePick :', event.pickx, event.picky)

    fig, ax = plt.subplots()
    line, = ax.plot(rand(50), rand(50), 'o', picker=line_picker)
    fig.canvas.mpl_connect('pick_event', linePick)


if 1:  # picking on a scatter plot (matplotlib.collections.RegularPolyCollection)

    x, y, c, s = rand(4, 50)

    def scatterPick(event):
        index = event.ind
        print('scatterPick:', index, np.take(x, index), np.take(y, index))

    fig, ax = plt.subplots()
    col = ax.scatter(x, y, 100*s, c, picker=True)
    fig.canvas.mpl_connect('pick_event', scatterPick)


plt.show()

