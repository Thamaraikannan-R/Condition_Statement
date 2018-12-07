low=int(input("Enter the low number:"))
high=int(input("Enter the highest number:"))
while(low<=high):
    print(low)
    if(low%3==0):
        print("div3")
    low=low+1