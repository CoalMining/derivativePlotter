import sys
from math import *
import matplotlib.pyplot as plt

incrementVal = 0.001

def findDerivative(xArray,minVal,maxval):
	last = 0
	retVal = list()
	for i in range ((maxval-minVal)-1):
		last = (xArray[i+1]-xArray[i])/incrementVal
		retVal.append(last)
	retVal.append(last)
	return retVal

def calcFunction(stringEqn):
	minVal = -10000
	maxVal = 10000
	t = [incrementVal*i for i in range(minVal,maxVal)]
	# print(len(t))
	xArray = list()
	for x in t:
		try:
			xArray.append(eval(stringEqn))
		except:
			print('Please make sure the equation entered is correct')
			exit(0)

	derVal = findDerivative(xArray,minVal,maxVal)
	plt.plot(t,xArray,label='Original Equation')
	plt.plot(t,derVal,label='Derivative Equation')
	plt.legend()
	plt.show()

def main():
	if(len(sys.argv)>1):
		eqn = sys.argv[1]
	else:
		eqn = '4*x**3+5'
	calcFunction(eqn)

if __name__=="__main__":
	main()