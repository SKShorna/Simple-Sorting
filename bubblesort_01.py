def bubbleSort(list):
    for i in range(0, len(list)-1): ##for passing the whole list
        for j in range(0, len(list)-1-i):##for inner checking iteration of each pass
            if list[j]> list[j+1]:
                list[j], list[j+1]= list[j+1], list[j]
    return list
arr=[]
elem = int(input("How Many Numbers:"))
print("Enter The NUmbers:")
for i in range(0, elem):
    arr.append(int(input()))
print("The Array Element After input:")
print(bubbleSort(arr))