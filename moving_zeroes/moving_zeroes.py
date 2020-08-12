'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    nums = []
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            nums.append(arr.pop(i))
        else:
            i += 1
    
    arr.extend(nums)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")