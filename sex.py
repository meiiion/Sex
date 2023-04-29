import random
from typing import Tuple

from penis_vagina_classes import Penis, Vagina


def do_sex(penis: Penis, vagina: Vagina) -> Tuple[int, int]:
    old_penis, pleasure_vagina, pleasure_penis = vagina.accept(penis)
    penis.size = old_penis
    return (pleasure_vagina, pleasure_penis)

def main():
    vagina = Vagina()
    penis_sizes = ["small", "medium", "large"]
    num_encounters = 1

    for i in range(num_encounters):
        penis_size = random.choice(penis_sizes)
        penis = Penis(penis_size)

        print(f"\nEncounter {i+1}, Penis size: {penis_size}")
        print(f"Before: {vagina.contents}")
        pleasure = do_sex(penis, vagina)
        print(f"After: {vagina.contents}")
        print(f"Pleasure Score: Penis - Size: {penis_size}, Score: {pleasure[0]} / Vagina - Score: {pleasure[1]}")


if __name__ == "__main__":
    main()