std1 ={'id1':
{'name':["Aarav"],
 'age':[15]},
 'id2':
{'name':["Naman"],
 'age':[15]},
 'id3':
{'name':["Aarav"],
 'age':[15]}}
result={}
for key,value in std1.items():
    if value not in result.values():
        result[key]=value
print(result)
