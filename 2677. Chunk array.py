# class Solution:
#     def chunkArray(arr,size):
#         if size == 1:
#             return [[i] for i in arr]
#         chunkedArr = []
#         l = len(arr)
#         if l < size:
#             chunkedArr.append([j for j in arr])
#             return chunkedArr
#         for i in range(size, l, size):
#             chunk = []
#             if i == size:
#                 left = 0
#             for j in range(left, i):
#                 chunk.append(arr[j])
#             chunkedArr.append(chunk)
#             left = i
#             if (l-i) < size:
#                 x = [k for k in range(i,len(arr))]
#                 chunkedArr.append(x)
#         return chunkedArr

class Solution:
    def chunkArray(arr, size):
        if size == 1:
            return [[i] for i in arr]

        chunkedArr = []
        l = len(arr)
        left = 0

        for i in range(size, l + size, size):
            chunk = arr[left:i]
            chunkedArr.append(chunk)
            left = i

        return chunkedArr

if __name__ == "__main__":
    arr = [1, 9, 6, 3, 2]
    slice_size = 6
    result = Solution.chunkArray(arr, slice_size)
    print(result)