def max_sub_array_sum(a, size):
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        # Do not compare for all elements. Compare only
        # when max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far

size = int(input("Enter size of an array\n"))
print("Enter the {0} array values".format(size))

ar = []
for i in range(0, size):
    ar.append(int(input()))

result = max_sub_array_sum(ar, size)
print("\nResult is {0}".format(result))
