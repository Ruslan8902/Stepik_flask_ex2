import random
from threading import Lock
import copy


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Game(metaclass=SingletonMeta):
    def __init__(self, username="Unknown_player", x=0, y=0, x1=1, y1=0):
        self.username = username
        self.x = x
        self.y = y
        self.map = [
            [None, "Балкон", None],
            ["Спальня", "Холл", "Кухня"],
            ["Подземелье", "Коридор", "Оружейная"]
        ]
        self.attempt = 0
        self.desired_x = x1
        self.desired_y = y1

    def move(self, direction, step_q):
        movement = {
            0: [self.x, self.y - step_q],
            1: [self.x + step_q, self.y],
            2: [self.x, self.y + step_q],
            3: [self.x - step_q, self.y]
        }
        message = None
        new_pos = movement[direction]
        col_s = len(self.map[0])
        rows = len(self.map)
        if direction == 3 and new_pos[0] <= 0:
            new_pos[0] = 0
            if self.map[new_pos[1]][new_pos[0]] is None:
                new_pos[0] += 1
            message = f"Вы уперлись в стену и находитесь в помещении '<u>{self.map[new_pos[1]][new_pos[0]]}</u>'"
        if direction == 1 and new_pos[0] >= col_s - 1:
            new_pos[0] = col_s - 1
            if self.map[new_pos[1]][new_pos[0]] is None:
                new_pos[0] -= 1
            message = f"Вы уперлись в стену и находитесь в помещении '<u>{self.map[new_pos[1]][new_pos[0]]}</u>'"
        if direction == 0 and new_pos[1] <= 0:
            new_pos[1] = 0
            if self.map[new_pos[1]][new_pos[0]] is None:
                new_pos[1] += 1
            message = f"Вы уперлись в стену и находитесь в помещении '<u>{self.map[new_pos[1]][new_pos[0]]}</u>'"
        if direction == 2 and new_pos[1] >= rows - 1:
            new_pos[1] = rows - 1
            if self.map[new_pos[1]][new_pos[0]] is None:
                new_pos[1] -= 1
            message = f"Вы уперлись в стену и находитесь в помещении '<u>{self.map[new_pos[1]][new_pos[0]]}</u>'"
        message_class = "alert alert-warning"
        self.x = new_pos[0]
        self.y = new_pos[1]
        if self.x == self.desired_x and self.y == self.desired_y:
            message = f"Вы достигли желаемого помещения (<u>{self.map[new_pos[1]][new_pos[0]]}</u>)"
            message_class = "alert alert-success"
        if message is None:
            message = f"Вы находитесь в помещении '<u>{self.map[new_pos[1]][new_pos[0]]}</u>'"
            message_class = "alert alert-info"
        return message, message_class
