def binary_search(sorted_list, target_value):
    left = 0
    right = len(sorted_list) - 1
    upper_bound = None
    n_iterations = 0

    while left <= right:
        n_iterations += 1
        mid_index = (left + right) // 2

        if sorted_list[mid_index] == target_value:
            return (n_iterations, target_value)
        elif sorted_list[mid_index] < target_value:
            left = mid_index + 1
        else:
            upper_bound = sorted_list[mid_index]
            right = mid_index - 1

    if left < len(sorted_list):
        upper_bound = sorted_list[left]
    return (n_iterations, upper_bound)

print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12], 5))
