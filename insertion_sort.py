def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]  # Current element to be inserted
    j = i - 1
    # Shift elements of arr[0..i-1] that are greater than key
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1  
    # Insert the key at the correct position
    arr[j+1] = key
  return arr
