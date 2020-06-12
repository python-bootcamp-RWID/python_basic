mydict = {
    'name':'Danil',
    'last_name':'Syah Arihardjo',
    'phone':628363008663
}

print(mydict)

mydict['email'] = 'danilsyah@gmail.com'
print(mydict)

# mydict.pop('name')
# print(mydict)

# mydict.clear()
# print(mydict)

newdict = mydict.copy()
print(newdict)
newdict['address'] = 'Tanjung Uban'
print(newdict)
print(mydict)

for i, biodata in mydict.items():
    print(i, ":",biodata)