import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('UDP', 'DNS', 'TCP', 'HTTP', 'ARP')
y_pos = np.arange(len(objects))
plt.title('Protocols in Wireshark by Kevin')
plt.xlabel('Usage')

performance = [3, 2, 17, 4, 63]
 
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)

plt.show()