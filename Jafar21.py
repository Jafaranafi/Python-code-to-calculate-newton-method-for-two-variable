import numpy as np
from scipy.linalg import solve
def myFcn(z):
	x, y = z
	return np.array([x**2+y**2-1, x-.5])
def myJac(z):
	x, y = z
	return np.array([[2*x,2*y],[1,0]])
zGuess = np.array([0.5,-1])
print myJac(zGuess)
print myFcn(zGuess)
print 'The inverse of the Jacobian matrix is'
A= np.linalg.inv(myJac(zGuess))
print A
print 'Note that the newton formular is  x[n+1]=x[n]-J(x,y)F(x,y)'
print 'J(x,y)F(x,y)=A.dot(myFcn(zGuess))'
t=A.dot(myFcn(zGuess))
p=zGuess-t
print 'The jacobia iteration is '
print p
Q=list(zGuess)
mylist=[]
for k in range(1,6):
	p=zGuess-t
	zGuess=p
	t=A.dot(myFcn(zGuess))
	mylist.append(p)
	print p

