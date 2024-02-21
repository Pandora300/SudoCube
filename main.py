import copy
import enum


class Facing(enum.IntEnum):
    FRONT = 0
    UP = 1
    RIGHT = 2
    BACK = 3
    DOWN = 4
    LEFT = 5


class Cell:
    def __init__(self, value: int, value_facing: Facing):
        # 'Cell' object attributes affectations
        self.__value: int = value
        self.__value_facing: Facing = value_facing

    def __repr__(self):
        # 'Cell' object representation in string
        return f"<Cell object with value={self.__value} and value_facing={self.__value_facing}>"

    @property
    def value(self):
        # Return the internal 'value' variable
        return self.__value

    @property
    def value_orientation(self):
        # Return the internal 'value_orientation' variable
        return self.__value_facing


class Face:
    PIECE_COUNT: int = 3
    PIECE_VALUE_INDEX: int = 0
    PIECE_ORIENTATION_INDEX: int = 1

    def __init__(self, pieceValues: list[list[tuple[int, int]]], facing: Facing):
        # 'Face' object attribute initialization
        self.__facing = facing
        self.__cells: list[list[Cell | None]] = [[None] * self.PIECE_COUNT for _ in range(self.PIECE_COUNT)]

        # Going through the input to store information in the '__cells' attribute
        for xIndex in range(self.PIECE_COUNT):
            for yIndex in range(self.PIECE_COUNT):
                self.__cells[xIndex][yIndex] = \
                    Cell(value=pieceValues[xIndex][yIndex][self.PIECE_VALUE_INDEX],
                         value_facing=pieceValues[xIndex][yIndex][self.PIECE_ORIENTATION_INDEX])

        self.EDGES_COLLISION = {Facing.FRONT: {Facing.UP: self.get_top_matrix_row,
                                               Facing.RIGHT: self.get_right_matrix_column,
                                               Facing.DOWN: self.get_bottom_matrix_row,
                                               Facing.LEFT: self.get_left_matrix_column},

                                Facing.DOWN: {Facing.FRONT: self.get_bottom_matrix_row,
                                              Facing.RIGHT: self.get_left_matrix_column,
                                              Facing.BACK: self.get_top_matrix_row,
                                              Facing.LEFT: self.get_right_matrix_column},

                                Facing.RIGHT: {Facing.UP: self.get_top_matrix_row,
                                               Facing.BACK: self.get_right_matrix_column,
                                               Facing.DOWN: self.get_bottom_matrix_row,
                                               Facing.FRONT: self.get_left_matrix_column},

                                Facing.BACK: {Facing.UP: self.get_top_matrix_row,
                                              Facing.RIGHT: self.get_left_matrix_column,
                                              Facing.DOWN: self.get_right_matrix_column,
                                              Facing.LEFT: self.get_bottom_matrix_row},

                                Facing.UP: {Facing.FRONT: self.get_top_matrix_row,
                                            Facing.RIGHT: self.get_left_matrix_column,
                                            Facing.BACK: self.get_bottom_matrix_row,
                                            Facing.LEFT: self.get_right_matrix_column},

                                Facing.LEFT: {Facing.UP: self.get_top_matrix_row,
                                              Facing.FRONT: self.get_right_matrix_column,
                                              Facing.DOWN: self.get_bottom_matrix_row,
                                              Facing.BACK: self.get_left_matrix_column}}

    def __repr__(self):
        # 'Face' object representation
        return f"<Piece object with {self.PIECE_COUNT}x{self.PIECE_COUNT} cells facing {self.__facing.name}>"

    @property
    def cells(self):
        # Return the internal 'cells' variable
        return self.__cells

    @property
    def facing(self):
        # Return the internal 'facing' variable
        return self.__facing

    def print(self):
        # 'Face' object displayed in string
        print("'Face' object displayed in string :")
        print('\n'.join(str([self.__cells[xIndex][yIndex].value for yIndex in range(self.PIECE_COUNT)])
                        for xIndex in range(self.PIECE_COUNT)))

    def get_top_matrix_row(self, index: int):
        return self.__cells[0][index]

    def get_left_matrix_column(self, index: int):
        return self.__cells[index][self.PIECE_COUNT - 1]

    def get_bottom_matrix_row(self, index: int):
        return self.__cells[self.PIECE_COUNT - 1][index]

    def get_right_matrix_column(self, index: int):
        return self.__cells[index][0]

    def set_top_matrix_row(self, index: int, value: int):
        self.__cells[0][index] = value

    def set_left_matrix_column(self, index: int, value: int):
        self.__cells[index][self.PIECE_COUNT - 1] = value

    def set_bottom_matrix_row(self, index: int, value: int):
        self.__cells[self.PIECE_COUNT - 1][index] = value

    def set_right_matrix_column(self, index: int, value: int):
        self.__cells[index][0] = value

    def get_edge_values(self, facing: Facing):
        # Initialing edge's values variable
        edges_values = list()

        # Going through the '__cells' attribute to return the edge values
        for index in range(self.PIECE_COUNT):
            edges_values.append(self.EDGES_COLLISION[self.__facing][facing](index))

        # Returning the asked edge's values
        return edges_values

    def set_edge_values(self, facing: Facing, edgesValues: list[Cell]):
        # Going through the '__cells' attribute to return the edge values
        for index in range(self.PIECE_COUNT):
            pass

    def rotate_clockwise(self):
        # Saving the current state of the '__cells' attribute
        cells = copy.deepcopy(self.__cells)

        # Going through the input to store information in the '__cells' attribute
        for xIndex in range(self.PIECE_COUNT):
            for yIndex in range(self.PIECE_COUNT):
                self.__cells[yIndex][self.PIECE_COUNT - xIndex - 1] = cells[xIndex][yIndex]

    def rotate_counter_clockwise(self):
        # Saving the current state of the '__cells' attribute
        cells = copy.deepcopy(self.__cells)

        # Going through the input to store information in the '__cells' attribute
        for xIndex in range(self.PIECE_COUNT):
            for yIndex in range(self.PIECE_COUNT):
                self.__cells[self.PIECE_COUNT - yIndex - 1][xIndex] = cells[xIndex][yIndex]

    def rotate_u_turn(self):
        # Saving the current state of the '__cells' attribute
        cells = copy.deepcopy(self.__cells)

        # Going through the input to store information in the '__cells' attribute
        for xIndex in range(self.PIECE_COUNT):
            for yIndex in range(self.PIECE_COUNT):
                self.__cells[self.PIECE_COUNT - xIndex - 1][self.PIECE_COUNT - yIndex - 1] = cells[xIndex][yIndex]


class Cube:
    FACE_COUNT = 6

    def __init__(self, faces_values: dict[Facing, list[list[tuple[int, Facing]]]]):
        self.__faces: dict[Facing, Face] = {facing: Face(pieceValues=face_values, facing=facing)
                                            for facing, face_values in faces_values.items()}

    def __repr__(self):
        # 'Cube' object representation in string
        return f"<Cube object with>"

    @property
    def faces(self):
        # Return the internal 'faces' variable
        return self.__faces

    def print(self):
        _str: str = str()
        _str += ' ' * 7 + '+-+-+-+\n'
        _str += '\n'.join(' ' * 7 + '|' + '|'.join(str(cell.value) for cell in cell_row) + '|'
                          for cell_row in self.__faces[Facing.DOWN].cells)
        _str += '\n' + ' ' * 7 + '+-+-+-+\n'
        _str += '\n'.join(' ' * 7 + '|' + '|'.join(str(cell.value) for cell in cell_row) + '|'
                          for cell_row in self.__faces[Facing.BACK].cells)
        _str += '\n+-+-+-++-+-+-++-+-+-+\n'
        _str += '|' + '|'.join(str(cell.value) for cell in self.__faces[Facing.LEFT].cells[0]) + '||' \
                + '|'.join(str(cell.value) for cell in self.__faces[Facing.UP].cells[0]) + '||' \
                + '|'.join(str(cell.value) for cell in self.__faces[Facing.RIGHT].cells[0]) + '|'
        _str += '\n' + '|' + '|'.join(str(cell.value) for cell in self.__faces[Facing.LEFT].cells[1]) + '||' \
                + '|'.join(str(cell.value) for cell in self.__faces[Facing.UP].cells[1]) + '||' \
                + '|'.join(str(cell.value) for cell in self.__faces[Facing.RIGHT].cells[1]) + '|'
        _str += '\n' + '|' + '|'.join(str(cell.value) for cell in self.__faces[Facing.LEFT].cells[2]) + '||' \
                + '|'.join(str(cell.value) for cell in self.__faces[Facing.UP].cells[2]) + '||' \
                + '|'.join(str(cell.value) for cell in self.__faces[Facing.RIGHT].cells[2]) + '|'
        _str += '\n+-+-+-++-+-+-++-+-+-+\n'
        _str += '\n'.join(' ' * 7 + '|' + '|'.join(str(cell.value) for cell in cell_row) + '|'
                          for cell_row in self.__faces[Facing.FRONT].cells)
        _str += '\n' + ' ' * 7 + '+-+-+-+\n'
        print(_str)

    def rotate_clockwise(self, facing: Facing):
        #
        rotating_edges_values: list[list[Cell | None]] = list()
        neighbours_edges_facing = [_facing for _facing in Facing if _facing not in (facing, (facing + 3))]

        #
        self.__faces[facing].rotate_clockwise()

        #
        for _facing in neighbours_edges_facing:
            rotating_edges_values.append(self.__faces[_facing].get_edge_values(facing=facing))

        #
        for facing_index in range(len(neighbours_edges_facing)):
            self.__faces[neighbours_edges_facing[(facing_index + 1) % 4]] \
                .set_edge_values(facing=neighbours_edges_facing[facing_index],
                                 edgesValues=rotating_edges_values[facing_index])

    def rotate_counter_clockwise(self, facing: Facing):
        #
        rotating_edges_values: list[list[Cell | None]] = list()
        neighbours_edges_facing = [_facing for _facing in Facing if _facing not in (facing, (facing + 3))]

        #
        self.__faces[facing].rotate_clockwise()

        #
        for _facing in neighbours_edges_facing:
            rotating_edges_values.append(self.__faces[_facing].get_edge_values(facing=facing))

        #
        for facing_index in range(len(neighbours_edges_facing)):
            self.__faces[neighbours_edges_facing[(facing_index + 3) % 4]] \
                .set_edge_values(facing=neighbours_edges_facing[facing_index],
                                 edgesValues=rotating_edges_values[facing_index])

    def rotate_u_turn(self, facing: Facing):
        #
        rotating_edges_values: list[list[Cell | None]] = list()
        neighbours_edges_facing = [_facing for _facing in Facing if _facing not in (facing, (facing + 3))]

        #
        self.__faces[facing].rotate_clockwise()

        #
        for _facing in neighbours_edges_facing:
            rotating_edges_values.append(self.__faces[_facing].get_edge_values(facing=facing))

        #
        for facing_index in range(len(neighbours_edges_facing)):
            self.__faces[neighbours_edges_facing[(facing_index + 2) % 4]] \
                .set_edge_values(facing=neighbours_edges_facing[facing_index],
                                 edgesValues=rotating_edges_values[facing_index])


if __name__ == "__main__":
    _faces_values = {Facing.FRONT: [[(4, Facing.UP),
                                     (3, Facing.UP),
                                     (6, Facing.UP)],
                                    [(7, Facing.UP),
                                     (5, Facing.UP),
                                     (1, Facing.UP)],
                                    [(7, Facing.UP),
                                     (2, Facing.UP),
                                     (8, Facing.UP)]],
                     Facing.DOWN: [[(3, Facing.UP),
                                    (8, Facing.UP),
                                    (7, Facing.UP)],
                                   [(2, Facing.UP),
                                    (1, Facing.UP),
                                    (7, Facing.UP)],
                                   [(5, Facing.UP),
                                    (6, Facing.UP),
                                    (4, Facing.UP)]],
                     Facing.RIGHT: [[(7, Facing.UP),
                                     (7, Facing.UP),
                                     (1, Facing.UP)],
                                    [(2, Facing.UP),
                                     (4, Facing.UP),
                                     (8, Facing.UP)],
                                    [(5, Facing.UP),
                                     (3, Facing.UP),
                                     (6, Facing.UP)]],
                     Facing.LEFT: [[(1, Facing.UP),
                                    (4, Facing.UP),
                                    (2, Facing.UP)],
                                   [(8, Facing.UP),
                                    (7, Facing.UP),
                                    (3, Facing.UP)],
                                   [(6, Facing.UP),
                                    (7, Facing.UP),
                                    (5, Facing.UP)]],
                     Facing.UP: [[(7, Facing.UP),
                                  (8, Facing.UP),
                                  (7, Facing.UP)],
                                 [(3, Facing.UP),
                                  (6, Facing.UP),
                                  (4, Facing.UP)],
                                 [(2, Facing.UP),
                                  (5, Facing.UP),
                                  (1, Facing.UP)]],
                     Facing.BACK: [[(4, Facing.DOWN),
                                    (2, Facing.DOWN),
                                    (8, Facing.DOWN)],
                                   [(5, Facing.DOWN),
                                    (1, Facing.DOWN),
                                    (6, Facing.DOWN)],
                                   [(7, Facing.DOWN),
                                    (7, Facing.DOWN),
                                    (3, Facing.DOWN)]]}

    cube_1 = Cube(faces_values=_faces_values)
    cube_1.print()
    cube_1.rotate_clockwise(facing=Facing.FRONT)
    cube_1.print()
