#Given an array, rotate the array to the right by k steps, where k is non-negative.
def rotate_array(input_array, k):
  count = k % len(input_array)
  placeholder = len(input_array)-k
  for i in range (0,count):
    input_array.insert(0,input_array[-1])
    input_array.pop()

  pass

#list = [6,1,2,3,4,5]
#rotate_array(list,1)

#for x in range (0,len(list)):
#      print(list[x])
