from time import sleep
from random import randrange

# hraci plocha
# vlozeni dvou bunek
# vkladani ruznych bunek a potom zjistovani stavu

WIDTH = 30
HEIGHT = 30


def create_gamefield():
    game_field = []
    for radek in range(HEIGHT):
        radek = []
        for prvek in range(WIDTH):
            radek.append("🧧")
        game_field.append(radek)
    return game_field


def print_gamefield(game_field):
    # vykresleni game field
    for radek in game_field:
        print()
        for item in radek:
            print(item, end="")
    print()


def putin_defined_organisms(game_field):
    for l_index in range(3, 8):
        for c_index in range(3, 8):
            game_field[l_index][c_index] = "🐥"

    return game_field


def putin_random_organisms(game_field):
    for organism in range(8):
        l_index = randrange(HEIGHT)
        c_index = randrange(WIDTH)
        game_field[l_index][c_index] = "🐥"


def putin_longlife(game_field):
    middle_h = int(HEIGHT / 2)
    middle_w = int(WIDTH / 2)
    game_field[middle_h][middle_w] = "🐥"
    game_field[middle_h - 1][middle_w] = "🐥"
    game_field[middle_h - 1][middle_w + 1] = "🐥"
    game_field[middle_h + 1][middle_w] = "🐥"
    game_field[middle_h][middle_w - 1] = "🐥"

    return game_field


def putin_line(game_field):
    game_field[4][5] = "🐥"
    game_field[4][6] = "🐥"
    game_field[4][7] = "🐥"

    return game_field


def count_alive(game_field, line_coord, column_coord):
    alive_organism = 0
    for line_changes in (-1, 0, 1):
        for column_changes in (-1, 0, 1):
            if (line_changes, column_changes) == (0, 0):
                continue

            coord_l = line_coord + line_changes
            coord_c = column_coord + column_changes

            try:
                if game_field[coord_l][coord_c] == "🐥":
                    alive_organism += 1
                    # print(f"for coord {line_coord}, {column_coord}")
                    # print("Found organism", coord_l, coord_c, alive_organism)
            except IndexError:
                continue

    return alive_organism


def input_number(up_border):
    while True:
        try:
            num = int(input("Write a number of choice: "))
            if num < 1:
                print("Number has to be more than zero.\n Try Again !")
                continue
            elif num > up_border:
                print(f"You have only {up_border} options to choose.")
                continue
        except TypeError:
            print("You do not write a number.")

        return num


def change_generation(game_field):
    result = create_gamefield()
    for l_index, radek in enumerate(game_field):
        for c_index, organism in enumerate(radek):
            if organism == "🐥":
                organism_alive = count_alive(game_field, l_index, c_index)
                if organism_alive < 2 or organism_alive > 3:
                    result[l_index][c_index] = "🧧"
                else:
                    result[l_index][c_index] = organism
                # is_alive(organism_alive)
            elif organism == "🧧":
                organism_alive = count_alive(game_field, l_index, c_index)
                if organism_alive == 3:
                    result[l_index][c_index] = "🐥"

    return result


def main():

    game_field = create_gamefield()
    print("For predefined start type '1'.\n For random start type '2'.")
    print("For longlife type 3.")
    print("For line type 4.")
    game_option = input_number(4)
    if game_option == 1:
        game_field = putin_defined_organisms(game_field)
    elif game_option == 2:
        game_field = putin_random_organisms(game_field)
    elif game_option == 3:
        game_field = putin_longlife(game_field)
    elif game_option == 4:
        game_field = putin_line(game_field)

    print_gamefield(game_field)
    # print(count_alive(game_field, 0, 1))

    sleep(1)
    while True:
        game_field = change_generation(game_field)
        print_gamefield(game_field)
        # return None
        sleep(1)


if __name__ == "__main__":
    main()
