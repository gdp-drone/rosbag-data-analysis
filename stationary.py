import yaml
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
import statistics 

pos_x = []
pos_y = []

with open("stationary_filtered3.txt", 'r') as stream:
    try:
        docs = yaml.load_all(stream)
        for doc in docs:
        	try:
                    pos_x.append(doc['point']['x'] - 11.35)
                    pos_y.append(doc['point']['y'] + 4.9)
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
plt.title('Filtered Stationary Test of OnePlus 3 GPS')
plt.xlabel('x deviation [m]')
plt.ylabel('y deviation [m]')
plt.plot(pos_x, pos_y,'ro',label='filtered GPS points')
plt.plot(pos_x_mean, pos_y_mean, 'ko',label='Mean')
plt.legend()

# Get standard deviation
stdev_x = statistics.stdev(pos_x)
stdev_y = statistics.stdev(pos_y)
print(stdev_x)
print(stdev_y)

# Plot diff histogram
plt.figure()
plt.hist(pos_x)
plt.xlabel('Deviation from x-mean [m]')
plt.ylabel('Count')

plt.figure()
plt.hist(pos_y)
plt.xlabel('Deviation from y-mean [m]')
plt.ylabel('Count')
plt.show()