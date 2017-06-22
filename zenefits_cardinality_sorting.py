# Complete the function below.

def cardinalitySort(nums):
    def get_binary_cardinality(num):
        """Gets binary cardinality of a number"""
        bin_rep = bin(num)[2:]
        return bin_rep.count('1')

    sorted_nums = []
    binary_nums = {}
    for num in nums:
        num_ones = get_binary_cardinality(num)
        if num_ones in binary_nums.keys():
            binary_nums[num_ones].append(num)
        else:
            binary_nums[num_ones] = [num]

    binary_keys = sorted(binary_nums.keys())
    for key in binary_keys:
        for num in sorted(binary_nums[key]):
            sorted_nums.append(num)
    return sorted_nums
