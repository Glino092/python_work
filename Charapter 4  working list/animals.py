# animals = ['dog', 'cat', 'hamster', 'toad', 'lizard']
# for animal in animals:
#     print(f"A {animal.title()} would make a great pet")
    
# print("Any of these animals are so cute!!!!")

def find_max(nums):
    max_num = float("-inf")
    for num in nums:
        if num > max_num:
            max_num += 1
        return max_num
