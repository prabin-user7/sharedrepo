#sets //unordered data type

from re import S


s={1,2,3}
print(s)

l=[1,2,3,4,5,5,5,6,7,7,8]
s2=set(l)
print(s2)

s3=list(set(l))
print(s3)

s.add(4)
print(s)

s.remove(3)
print(s)

print(s.clear())

s1=s.copy()
print(s1)

s1={1,2,3,4}
s2={3,4,5,6}

#s1Us2=[1,2,3,4,5,6]
#s1As2=[3,4]

union_set=s1|s2
print(union_set)

int_set=s1&s2
print(int_set)