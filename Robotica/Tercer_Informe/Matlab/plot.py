import matplotlib.pyplot as plt
import numpy as np
t = np.arange(-20.0, 20.0, 0.001)
s = np.tanh(t)/(1+np.tanh(t)*np.tanh(t))
plt.plot(t, s)
plt.grid(True)
plt.savefig('done.png')
s = np.power(np.tanh(t),1)/(np.power(np.sinh(t),1)*np.cosh(t))
plt.plot(t, s)
plt.grid(True)
plt.savefig('done1.png')