"""

Complex_Numbers.py : A module that implements basic complex number operations in python.
python version : python 2.7.x
author : Mohd Sanad Zaki Rizvi
contact : mohdsanadzakirizvi@gmail.com
license : GPL-3

"""
from __future__ import division
import numpy as np

class Complex:
	#parameterised constructor
	def __init__(self, a=0, b=0):
		self.a = a
		self.b = b

    #str representation
	def __str__(self):
		"""
			Generate string representation of complex number based on imaginary part's sign.
		"""
		st = ""
		if self.b >= 0:
			st = str(self.a)+"+"+str(self.b)+"i"
		else:
			st = str(self.a)+str(self.b)+"i"
		return st
	
	#overloading addition operator 
	def __add__(self, n2):
		temp = Complex()
		try:
			temp.a = self.a + n2.a 
			temp.b = self.b + n2.b
		except AttributeError:
			"""
				Complex object + int or float Eg. c1+8 should add
				c1's real part by 8.
			"""
			if type(n2) == int or type(n2) == float:
				temp.a = self.a + n2
				temp.b = self.b
			else:
				return "Invalid Type"
		return temp

	#overloading substraction operator
	def __sub__(self, n2):
		temp = Complex()
		try:
			temp.a = self.a - n2.a 
			temp.b = self.b - n2.b
		except AttributeError:
			"""
				Complex object - int or float Eg. c1-8 should substract
				c1's real part by 8.
			"""
			if type(n2) == int or type(n2) == float:
				temp.a = self.a - n2
				temp.b = self.b
			else:
				return "Invalid Type"
		return temp

    #overloading multiplication operator
	def __mul__(self, n2):
		temp = Complex()
		try:
			c, d = n2.a, n2.b
			temp.a = (self.a*c) - (self.b*d)
			temp.b = (self.a*d) + (self.b*c)
	
		except AttributeError:
			"""
				Complex object * int or float Eg. c1*8 should multiply
				c1's real part by 8.
			"""
			if type(n2) == int or type(n2) == float:
				temp.a = self.a * n2
				temp.b = self.b * n2
			else:
				return "Invalid Type"
		return temp

    #overloading division operator 
	def __div__(self, n2):
		temp = Complex()
		try:
			"""
				If second complex no is zero, raise exception.
			"""
			c, d = n2.a, n2.b
			if c == 0 and d == 0:
				raise Exception("Second complex number cannot be zero")
			denom = c**2 + d**2
			temp.a = (self.a*c + self.b*d) / denom
			temp.b = -(self.a*d - self.b*c) / denom
	
		except AttributeError:
			"""
				Complex object / int or float Eg. c1/8 should divide.
				c1's real part by 8.
			"""
			if type(n2) == int or type(n2) == float:
				temp.a = self.a / n2
				temp.b = self.b / n2
			else:
				return "Invalid Type"

		except Exception as exp:
			return exp
		return temp

    #overloading absolute operator
	def __abs__(self):
		temp = Complex()
		temp.a = abs(self.a)
		temp.b = abs(self.b)
		return temp

	#real part
	def real(self):
		return self.a

    #imaginary part
	def imag(self):
		return self.b

    #argument of complex no
	def argument(self):
		rad = np.arctan2(self.b, self.a)
		deg = (rad * 180) / np.pi
		return round(deg, 2)

    #conjugate of complex no
	def conjugate(self):
		temp = Complex()
		temp.a = self.a
		temp.b = -self.b
		return temp


