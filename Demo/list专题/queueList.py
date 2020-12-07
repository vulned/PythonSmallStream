#from collections import deque
import collections

x_left = []
x_right = []

x_left.append(1)
x_left.append(2)

for i in range(3,10):
    x_left.append(i)
print (x_left)

x_right.append(x_left.pop()) 

print(x_left)

print(x_right)

print('-----------------------------------------------')
queue = collections.deque(["Eric", "John", "Michael", "YuanShuai", "MaoZedong"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
'Eric'
queue.popleft()                 # The second to arrive now leaves
'John'
print(queue)                    # Remaining queue in order of arrival
