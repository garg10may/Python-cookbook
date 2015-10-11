
# find the count of each character in message

from pprint import pprint
from collections import Counter, defaultdict

message = 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'

# first method
d={}
for i in message:
	d[i] =  d.get(i,0) +1
print d

#second method
d={}
for i in message:
	d[i] = d.setdefault(i,0) + 1
print  d

# third method
from collections import defaultdict
d = defaultdict(int)
for i in message:
	d[i] +=1
print d

# fourth method
d = Counter()
for i in message:
	d[i] +=1
print d

#fifth method
print Counter(message)

