import numpy as np
from scipy.linalg import solve

def myFcn(z):
   x, y = z
   return np.array([x**2+y**2-1, x-.5])

def myJac(z):
   x, y = z
   return np.array([[2*x,2*y],[1,0]])

zGuess = np.array([0.5,-1])
zexact = np.array([.5,-np.sqrt(3)/2])
print 'exact ', zexact


print ' '
print 'Newton'
z = zGuess
dz = np.empty(2)
print z
for k in range(6):
    f = -myFcn(z)    
    Df = myJac(z)    
    dz = solve(Df, f)
    z = z + dz
    print z
    
