arr = [2, 3, 2, 2, 2] # 3

def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i

print(stray(arr))