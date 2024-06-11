list1=[0,1,2,3,4,6,5,7,8]
print(list1[2:5])



list2=[0,1,2,4,5,6,7,8,9,10,11]
print(list2[0:4])

print(list1[:4])

print(list1[3:])

#to find the length of the list
print(len(list1))

#change value of current list item
list1[0]='apple'
print(list1)

#using for loop
mylist=['onion','tomato','carrot','orange']
print('list of elements:',mylist)
for x in mylist:
    print(x)

#append()
mylist=['onion','tomato','carrot','orangr','apple']
mylist.append('cabbage')
print(mylist)

#insert
mylist=['onion','tomato','carrot','orangr','apple']
mylist.insert(0,'cabbage')
print(mylist)

#remove
mylist1=['onion','tomato','carrot']
mylist1.remove('tomato')
print(mylist1)

#clear list
thislist=['onion','tomato','carrot']
thislist.clear()
print(thislist)

#extend()
fruits=['bannana','apple','cherry','orange']
vegetables=['carrot','onion','tomatio']
fruits.extend(vegetables)
print(fruits)

























