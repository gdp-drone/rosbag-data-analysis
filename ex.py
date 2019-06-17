import yaml
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
import matplotlib.mlab as mlab
from scipy.stats import norm

pos_x = []
pos_y = []

with open("ex_bo.txt", 'r') as stream:
    try:
        docs = yaml.load_all(stream)
        for doc in docs:
        	try:
                    pos_x.append(doc['point']['x'])
                    pos_y.append(doc['point']['y'])
	        except TypeError:
	        	pass
    except yaml.YAMLError as exc:
        print(exc)

# Raw data
pos_x = np.array(pos_x)
pos_y = np.array(pos_y)

# Best fit
pos_x_fit = np.linspace(-24,0)
coeffs = poly.polyfit(pos_x, pos_y, 1)
pos_y_fit = poly.polyval(pos_x_fit, coeffs)

# Plot
plt.figure()
plt.grid(True)
plt.title('Filtered Straight Line Test of OnePlus 3 GPS (Haphazard GPS)')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.plot(pos_x, pos_y,'ro',label='Filtered GPS points')
plt.plot(pos_x_fit, pos_y_fit, 'k',label='Best fit line')
plt.legend()

# Get standard deviation
pos_y_corrected = poly.polyval(pos_x, coeffs)
pos_y_dev = pos_y - pos_y_corrected
(mu, sigma) = norm.fit(pos_y_dev)
print(sigma)

# Plot diff histogram
plt.figure()
n, bins, patches = plt.hist(pos_y_dev, 10, normed=1, alpha=0.75, label='Deviation from best-fit line')

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=2, label='Gaussian best-fit')
plt.xlabel('Deviation from best-fit line [m]')
plt.ylabel('Probability')
plt.grid(True)
plt.legend()
plt.show()