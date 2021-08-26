thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  1964 : "ferrari",
}

'''
for item in thisdict:
    print(item, end='\t')
    print(thisdict[item])
'''

item = 1964
if 1964 in thisdict:
    print(thisdict[item])


my_dict = {k:k**k for k in range(10)}

for item in my_dict:
    print(item, end='\t')
    print(my_dict[item])