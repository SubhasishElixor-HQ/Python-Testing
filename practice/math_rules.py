def add(left: int, right: int) -> int:
    return left + right


def is_valid_quantity(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and 1 <= value <= 100


def apply_discount(price: int, discount: int) -> int:
    if not isinstance(price, int) or isinstance(price, bool) or price < 0:
        raise ValueError("price must be a non-negative integer")
    if not isinstance(discount, int) or isinstance(discount, bool) or not 0 <= discount <= 100:
        raise ValueError("discount must be an integer between 0 and 100")
    return price * (100 - discount) // 100
