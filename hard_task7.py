class Row:
    def __init__(self, **fields) -> None:
        self.__dict__.update(fields)

    def __repr__(self) -> str:
        fields = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"Row({fields})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Row) and self.__dict__ == other.__dict__


class Table:
    def __init__(self, name: str, columns: list[str]) -> None:
        self.name = name
        self.columns = columns
        self._rows: list[Row] = []

    def insert(self, **values) -> Row:
        self._check_columns(values)
        row = Row(**values)
        self._rows.append(row)
        return row

    def select(self, predicate=None, **conditions) -> list[Row]:
        if predicate is not None:
            return [row for row in self._rows if predicate(row)]
        return [
            row for row in self._rows
            if all(getattr(row, k) == v for k, v in conditions.items())
        ]

    def all(self) -> list[Row]:
        return list(self._rows)

    def _check_columns(self, values: dict) -> None:
        unknown = set(values) - set(self.columns)
        if unknown:
            raise ValueError(f"Неизвестные колонки: {unknown}")

    def __len__(self) -> int:
        return len(self._rows)

    def __str__(self) -> str:
        return f"Table({self.name}, rows={len(self._rows)})"


if __name__ == "__main__":
    users = Table("users", ["id", "name", "age"])
    users.insert(id=1, name="Иван", age=20)
    users.insert(id=2, name="Мария", age=22)
    users.insert(id=3, name="Пётр", age=19)

    print(users)
    print(users.select(name="Иван"))
    print(users.select(age=22))
    print(users.select(lambda r: r.age > 20))
    print(users.all())
    print(len(users))
