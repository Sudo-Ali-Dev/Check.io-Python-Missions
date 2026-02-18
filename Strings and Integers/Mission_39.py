# https://py.checkio.org/en/mission/quadratic-equation-roots/

from collections.abc import Iterable
from typing import Union

def quadratic_roots(a: int, b: int, c: int) -> Iterable[Union[int | float] | str]:
    
    result = []
    disc = pow(b, 2) - (4 * a * c)

    if disc < 0:
        result.append("No real roots")
        return result
        
    deno = 2 * a
    nume_disc = disc ** 0.5

    x_1 = ((-b) + (nume_disc)) / deno
    x_2 = ((-b) - (nume_disc)) / deno

    result.append(x_1)
    result.append(x_2)

    return result


print("Example:")
print(list(quadratic_roots(1, 0, 1)))

# These "asserts" are used for self-checking
assert list(quadratic_roots(1, -3, 2)) == [2, 1]
assert list(quadratic_roots(1, 0, -1)) == [1, -1]
assert list(quadratic_roots(1, 2, 1)) == [-1, -1]
assert list(quadratic_roots(1, 0, 1)) == ["No real roots"]
assert list(quadratic_roots(1, 4, 4)) == [-2, -2]
assert list(quadratic_roots(1, -5, 6)) == [3, 2]
assert list(quadratic_roots(1, -6, 9)) == [3, 3]
assert list(quadratic_roots(2, 2, 1)) == ["No real roots"]
assert list(quadratic_roots(2, -7, 6)) == [2, 1.5]
assert list(quadratic_roots(2, -3, 1)) == [1, 0.5]

print("The mission is done! Click 'Check Solution' to earn rewards!")
