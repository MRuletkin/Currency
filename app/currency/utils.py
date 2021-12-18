from decimal import Decimal


def to_decimal(num: str) -> Decimal:
    return Decimal(num).quantize(Decimal(10) ** -2)
