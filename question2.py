paragraph=input('enter the paragraph')
words=paragraph.split()
list1=[]
for i in words:
    if len(i)> 4:
        list1.append(i)
print(list1)