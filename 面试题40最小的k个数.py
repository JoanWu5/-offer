import heapq
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # arr.sort()
        # return arr[:k]
        if k == 0:
            return []
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k,len(arr)):
            if -hp[0]>arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp,-arr[i])
        result = [-x for x in hp]
        return result