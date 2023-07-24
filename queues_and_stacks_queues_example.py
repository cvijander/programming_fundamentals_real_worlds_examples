import queue
# new q  queue is module , but Queue is constructor 

q =queue.Queue()
print()
print('Is it queue is empty  ')
print(q.empty())


print('insert bag')

q.put('bag1')
print()
print('is it empty')
print(q.empty())


print()
print('insert bag')
q.put('bag2')
print('insert bag')
q.put('bag3')

print()
print('lose a bag')
print(q.get())

print(q.get())
print(q.get())
#print(q.get())

