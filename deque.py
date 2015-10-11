from __future__ import division
from collections import deque
import itertools

def moving_average(iterable, n=3):
		it = iter(iterable)
		#since the first 3 elements of it are consumed they are no more there
		d = deque(itertools.islice(it,n-1)) 
		d.appendleft(0)
		s =sum(d)
		for elem in it:
			a = d.popleft()
			s += elem - a
			d.append(elem)
			yield s / n

for i in moving_average([1,2,3,4,5,6,9]):
	print i

d = deque([1,2,3,4])

#pure Python implementation of del d[n] relies on the rotate() method to position elements to be popped:
def delete_nth(d,n):
	d.rotate(-n)
	d.popleft()




