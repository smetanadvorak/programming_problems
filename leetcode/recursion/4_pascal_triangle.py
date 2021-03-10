# Given an integer rowIndex, return the rowIndexth (0-indexed) row
# of the Pascal's triangle.


# In Pascal's triangle, each number is the sum of the two
# numbers directly above it.

# Example 1:
#
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
#
# Input: rowIndex = 0
# Output: [1]
# Example 3:
#
# Input: rowIndex = 1
# Output: [1,1]

# Constraints:
#
# 0 <= rowIndex <= 33
#
# Follow up: Could you optimize your algorithm to use only O(rowIndex)
# extra space?

def getElement(columnIndex, rowIndex, memoization):
    # Check if outside the triangle
    if columnIndex < 0 or columnIndex > rowIndex:
        return 0

    # Check if in base case
    if columnIndex == 0 and rowIndex == 0:
        return 1

    if not memoization[rowIndex][columnIndex]:
        memoization[rowIndex][columnIndex] = getElement(columnIndex-1, rowIndex-1, memoization) + getElement(columnIndex, rowIndex-1, memoization)
    return memoization[rowIndex][columnIndex]


def getRow(rowIndex):
    memoization = [[0 for j in range(i+1)] for i in range(rowIndex+1)]
    return [getElement(i, rowIndex, memoization) for i in range(rowIndex+1)]


for row in range(15):
    print('Row %d' % row, getRow(row))
