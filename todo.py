import os
clear = lambda: os.system('clear')

class Database:
    todos: list[dict]

    def __init__(self):
        self.todos: list[dict] = []

    def add(self, item: str) -> None:
        self.todos.append({"value": item, "checked": False})

    def pop(self, index: int) -> None:
        if index in range(len(self.todos)):
            self.todos.pop(index)

    def check(self, index: int) -> None:
        if index in range(len(self.todos)):
            self.todos[index]["checked"] = True

    def uncheck(self, index: int) -> None:
        if index in range(len(self.todos)):
            self.todos[index]["checked"] = False

    def toggleCheck(self, index: int) -> None:
        if index in range(len(self.todos)):
            self.todos[index]["checked"] = not self.todos[index]["checked"]

    def isChecked(self, index: int) -> bool:
        if index in range(len(self.todos)):
            return self.todos[index]["checked"]
        else:
            return False

if __name__ == "__main__":
    db = Database()
    while True:
        clear()
        for i in range(len(db.todos)):
            print(f"{i} - [{"X" if db.todos[i]['checked'] else ""}] {db.todos[i]['value']}")

        cmd = input()
        function = cmd.split(" ")[0]
        attr = " ".join(cmd.split(" ")[1:])

        if function == "add":
            db.add(attr)
        if function == "delete":
            db.pop(int(attr))
        if function == "check":
            db.check(int(attr))
        if function == "uncheck":
            db.uncheck(int(attr))
        if function == "quit":
            break
        if function == "help" or function == "h":
            input("Commands are add TODO, delete KEY, check KEY, uncheck KEY or quit (Enter to reset)")
