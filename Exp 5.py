print("Name : Aiswarya Sunil ")
print("Admission No: A24MCA004")
print("Ascending & Descending Experiemnt : 5")
fruits={'Mango': 3, 'Grapes' :2, 'Apple':4, 'Banana':1}

ascending=dict (sorted(fruits.items()))
descending=dict (sorted(fruits.items(), reverse=True))
print("Ascending Order : ", ascending)
print("Descending Order : ",descending)
merge={**ascending, **descending}

print("Merged dictionary ", merge)

