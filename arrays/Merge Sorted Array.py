def merge_stored_arrays(arr1, arr2):
    merged = []
    i = 0
    j = 0

    # Merge while both arrays have elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])  
            j += 1

    # Add remaining elements in arr1 (if any)
    while i < len(arr1):
        merged.append(arr1[i])   # Use [i], not (i)
        i += 1

    # Add remaining elements in arr2 (if any)
    while j < len(arr2):        # Was: while i < len(arr2[i]) ❌
        merged.append(arr2[j])  # Use [j], not (j)
        j += 1

    return merged

print(merge_stored_arrays([1, 3, 5], [2, 4, 6]))
