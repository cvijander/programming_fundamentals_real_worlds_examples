# sets 

college  = set(['Bill','Katy','Verne','Dillon','Bruce', 'Olivia','Richard','Jim'])

coworker = set(['Aaron','Bill','Brandon','David','Frank','Conne','Kyle','Olivia'])

family = set (['Garry','Landon','Larry','Mark','Olivia','Katy','Ray','Tom'])

print(college)
print(len(college))
print(len(coworker))
print(len(family))

# combining all sets in one single set
friends = college.union(coworker,family)

print(friends)
print(len(friends))
print('4 people are missing because they were duplicates')


invite = set (['Amanda','Nestor','Olivia'])
print(invite)
print('Verne' in invite)
invite.add('Verne')
print(invite)
invite.remove('Nestor')
print(invite)

print(invite.pop())
print(invite.pop())
print(invite.pop())