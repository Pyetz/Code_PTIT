def hamming_sequence(upper_bound = 10**18):
    reuslt = (1,)
    nums = [2, 3, 5]
    for i in range(3):
        num = nums[i]
        temp_tpl = ()
        while num <= upper_bound:
            reuslt += (num,)
            temp_tpl += (num,)
            num *= nums[i]
        nums[i] = temp_tpl

    for col1 in range(3):
        for col2 in range(col1+1, 3):
            for i in range(len(nums[col1])):
                for j in range(len(nums[col2])):
                    num = nums[col1][i] * nums[col2][j]
                    if num <= upper_bound:
                        reuslt += (num,)
                    else:
                        break

    for i in range(len(nums[0])):
        for j in range(len(nums[1])):
            for k in range(len(nums[2])):
                num = nums[0][i] * nums[1][j] * nums[2][k]
                if num <= upper_bound:
                    reuslt += (num,)
                else:
                    break
            

    return sorted(reuslt)

def bin_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    tess = int(input())
    test_cases = [int(input()) for _ in range(tess)]
    hamming_seq = hamming_sequence()
    
    for test in test_cases:
        index = bin_search(hamming_seq, test)
        if index == -1:
            print("Not in sequence")
        else:
            print(index+1)
    
main()