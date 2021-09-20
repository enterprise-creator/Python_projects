# Python3 program to find
# minimum number of swaps
# required to sort an array

# Function returns the minimum
# number of swaps required to
# sort the array
def minSwaps(arr):
  swaps = 0
  
  for i in range(len(arr)):
    while place(arr,i)!=0: 
      swaps+=1
      place(arr,i)
      
  return swaps
      
def place(array , idx):
  count = 0
  for j in range(idx+1,len(array)):
    if array[j]<array[idx]: count+=1
    
  if count!=0:
    array[idx+count] , array[idx] = array[idx] , array[idx+count]
    
  return count


arr = [1, 5, 4, 3, 2]
print(minSwaps(arr))

