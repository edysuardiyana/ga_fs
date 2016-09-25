import features_extract as fe

data = [1,2,3,4,5,6,7,8,9]
x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8,9]
z = [1,2,3,4,5,6,7,8,9]
elem = [1,0,0,0,0,0,0,0,0]

res = fe.features_calc(data,x,y,z,1,elem)
print res
