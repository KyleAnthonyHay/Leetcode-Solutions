# Optimal Solution
# Time: O(nlogn) sorting
# Space: O(1)

def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    firstRow = 'R' if redShirtHeights[0] < blueShirtHeights[0] else 'B'

    for idx in range(len(redShirtHeights)):

        if firstRow == 'R':
            if redShirtHeights[idx] >= blueShirtHeights[idx]:
                return False
        else:
            if redShirtHeights[idx] <= blueShirtHeights[idx]:
                return False

    return True
