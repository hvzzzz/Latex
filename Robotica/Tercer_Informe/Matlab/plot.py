import matplotlib.pyplot as plt
import numpy as np
def sech(t):
    return(1/np.cosh(t))
t = np.arange(-20.0, 20.0, 0.001)#[np.newaxis] este es para poder sacarle la transpuesta a 
#s = np.tanh(t)/((1+np.power(np.tanh(t),2) )*np.power(np.cosh(t),2))
#s=-np.log(np.power(np.tanh(t),2)+1)
s=-(2*np.power(np.tanh(t),2)*np.power(sech(t),4))/np.power(1+np.power(np.tanh(t),2),2)+np.power(sech(t),4)/(1+np.power(np.tanh(t),2))-2*np.power(np.tanh(t),2)*np.power(sech(t),2)/(1+np.power(np.tanh(t),2))
#ss=s.T
#print(s)
#print(ss)
#euclidean=np.sqrt(s.dot(ss))
#print(euclidean)
#s=np.sqrt(np.log(np.power(np.tanh(t),2)+1))
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.plot(t, s)
plt.grid(True)
plt.xlabel(r'$\tilde{q}$',fontsize=16)
plt.ylabel(r'$\frac{1}{cosh^2(\tilde{q})}\frac{tanh(\tilde{q})}{1+tanh^2(\tilde{q})}$',fontsize=16)
plt.savefig('done.png')
#s = np.power(np.tanh(t),1)/(np.power(np.sinh(t),1)*np.cosh(t))
#lt.plot(t, s)
#plt.grid(True)
#plt.savefig('done1.png')