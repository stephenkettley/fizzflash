def compute_accuracy(correct: int, seen: int) -> float:
    return correct / seen if seen > 0 else 0.0
