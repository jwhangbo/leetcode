# 981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:
    # as the constraint that all timestamps of set will be strictly increasing, binary search can be used to optimize the time complexity

    def __init__(self):
        # create a hash map to track the key and its respective list of values and timestamps
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # check if the key is not in the store - if true, intialize the key with an empty list
        if key not in self.store:
            self.store[key] = []
        
        # push the list containing the value and timestamp to the stored key
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # initialize the result as an empty string
        res = ""

        # get the values from the store based on the key, with the default set to an empty list
        values = self.store.get(key, [])

        # itialize two pointers for the leftmost and rightmost timestamps in the list of values
        l, r = 0, len(values) - 1

        # loop until the left pointer becomes greater than the right pointer
        while l <= r:

            # set the middle pointer to the sum of the left and right pointers, then divided by 2
            m = (l + r) // 2

            # check if the middle pointer's timestamp is less than or equal to the given timestamp
            if values[m][1] <= timestamp:

                # as this is a valid result, overwrite the existing result with the new value
                res = values[m][0]

                # recalculate the left pointer to middle + 1
                l = m + 1

            else:

                # recalculate the right pointer to middle - 1
                # note that the result for this case will not be saved
                # this is because the problem looks for values with timestamps equal, if not less than the given timestamp
                # as this case would have a greater timestamp, the result should not be affected
                r = m - 1
        
        # if code reaches this point, the target value with the correct timestamp under given circumstances will have been found
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)