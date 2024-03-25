# Python3 program to find element
# closest to given target using binary search.

# Returns element closest to target in arr[]
def findClosest(arr, n, target):
    # Corner cases
    global max, min
    if (target <= arr[0]):
        return arr[0]
    if (target >= arr[n - 1]):
        return arr[n - 1]

    # Doing binary search
    i = 0; j = n;
    mid = 0
    while (i < j):
        mid = (i + j) // 2

        if (arr[mid] == target):
            return arr[mid]

        # If target is less than array
        # element, then search in left
        if (target < arr[mid]):

            # If target is greater than previous
            # to mid, return closest of two
            if (mid > 0 and target > arr[mid - 1]):
                return getClosest(arr[mid - 1], arr[mid], target)

            # Repeat for left half
            j = mid

        # If target is greater than mid
        else:
            if (mid < n - 1 and target < arr[mid + 1]):
                return getClosest(arr[mid], arr[mid + 1], target)

            # update i
            i = mid + 1

    # Only single element left after search
    if arr[mid] > target:
        max = arr[mid]
        min = arr[mid-1]
    if arr[mid] < target:
        min = arr[mid]
        max = arr[mid+1]
    return [min, max]


# Method to compare which one is the more close.
# We find the closest by taking the difference
# between the target and both values. It assumes
# that val2 is greater than val1 and target lies
# between these two.
def getClosest(val1, val2, target):
    if (target - val1 >= val2 - target):
        return val2
    else:
        return val1


# Driver code
arr = [-503.462, -496.884, -490.214, -483.654, -483.528, -476.75, -469.814, -462.658, -455.286, -447.672, -439.806, -431.698, -423.32, -414.702, -405.848, -396.76, -387.464, -377.966, -368.284, -358.436, -348.428, -338.276, -327.99199999999996, -317.582, -307.06399999999996, -296.446, -285.726, -274.914, -264.028, -253.066, -242.028, -230.932, -208.548, -185.94599999999997, -163.15999999999997, -140.20600000000002, -117.094, -93.84800000000001, -70.48399999999998, -47.00400000000002, -23.413999999999987, 0.2599999999999909, 24.024, 47.88199999999995, 71.822, 95.83799999999997, 119.93799999999999]
n = len(arr)
target = 0.0
print(findClosest(arr, n, target))

# This code is contributed by Smitha Dinesh Semwal