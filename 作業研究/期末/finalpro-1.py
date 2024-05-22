import numpy as np
from gurobipy import *
import pandas as pd
try:
    # We establish two menus here
	B=np.zeros((20,1))
	NB=np.zeros((57,1))
	CB=np.zeros((20,1))
	CNB=np.zeros((57,1))
	HB=np.zeros((20,1))
	HNB=np.zeros((57,1))
	uB=np.zeros((20,1))
	uNB=np.zeros((57,1))
	db = pd.read_excel(r'早餐們.xlsx',sheetname=0)
	dnb=pd.read_excel(r'晚餐們.xlsx',sheetname=0)
	dataB=np.array(db)
	dataNB=np.array(dnb)
	for j in range(len(B[:,0])):
		for w in range(len(B[0])):
			CB[j][w]=dataB[j][2]
			HB[j][w]=dataB[j][3]
	for j in range(len(NB[:,0])):
		for w in range(len(NB[0])):
			CNB[j][w]=dataNB[j][2]
			HNB[j][w]=dataNB[j][3]
    
    # First, please input your basic information
	gender=input("Please input your gender (Male or Female): ")
	age=int(input("Please input your age: "))
	high=float(input("Please input your height(cm): "))
	weight=float(input("Please input your weight(kg): "))
	care=input("Do you care about eating same food in two days row (Y/N): ")
	if (gender=='Male'):
		P=10*high+6.25*weight-5*age+5
	else:
		P=10*high+6.25*weight-5*age-161
	activity=int(input("How many times do you exercise every week(0~5): "))
	if (activity==0):
		H=P
	elif (activity==1):
		H=P*1.2
	elif (activity==2):
		H=P*1.375
	elif (activity==3):
		H=P*1.55
	elif (activity==4):
		H=P*1.725
	elif (activity==5):
		H=P*1.9
	H=H*0.4
	day=int(input("How many days do you want to plan (Please enter an integer): "))
	C=int(input("How many budget do you have(Plese enter an integer): "))
    
    # Second, please choose what you want to eat
	print ("Part one: Breakfast")
	while True :
		i= input("Which restaurant do you want to choose (Please input the integer number of restaurant): ")
		if (i=='q'):
			break
		elif (int(i)>=len(B[:,0])):
			while True:
				i=input("This is invalid input, please input again: ")
				if (int(i)<len(B[:,0])):
					break
		j= input("Which food do you want to eat: ")
		if(int(j)>=len(B[0])):
			while True:
				j=input("This is invalid input, please input again (Please input the integer number of food): ")
				if (int(j)<len(B[0])):
					break
		else:
			B[int(i)][int(j)]=1
			u=input("Please input your preference for this food（1~5): ")
			uB[int(i)][int(j)]=int(u)
	print("Part two: Lunch and Dinner")
	while True :
		i= input("Which restaurant do you want to choose (Please input the integer number of restaurant): ")
		if (i=='q'):
			break
		elif (int(i)>=len(NB[:,0])):
			while True:
				i=input("This is invalid input, please input again: ")
				if (int(i)<len(NB[:,0])):
					break
		j= input("Which food do you want to eat (Please input the integer number of food): ")
		if(int(j)>=len(NB[0])):
			while True:
				j=input("This is invalid input, please input again: ")
				if (int(j)<len(NB[0])):
					break
		else:
			NB[int(i)][int(j)]=1
			u=input("Please input your reference for this food（1~5): ")
			uNB[int(i)][int(j)]=int(u)
	
	m = Model("Final")
	EBij={}
	ENBij={}
	for i in range (day):
		for j in range(len(B[:,0])):
			for w in range(len(B[0])):
				EBij[i,j,w] = m.addVar(vtype=GRB.BINARY,name='EB_%d_%d_%d' % (i, j,w))
		for j in range(len(NB[:,0])):
			for w in range(len(NB[0])):
				ENBij[i,j,w]=m.addVar(vtype=GRB.BINARY,name='ENB_%d_%d_%d' % (i, j,w))
	m.update()
	for x in range (day):
		m.addConstr((quicksum(HB[i][j]*B[i][j]*EBij[x,i,j] for i in range(len(B[:,0])) for j in range (len(B[0])))+quicksum(HNB[i][j]*NB[i][j]*ENBij[x,i,j] for i in range(len(NB[:,0])) for j in range (len(NB[0]))))>=H)
		m.addConstr(quicksum(B[i][j]*EBij[x,i,j] for i in range(len(B[:,0])) for j in range (len(B[0])))==1)
		m.addConstr(quicksum(NB[i][j]*ENBij[x,i,j] for i in range(len(NB[:,0])) for j in range (len(NB[0])))==2)
	m.addConstr(quicksum((quicksum(CB[i][j]*B[i][j]*EBij[x,i,j] for i in range(len(B[:,0])) for j in range (len(B[0])))+quicksum(CNB[i][j]*NB[i][j]*ENBij[x,i,j] for i in range(len(NB[:,0])) for j in range (len(NB[0]))))for x in range (day))<=C)
	m.update()
	if (care=='Y'):
		for k in range (day):
			for i in range (len(B[:,0])):
				for j in range (len(B[0])):
					m.addConstr(B[i][j]*EBij[k,i,j] != B[i][j]*EBij[k+1,i,j])
			for i in range (len(NB[:,0])):
				for j in range (len(NB[0])):
					m.addConstr(NB[i][j]*ENBij[k,i,j] != NB[i][j]*ENBij[k+1,i,j])
	m.setObjective((quicksum((quicksum(uB[i][j]*B[i][j]*EBij[x,i,j] for i in range(len(B[:,0])) for j in range (len(B[0])))+quicksum(uNB[i][j]*NB[i][j]*ENBij[x,i,j] for i in range(len(NB[:,0])) for j in range(len(NB[0])))) for x in range (day))), GRB.MAXIMIZE)
	m.update()
	m.optimize()
	print('Optimal:')
	for v in m.getVars():
		if(v.x==1):
			print('%s: %f' % (v.VarName, v.x))
	print('Obj: %f' % m.objVal)

except GurobiError:
    print ('Error reported')