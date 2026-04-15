class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        sub_nums1 = nums1[:m]
        sub_nums2 = nums2[:n]
        self.nums1 = []

        pointer1 = 0
        pointer2 = 0

        while pointer1 < len(sub_nums1) and pointer2 < len(sub_nums2):
            if sub_nums1[pointer1] < sub_nums2[pointer2]:
                self.nums1.append(sub_nums1[pointer1])
                pointer1 +- 1
            else:
                self.nums1.append(sub_nums2[pointer2])
                pointer2 += 1

        self.nums1.extend(sub_nums1[pointer1:])
        self.nums1.extend(sub_nums2[ pointer2:])

        nums1 = self.nums1