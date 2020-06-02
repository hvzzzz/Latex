import matplotlib.pyplot as plt
import numpy as np
def sech(t):
    return(1/np.cosh(t))
t = np.arange(-10.0, 10.0, 0.001)#[np.newaxis] este es para poder sacarle la transpuesta a 
#s = np.tanh(t)/((1+np.power(np.tanh(t),2) )*(np.power(np.cosh(t),2)))

s = ((1+np.power(np.tanh(t),2) )*(np.power(np.cosh(t),2)))/np.tanh(t)
s1=np.arctan(t)
#s=-np.log(np.power(np.tanh(t),2)+1)
#s=-((2*np.power(np.tanh(t),2)*np.power(sech(t),4))/np.power(1+np.power(np.tanh(t),2),2)+np.power(sech(t),4)/(1+np.power(np.tanh(t),2))-2*np.power(np.tanh(t),2)*np.power(sech(t),2)/(1+np.power(np.tanh(t),2)))
#ss=s.T
#print(s)
#print(ss)
#euclidean=np.sqrt(s.dot(ss))
#print(euclidean)
#s=np.sqrt(np.log(np.power(np.tanh(t),2)+1))
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#plt.subplot(1,2,1)
plt.plot(t, s)
plt.grid(True)
plt.xlabel(r'$\tilde{q}$',fontsize=16)
plt.title(r'$\frac{1}{cosh^2(\tilde{q})}\frac{tanh(\tilde{q})}{1+tanh^2(\tilde{q})}$',fontsize=16)
#plt.subplot(1,2,2)
#plt.plot(t, s1)
#plt.grid(True)
#plt.xlabel(r'$\dot{q}$',fontsize=16)
#plt.title(r'$atan(\dot{q})$',fontsize=16)
plt.savefig('sintonia.png',dpi=150)

#s = np.power(np.tanh(t),1)/(np.power(np.sinh(t),1)*np.cosh(t))
#lt.plot(t, s)
#plt.grid(True)
#plt.savefig('done1.png')