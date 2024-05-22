import numpy as np
a = np.matrix( [[6,5],[10,20]] )
b = np.matrix( [[60],[150]] )
x = np.linalg.solve(a,b)
z = (500*x[0]+450*x[1])

b_adjust = np.matrix( [[62],[150]] )
x_adjust = np.linalg.solve(a,b_adjust)
z_adjust = (500*x_adjust[0]+450*x_adjust[1])

print('The final x1 and x2 and z is :'+str(x_adjust[0])+str(x_adjust[1])+str(z_adjust))
print('The Shadow Price is :'+str(z_adjust-z))
