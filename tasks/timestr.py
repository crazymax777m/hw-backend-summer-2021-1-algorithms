__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    if m == h == d == 0:
        return f'{s:02d}s'
    elif h == d == 0:
        return f'{m:02d}m{s:02d}s'
    elif d == 0:
        return f'{h:02d}h{m:02d}m{s:02d}s'
    return f'{d:02d}d{h:02d}h{m:02d}m{s:02d}s'




