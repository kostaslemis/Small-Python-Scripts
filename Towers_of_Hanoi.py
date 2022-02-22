# Towers of Hanoi Game

def main():
    discs_num = 8

    from_pillar = 1
    temp_pillar = 2
    to_pillar = 3

    move_discs(discs_num, from_pillar, to_pillar, temp_pillar)
    print("All discs have been moved to the 3rd pillar successfully !")


def move_discs(num, from_pillar, to_pillar, temp_pillar):
    if num > 0:
        move_discs(num - 1, from_pillar, temp_pillar, to_pillar)
        print("A disc has been moved from pillar", from_pillar, "to pillar", to_pillar)
        move_discs(num - 1, temp_pillar, to_pillar, from_pillar)


if __name__ == "__main__":
    main()
