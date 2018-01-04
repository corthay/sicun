#!/usr/bin/env python3
__author__="Ya yifan"
import math
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
		results=[]
		step=self.__default_step
		while True:
			#variable initialization
			x=self.__start
			result=float()

			# differential of the variable x
			dx=(self.__end-self.__start)/step
			while x<=self.__end:
				result+=eval(self.__equation)*dx
				x+=dx

			#judge the precision
			if step!=1 and math.fabs(result-results[-1])<self.__precision:
				break
			results.append(result)
			print(result)	
			step*=2
		return results[-1]

		
		
if __name__ == '__main__':
	equation=input('Enter the equation f(x)=')
	start=input('Enter where the integral start ')
	end=input('Enter where the integral end ')
	print("result ==> {0:.4f}".format((Integral(equation, start, end)())))