import yaml
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
import numpy.polynomial.polynomial as poly

pos_x = []
pos_y = []

with open("filtered_circle2.txt", 'r') as stream:
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

# Mean
pos_x_mean = np.mean(pos_x)
pos_y_mean = np.mean(pos_y)
print(pos_x_mean)
print(pos_y_mean)

# Plot
plt.figure()
plt.grid(True)
plt.title('Filtered Circle Test of OnePlus 3 GPS')
plt.xlabel('x deviation [m]')
plt.ylabel('y deviation [m]')
plt.plot(pos_x, pos_y,'ro',label='Filtered GPS points')
plt.plot(pos_x_mean, pos_y_mean, 'ko',label='Mean')
plt.legend()

# Get standard deviation
distance_array = []
for i in range(len(pos_x)):
    dev_x = pos_x[i] - pos_x_mean
    dev_y = pos_y[i] - pos_y_mean
    dist = np.sqrt(dev_x*dev_x + dev_y*dev_y)
    distance_array.append(dist)

distance_array = np.array(distance_array)

dev_array = distance_array - 5
(mu, sigma) = norm.fit(dev_array)
print(sigma)

# Plot diff histogram
plt.figure()
n, bins, patches = plt.hist(dev_array, 10, normed=1, alpha=0.75, label='Deviation from 5m')

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=2, label='Gaussian best-fit')
plt.xlabel('Deviation from 5m radius [m]')
plt.ylabel('Probability')
plt.grid(True)
plt.legend()
plt.show()