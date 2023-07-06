class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml: int) -> str:
        if ml + self.content <= Glass.capacity:
            self.content += ml
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self) -> str:
        self.content = 0
        return "Glass is now empty"

    def info(self) -> str:
        space_left = Glass.capacity - self.content
        return f"{space_left} ml left"
