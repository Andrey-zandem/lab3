class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    v1 = Vector(2, 3)
    v2 = Vector(5, 7)
    v3 = v1 + v2
    print(f"Вектор 1: [{v1.x}, {v1.y}]")
    print(f"Вектор 2: [{v2.x}, {v2.y}]")
    print(f"Суммарный вектор: [{v3.x}, {v3.y}]")
