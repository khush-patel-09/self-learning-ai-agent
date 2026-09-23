import math
#cosine similarity

def cosine_similarity(
    first: list[float],
    second: list[float],
) -> float:
    """Calculate cosine similarity between two vectors."""
    if len(first) != len(second):
        raise ValueError("Vectors must have the same dimension.")

    first_norm = math.sqrt(sum(value * value for value in first))
    second_norm = math.sqrt(sum(value * value for value in second))

    if first_norm == 0 or second_norm == 0:
        return 0.0

    dot_product = sum(
        first_value * second_value
        for first_value, second_value in zip(first, second)
    )

    return dot_product / (first_norm * second_norm)