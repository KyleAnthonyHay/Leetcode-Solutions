# Optimal Solution

# Time 0(n) | Space 0(1)
def bestSeat(seats):
    longest_empty_space = 0
    best_seat_idx = -1
    empty_space = 0
    for i in range(len(seats)):
        if not seats[i]:
            # Found empty seat, add to current count and continue
            empty_space += 1
        else:
            # Found a taken seat, determine if seen space
            # is better than anything previously found
            if empty_space > longest_empty_space:
                longest_empty_space = empty_space
                best_seat_idx = i - 1 - empty_space // 2
            empty_space = 0
    return best_seat_idx
# Credit: Carlos on January 5, 2024


