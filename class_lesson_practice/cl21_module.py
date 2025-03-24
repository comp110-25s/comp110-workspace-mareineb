def count_regs(coi: str, counties: list[str]) -> int:
    idx: int = 0
    total: int = 0
    while idx < len(counties):
        if counties[idx] == coi:
            total += 1
        idx += 1
    return total
