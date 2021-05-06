#!/usr/bin/python3
def roman_to_int(roman_string):

    total = 0
    roman_numerals = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    if not (isinstance(roman_string, str)) or not roman_string:
        return 0

    nums = [roman_numerals[ite] for ite in roman_string]
    for ite in range(len(nums) - 1):
        if nums[ite] >= nums[ite + 1]:
            total += nums[ite]
        else:
            nums[ite + 1] = nums[ite + 1] - nums[ite]
    total += nums[len(nums) - 1]
    return total
