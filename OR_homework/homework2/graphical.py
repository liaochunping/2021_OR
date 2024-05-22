import matplotlib.pyplot as plt
import numpy as np

#################################################
plt.axis([0, 5, 0, 5]) # x , y axis
plt.xlabel('x1', fontsize=14, color='maroon')
h= plt.ylabel('x2', fontsize=14, color='maroon')
h.set_rotation(0)
plt.title('Operations Research Homework2-2')


##################################################
line1x = np.arange(0, 5, 1) # x1座標從0到8，間隔是1，不含結束點8
line1y = (24 - 6*line1x)/4.0 # 6x + 4y = 24
plt.plot(line1x,line1y,color='r',label = '6x + 4y = 24')
###################################################
line2x = np.arange(0, 8, 1) # x1座標從0到8，間隔是1，不含結束點8
line2y = (6 - line2x)/2     # x + 2y = 6
plt.plot(line2x,line2y,color='g',label = 'x + 2y = 6')
###################################################
line3x = np.arange(0, 8, 1) # x1座標從0到8，間隔是1，不含結束點8
line3y = 1 + line3x         #-x + y = 1
plt.plot(line3x,line3y,color='b',label = '-x + y = 1')
###################################################

plt.axhline(y=2,color='maroon',label = 'y = 2 ') # y = 2 
###################################################

line12left = np.matrix([[6,4],[1,2]])
line12right = np.matrix([[24],[6]])
point12 = np.linalg.solve(line12left,line12right)

line24left = np.matrix([[1,2],[0,1]])
line24right = np.matrix([[6],[2]])
point24 = np.linalg.solve(line24left,line24right)


line34left = np.matrix([[-1,1],[0,1]])
line34right = np.matrix([[1],[2]])
point34 = np.linalg.solve(line34left,line34right)


linex1left = np.matrix([[0,1],[6,4]])
linex1right = np.matrix([[0],[24]])
pointx1 = np.linalg.solve(linex1left,linex1right)

liney3left = np.matrix([[1,0],[-1,1]])
liney3right = np.matrix([[0],[1]])
pointy3 = np.linalg.solve(liney3left,liney3right)

##################################################
plt.plot(point12[0],point12[1],'o',color='b')
plt.plot(point24[0],point24[1],'o',color='r')
plt.plot(point34[0],point34[1],'o',color='g')
plt.plot(pointx1[0],pointx1[1],'o',color='black')
plt.plot(pointy3[0],pointy3[1],'o',color='black')

plt.legend()
plt.show()

##################################################
z=[0]*5
z[0] = 5*3 +4*1.5
z[1] = 5*1 +4*2
z[2] = 5*1 +4*2
z[3] = 5*4 +4*0
z[4] = 5*0 +4*1
maxelement =np.amax(z)
print(point12[0],point12[1],z[0])
print(point24[0],point24[1],z[1])
print(point34[0],point34[1],z[2])
print(pointx1[0],pointx1[1],z[3])
print(pointy3[0],pointy3[1],z[4])
print("the max z is :"+ str(maxelement)+" at point "+str(point12[0])+str(point12[1]))





