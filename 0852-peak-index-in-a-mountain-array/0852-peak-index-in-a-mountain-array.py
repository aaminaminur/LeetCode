class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        size = len(arr)
        low = 0
        high = size-1
        if arr[0] > arr[1]:
            return 0
        if arr[-1] > arr[-2]:
            return size - 1
        while low < high:
            mid = low + (high - low)//2
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] < arr[mid] :
                low = mid + 1
            else:
                high = mid
                