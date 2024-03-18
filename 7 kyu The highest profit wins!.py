lst = [2334454, 5] # [5,2334454]

def min_max(lst):
  min_max_lst = []
  min_max_lst.append(min(lst))
  min_max_lst.append(max(lst))
  return min_max_lst

print(min_max(lst))