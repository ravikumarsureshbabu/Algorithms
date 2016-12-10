

def findMedianSortedArrays(nums1, nums2):
        n1_index =0
        n2_index = 0
        index = 0
        pos = (len(nums1) + len(nums2) ) / 2
        evencase = 0
        if (len(nums1) + len(nums2) ) % 2 == 0:
            evencase = 1
        median1 = 0
        median2 = 0
        while index <= pos :
            if nums1[n1_index] < nums2[n2_index]:
                median1 = median2
                median2 = nums1[n1_index]
                n1_index += 1
            else:
                median1 = median2
                median2 = nums2[n2_index]
                n2_index += 1
            index += 1
        if evencase:
            return float((median1+median2)/2)
        else:
            return median2

a = [1,3]
b = [2,4]
print(findMedianSortedArrays(a, b))
