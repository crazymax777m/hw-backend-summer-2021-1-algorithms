from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    string = text.strip().split()
    if string:
        shortest = min(string, key=len)
        longest = max(string, key=len)
    else:
        return None, None
    return shortest, longest
