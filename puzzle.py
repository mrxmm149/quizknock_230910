import itertools
nums = [5,6,7,9]
target = 19

def run_nums(curr, target, left):
    if len(left) == 0:
        return curr == target

    left.append(curr)
    next = left[0]
    curr = left[1]
    left.pop(0)
    left.pop(0)

    if run_nums(curr + next, target, list(left)):
        print(f"{curr} + {next}")
        return True

    if run_nums(next * curr, target, list(left)):
        print(f"{curr} * {next}")
        return True

    smaller, larger = sorted([curr, next])

    if run_nums(larger - smaller, target, list(left)):
        print(f"{larger} - {smaller}")
        return True

    if smaller == 0:
        return False

    if larger % smaller == 0 and run_nums(int(larger / smaller), target, list(left)):
        print(f"{larger} / {smaller}")
        return True

    return False

def run_nums_2(curr, target, left):
    if len(left) == 0:
        return curr == target

    next = left[0]
    left.pop(0)

    if run_nums_2(curr + next, target, list(left)):
        print(f"{curr} + {next}")
        return True

    if run_nums_2(next * curr, target, list(left)):
        print(f"{curr} * {next}")
        return True

    smaller, larger = sorted([curr, next])

    if run_nums_2(larger - smaller, target, list(left)):
        print(f"{larger} - {smaller}")
        return True

    if smaller == 0:
        return False

    if larger % smaller == 0 and run_nums_2(int(larger / smaller), target, list(left)):
        print(f"{larger} / {smaller}")
        return True

    return False

for perm in itertools.permutations(nums):
    left = list(perm)
    start = left[0]
    left.pop(0)
    if run_nums_2(start, target, list(left)) or run_nums(start, target, list(left)):
        print("Found!")
        break
