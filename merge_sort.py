def merge_sort(arr):
  if len(arr) > 1:
    mid = len(arr)//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
  else:
    return arr
  return merge(right_arr, left_arr)

def merge(left, right):
  result = []
  i = j = 0
  
  # Compare elements from both lists and append the smaller one
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
      
  # Append remaining elements from both lists
  result.extend(left[i:])
  result.extend(right[j:])
  return result
