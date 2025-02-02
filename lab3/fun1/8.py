def spy_game(nums):
    code = [0, 0, 7]
    index = 0
    for num in nums:
        if num == code[index]:
            index += 1
        if index == 3:
            return True
    return False

nums = list(map(int, input("san engiz: ").split()))
print("007 barma?", spy_game(nums))