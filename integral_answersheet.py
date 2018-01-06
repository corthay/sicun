#!/usr/bin/env python3
__author__="Ya yifan"
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import sin,cos,tan,pi,e,log,asin,acos,atan,sinh,cosh,tanh,asinh,acosh,atanh
'''
just directly input common mathematical elementary functions and values
like pi,cos(x),sin(x)...
for the mathematical value of pi, you have to input as pi
for nth root, you have to input as x**(1/n)
for logn(x), you have to input as log(x,n)
for Inverse trigonometric functions, you havt to input as asin()
for hyperbolic functions, you have to input as sinh()
for inverse hyperbolic functions, you have to input as asinh()
'''

class Integral:
	'''
	Calculate the integral of the equation

	you must
	input the standard form of the function
	input a finite value to start
	input a upper value to end

	you can 
	input the precision like 0.0001,0.00000001

	the default_step means
	the interval[start,end] will be divided into one or what you input  
	'''
	def __init__(self, equation, start, end,
				precision=0.00001,default_step=1):
		self.__equation=equation
		self.__start=float(start)
		self.__end=float(end)
		self.__precision=precision
		self.__default_step=default_step
		
		#check the equation
		try:
			eval(equation.replace('x', '123'))
		except SyntaxError: # equation not valid In fact, this Error won't happen :)
			print("Unsupported expression!")

	#Calculate
	def __call__(self):	
		results=[]#store results to draw y axis in figure later
		t=0
		time=[]#store time of the calculation to draw x axis in figure
		step=self.__default_step
		while True:
			#variable initialization
			x=self.__start
			result=float()
			
			#differential of the variable x
			
			dx=(self.__end-self.__start)/step
			while x<=self.__end:
				result+=eval(self.__equation)*dx
				x+=dx

			#judge the precision
			if step!=1 and math.fabs(result-results[-1])<self.__precision:
				break
			t+=1
			time.append(t)
			results.append(result)
			step*=2

		#the figure of rusults
		plt.figure('result')
		plt.title('Variation figure of result')
		plt.xlabel('Calculation time')
		plt.ylabel('Result')
		plt.plot(time,results)
		plt.show()
		return results[-1]

		
		
if __name__ == '__main__':
	equation=input('Enter the equation f(x)=')
	start=input('Enter where the integral start ')
	end=input('Enter where the integral end ')
	print("result ==> {0:.4f}".format((Integral(equation, start, end)())))
