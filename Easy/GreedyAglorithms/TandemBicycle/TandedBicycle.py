# Optimal Solution
# Time: O(nlogn) sorting
# Space: O(1)

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    totalSpeed = 0

    if fastest == True:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort(reverse=True)
        for idx in range(len(redShirtSpeeds)):
            totalSpeed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])

    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
        for idx in range(len(redShirtSpeeds)):
            totalSpeed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])

    return totalSpeed
