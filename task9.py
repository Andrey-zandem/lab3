class FileReader:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def get_text(self) -> str:
        with open(self.filename, encoding="utf-8") as file:
            return file.read()


if __name__ == "__main__":
    task = FileReader("task9.txt")
    print(task.get_text())
