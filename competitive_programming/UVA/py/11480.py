import math

a = int(input())
r = 1
soma = 1
b = 2
g = a - b - r 
prob = 0
while(a > 0):
	
	while(g > b):
		prob = math.ceil((g-b)/2) + prob
		r += 1
		b = r + 1
		g = a - r - b 
	print("Case %d: %d" %(soma,prob))
	a = int(input())
	soma += 1
	r = 1
	b = 2
	g = a - b - r 
	prob = 0

					
	
