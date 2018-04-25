#Demonstrate python program to create all possible permutations from a given collection of distinct numbers


def permute(nums):
  if nums == []:
    return [[]]
  permutations=[]
  for i,n in enumerate(nums):
    other_permutations=permute(nums[:i] + nums[i+1:])
    permutations+=map(lambda permutation: [n] + permutation,other_permutations)
  return permutations
print(permute([1,2,3]))




#this can also be done by importing itertools
import itertools

lst = [1,2,3]
print(set(itertools.permutations(lst)))


