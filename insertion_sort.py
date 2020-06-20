
# Insertion sort is a simple sorting algorithm that builds
# the final sorted array (or list) one item at a time.
# 	(https://en.wikipedia.org/wiki/Insertion_sort)

def insert_sort(myArray):
    array = myArray.copy()

    # Loop through every element of the array.
    for i in range(0, len(array)):
        # If we're dealing with the first element of the array,
        # continue the loop as the element cannot be compared to anything.
        if i == 0:
            continue

        # The index at which the selected element will need to be appended to
        # at the end of this for loop.
        newIndex = i

        # Loop through every element from the beginning of the array
        # to the current element starting from the last element.

        # In this situation, we set the starting value to i - 1
        # to avoid the element to compare to itself, thus resulting
        # in an unsorted array.
        for j in range(i - 1, 0 - 1, -1):
            # The selected element is lower than the element preceding it,
            # thus needing a new index.
            if array[i] < array[j]:
                newIndex = j
            else:
                # The selected element has reached its final position.
                break
        # Remove the element from its current index and insert it at its new index.
        element = array[i]
        array.pop(i)
        array.insert(newIndex, element)
    # Finished sorting!
    return array
