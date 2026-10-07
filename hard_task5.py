import json


class JsonSerializer:
    """Сериализует объекты Python в JSON и обратно."""

    def dumps(self, obj) -> str:
        if not hasattr(obj, "__dict__"):
            raise TypeError(f"Объект {type(obj).__name__} не поддерживается")
        return json.dumps(obj.__dict__, ensure_ascii=False, indent=2)

    def dump(self, obj, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.dumps(obj))

    def loads(self, text: str, cls):
        data = json.loads(text)
        return cls(**data)

    def load(self, path: str, cls):
        with open(path, encoding="utf-8") as f:
            return self.loads(f.read(), cls)


class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, age={self.age})"


if __name__ == "__main__":
    ser = JsonSerializer()

    s1 = Student("Иван", 20)

    # строка
    text = ser.dumps(s1)
    print("JSON-строка:")
    print(text)

    # файл
    ser.dump(s1, "student.json")

    # обратно
    s2 = ser.load("student.json", Student)
    print("Восстановлено:", s2)
    print("Совпадает:", s1.__dict__ == s2.__dict__)