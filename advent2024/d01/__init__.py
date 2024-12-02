def part_1(lines: list[str]) -> int:

    # Define function to compare/return diference of two values
    def cmp(values: tuple[int, int]) -> int:
        lf, rt = values
        return lf - rt if lf > rt else rt - lf

    # Parse each line, separating left elements from the ones on the right
    lfs: list[int] = []
    rts: list[int] = []
    for ln in lines:
        curr = [_ for _ in ln.strip().split() if _]
        if 2 != len(curr):
            continue
        lfs.append(int(curr[0]))
        rts.append(int(curr[1]))

    # Sort each side so we pair them correctly
    lfs, rts = sorted(lfs), sorted(rts)
    res = sum(map(cmp, zip(lfs, rts)))

    return res

def part_2(lines: list[str]):

    from collections import Counter

    # Parse each line, separating left elements from the ones on the right
    lfs: list[int] = []
    rts: list[int] = []
    for ln in lines:
        curr = [_ for _ in ln.strip().split() if _]
        if 2 != len(curr):
            continue
        lfs.append(int(curr[0]))
        rts.append(int(curr[1]))

    # Define counter and function to compute similarity score
    count = Counter(rts)
    def score(value: int) -> int:
        return value * count[value]

    res = sum(map(score, lfs))

    return res
