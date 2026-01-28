import math

def fix_missing_elements():
    # Setup
    n_input = int(input("How many elements are you entering? "))
    arr = []
    for i in range(n_input):
        a = int(input(f"Enter element {i+1}: "))
        arr.append(a)

    # 1. Identify the range
    low, high = min(arr), max(arr)
    # The total numbers that SHOULD be there (including 2 missing)
    # is high - low + 1. 
    
    # 2. Find the sum of missing numbers (x + y)
    expected_sum = sum(range(low, high + 1))
    actual_sum = sum(arr)
    sum_missing = expected_sum - actual_sum
    
    # 3. Find the average to split the search
    # One missing number is below avg, one is above avg.
    avg_missing = sum_missing // 2
    
    # 4. Find the first missing number (x) 
    # by looking at the range [low ... avg_missing]
    expected_sum_left = sum(range(low, avg_missing + 1))
    actual_sum_left = sum(num for num in arr if num <= avg_missing)
    
    first_missing = expected_sum_left - actual_sum_left
    second_missing = sum_missing - first_missing
    
    # 5. Append and maintain uniqueness
    if first_missing != second_missing and first_missing not in arr:
        arr.append(first_missing)
        arr.append(second_missing)
        arr.sort() # Optional: keep it tidy
        print(f"Added {first_missing} and {second_missing}")
    else:
        print("Logic Error: Numbers might not be missing in this range.")
        
    print("Final Array:", arr)

fix_missing_elements()
