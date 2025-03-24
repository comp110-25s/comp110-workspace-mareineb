from class_lesson_practice.cl21_module import count_regs


def test_count_regs_use() -> None:
    """Tests count_regs function for functionality."""
    assert count_regs("Orange", ["Wake", "Orange", "Orange", "Durham"]) == 2


def test_count_regs_edge() -> None:
    assert count_regs("Orange", []) == 0
