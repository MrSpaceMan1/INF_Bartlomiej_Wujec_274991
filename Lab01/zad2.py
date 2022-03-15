import random


def scalar(vec1: list[int | float], vec2: list[int | float]) -> int | float:
    if len(vec1) != len(vec1):
        raise TypeError("Vectors have different sizes")
    _sum = 0
    for i in range(0, len(vec1)):
        _sum += vec1[i] * vec2[i]
    return _sum


def euclidian_distance(vec: list[int | float]) -> float:
    _sum = 0
    for i in vec:
        _sum += i**2
    return _sum**(1/2)


def mean(vec: list[int | float]) -> float:
    return sum(vec)/len(vec)


def sd(vec: list[int | float]) -> float:
    m = mean(vec)
    _sum = 0
    for i in vec:
        _sum = (i - m)**2
    return (_sum/len(vec))**(1/2)


def normalise(vec: list[int | float]) -> list[int | float]:
    new_vec = []
    _min = min(vec)
    _max = max(vec)
    for i in vec:
        new_vec.append((i - _min) / (_max - _min))
    return new_vec


def standardise(vec: list[int | float]) -> list[int | float]:
    m = mean(vec)
    _sd = sd(vec)
    new_vec = []
    for i in vec:
        new_vec.append((i - m) / _sd)
    return new_vec


def makeDiscrete(vec: list[int | float]) -> list:
    new_vec = []
    for i in vec:
        print(i / 10)
        # new_vec.append(f"[{}")


v1 = [3, 8, 9, 10, 12]
v2 = [8, 7, 7, 5, 6]

print(scalar(v1, v2))
print("-")
print(euclidian_distance(v1))
print(euclidian_distance(v2))
print("-")
vec = [random.randint(1, 100) for i in range(0, 50)]
print(mean(vec))
print(min(vec))
print(max(vec))
print(sd(vec))
print()
print(normalise(vec))
print()
print(standardise(vec))
print()
print(mean(standardise(vec)))
print(sd(standardise(vec)))
print()
makeDiscrete(vec)
