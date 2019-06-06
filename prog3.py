def search(a,beg,end,ele):
	while beg<=end:
		mid=(beg+end)//2
		if a[mid]==ele:
			return mid
		elif a[mid]<ele:
			beg=mid+1
		elif a[mid]>ele:
			end=mid-1
    return -1

	
n=int(input("Enter no. of elements"))
a=[]
for i in range(n):
	e=int(input("Enter no."))
	a.append(e)

ele=int(input("Enter element to be searched"))

res=search(a,0,n,ele)

if(res==-1):
	print("Element not found")
else:
	print("Element found at", res)