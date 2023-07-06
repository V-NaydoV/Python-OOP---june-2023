from typing import List


class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self) -> None:
        if not self.is_on:
            self.is_on = True
        else:
            self.is_on = False

    def install(self, app: str, app_memory: int) -> str:
        if self.memory >= app_memory:
            if self.is_on:
                self.apps.append(app)
                self.memory -= app_memory
                return f"Installing {app}"
            return f"Turn on your phone to install {app}"
        return f"Not enough memory to install {app}"

    def status(self) -> str:
        total_apps_count = len(self.apps)
        return f"Total apps: {total_apps_count}. Memory left: {self.memory}"


