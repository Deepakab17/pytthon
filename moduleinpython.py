# l = [64, 34, 25, 12, 22, 11, 90, 5]
# n = len(l)
# for i in range(n-1):
# for j in range(n-i-1):
# if l[j] > l[j+1]:
# l[j], l[j+1] = l[j+1], l[j]
# print(l)
# l = [64, 34, 25, 12, 22, 11, 90, 5]
# n = len(l)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if l[j] < l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j]
# print(l)
# l = [2,4,9,3,5]
# max = l[0]
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         max = l[i]
#         l[i],l[i+1]=l[i+1],l[i]
#     else:
#         max=l[i+1]
# print(max)
# l = [2,4,9,3,5]
# min = l[0]
# for i in range(len(l)-1):
#     if l[i]<l[i+1]:
#         min = l[i]
#         l[i],l[i+1]=l[i+1],l[i]
# else:
#     min=l[i+1]
# print(min)