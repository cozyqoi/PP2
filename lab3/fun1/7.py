def has_33(nums):
    return any(nums[i] == 3 and nums[i+1] == 3 for i in range(len(nums)-1))

nums = list(map(int, input("san engiz: ").split()))
print("eki 3 katarma?", has_33(nums))