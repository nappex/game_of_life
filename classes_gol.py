from time import sleep
from random import randrange


class Game:
    def __init__(self, width, height):
        self.game_field_width = width
        self.game_field_height = height
        self.mark_alive = "🐝"
        self.mark_dead = "⬜️"
        self.field = self.create_gamefield()
        self.put_in_organism()

    def create_gamefield(self):
        field = []
        for line in range(self.game_field_height):
            line = []
            for organism in range(self.game_field_width):
                line.append(self.mark_dead)
            field.append(line)
        return field

    def print_gamefield(self):
        # vykresleni game field
        for line in self.field:
            print()
            for organism in line:
                print(organism, end="")
        print()

    def input_number(self, up_border):
        while True:
            try:
                num = int(input("Write a number of choice: "))
                if num < 0:
                    print("Number can not be negative.\n Try Again !")
                    continue
                elif num > up_border:
                    print(f"You have only {up_border} options to choose.")
                    continue
            except TypeError:
                print("You do not write a number.")

            return num

    def choose_option(self):
        options = ["Square", "Random", "Longlife", "Line"]
        print("Choose start of game: \n")
        for i, option in enumerate(options):
            print(f"{i}: {option} shape")
        num = self.input_number(len(options) - 1)
        return num

    def square_shape(self):
        middle_h = int(self.game_field_height / 2)
        middle_w = int(self.game_field_width / 2)
        for l_index in range(middle_h - 2, middle_h + 3):
            for c_index in range(middle_w - 2, middle_w + 3):
                self.field[l_index][c_index] = self.mark_alive

    def random_shape(self):
        for organism in range(100):
            l_index = randrange(self.game_field_height)
            c_index = randrange(self.game_field_width)
            self.field[l_index][c_index] = self.mark_alive

    def line_shape(self):
        middle_h = int(self.game_field_height / 2)
        middle_w = int(self.game_field_width / 2)
        for coord_w in range(3):
            self.field[middle_h][middle_w + coord_w] = self.mark_alive

    def longlife_shape(self):
        middle_h = int(self.game_field_height / 2)
        middle_w = int(self.game_field_width / 2)
        self.field[middle_h][middle_w] = self.mark_alive
        self.field[middle_h - 1][middle_w] = self.mark_alive
        self.field[middle_h - 1][middle_w + 1] = self.mark_alive
        self.field[middle_h + 1][middle_w] = self.mark_alive
        self.field[middle_h][middle_w - 1] = self.mark_alive

    def put_in_organism(self):
        option = str(self.choose_option())
        if option == "0":
            self.square_shape()
        if option == "1":
            self.random_shape()
        if option == "2":
            self.longlife_shape()
        if option == "3":
            self.line_shape()

    def count_alive(self, line_coord, column_coord):
        alive_organism = 0
        for line_changes in (-1, 0, 1):
            for column_changes in (-1, 0, 1):
                if (line_changes, column_changes) == (0, 0):
                    continue

                coord_l = line_coord + line_changes
                coord_c = column_coord + column_changes

                try:
                    if self.field[coord_l][coord_c] == self.mark_alive:
                        alive_organism += 1
                        # print(f"for coord {line_coord}, {column_coord}")
                        # print("Found organism", coord_l, coord_c, alive_organism)
                except IndexError:
                    continue

        return alive_organism

    def next_generation(self):
        result = self.create_gamefield()
        for l_index, line in enumerate(self.field):
            for c_index, organism in enumerate(line):
                if organism == self.mark_alive:
                    organism_alive = self.count_alive(l_index, c_index)
                    if organism_alive < 2 or organism_alive > 3:
                        result[l_index][c_index] = self.mark_dead
                    else:
                        result[l_index][c_index] = organism
                    # is_alive(organism_alive)
                elif organism == self.mark_dead:
                    organism_alive = self.count_alive(l_index, c_index)
                    if organism_alive == 3:
                        result[l_index][c_index] = self.mark_alive

        return result

    def play(self):
        self.print_gamefield()
        sleep(1)
        while True:
            self.field = self.next_generation()
            self.print_gamefield()
            sleep(1)


def main():
    game_of_life = Game(30, 30)
    game_of_life.play()


if __name__ == "__main__":
    main()
