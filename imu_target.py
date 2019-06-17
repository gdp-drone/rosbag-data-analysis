import yaml
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
import statistics 

pos_x = []
pos_y = []

with open("pelham_ground_truth_3.txt", 'r') as stream:
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

# Plot
plt.figure()
plt.grid(True)
plt.title('Raw GPS points around Pelham Crescent')
plt.ylabel('y [m]')
plt.plot(pos_x, pos_y,'ro',label='Raw GPS points')
plt.legend()
plt.savefig('pelham_ground_truth_3.png', transparent=True)