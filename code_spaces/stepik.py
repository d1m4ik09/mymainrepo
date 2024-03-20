def quick_merge(list1, list2):
    res = []
    p1 = 0
    p2 = 0

    list1 = list(str(list1).split())
    list2 = list(str(list2).split())

    while p1 < len(list1) and p2 < len(list2):
        if int(list1[p1]) < int(list2[p2]):
            res.append(list1[p1])
            p1 += 1
        else:
            res.append(list2[p2])
            p2 += 1

    if p1 == len(list1):
        res.append(list2[p2:])
    else:
        res.append(list1[p1:])
    return res

a = int(input())
nums = []

for _ in range(a):
    nums.append(input())

while len(nums) > 2:
    nums = list(quick_merge(nums[0], nums[1])) + nums[2:]

hui = quick_merge(nums[0], nums[1])
print(* hui)