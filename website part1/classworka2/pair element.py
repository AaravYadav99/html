class pair_elements:
    def too_sum(self,nums,target):
        sum=0
        lookup={ }
        for i ,num in enumerate(nums):
            sum=sum+num
            lookup[i]=num
            if sum>target:
                return i-1,lookup[i-1]
value=int(input("enter the sum which you want to make"))
print("the element is ",pair_elements().too_sum((10,20,30,40,50,60,70),value))