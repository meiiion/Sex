import random
from typing import Tuple

class Penis:
    def __init__(self, size: str):
        self.size = size

class Vagina:
    def __init__(self):
        self.contents = []
    
    def accept(self, penis: Penis) -> Tuple[str, int, int]:
        pleasure_penis = random.randint(1, 10)
        pleasure_vagina = random.randint(1, 10)
        self.contents.append((penis.size, pleasure_penis))
        if len(self.contents) > 1:
            old_penis, old_pleasure = self.contents.pop(0)
            return (old_penis, pleasure_vagina, pleasure_penis)
        else:
            return ("", pleasure_vagina, pleasure_penis)