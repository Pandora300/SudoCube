import copy
import enum


class Orientation(enum.IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Facing(enum.IntEnum):
    FRONT = 0
    UP = 1
    RIGHT = 2
    BACK = 3
    DOWN = 4
    LEFT = 5


class Cell:
    def __init__(self, value: int, value_orientation: Orientation):
        # 'Cell' object attributes affectations
        self.__value: int = value
        self.__value_orientation: Orientation = value_orientation

    def __repr__(self):
        # 'Cell' object representation in string
        return f"<Cell object with value={self.__value} and value_orientation={self.__value_orientation}>"

    @property
    def value(self):
        # Return the internal 'value' variable
        return self.__value

    @property
    def value_orientation(self):
        # Return the internal 'value_orientation' variable
        return self.__value_orientation


class Face:
    PIECE_COUNT = 3
    PIECE_VALUE_INDEX = 0
    PIECE_ORIENTATION_INDEX = 1

    def __init__(self, pieceValues: list[list[tuple[int, int]]], facing: Facing):
        # 'Face' object attribute initialization
        self.__facing = facing
        self.__cells: list[list[Cell | None]] = [[None] * self.PIECE_COUNT] * self.PIECE_COUNT

        # Going through the input to store information in the '__cells' attribute
        for xIndex in range(self.PIECE_COUNT):
            for yIndex in range(self.PIECE_COUNT):
                self.__cells[xIndex][yIndex] = \
                    Cell(value=pieceValues[xIndex][yIndex][self.PIECE_VALUE_INDEX],
                         value_orientation=pieceValues[xIndex][yIndex][self.PIECE_ORIENTATION_INDEX])

    def __repr__(self):
        # 'Face' object representation
        return f"<Piece object with {self.PIECE_COUNT}x{self.PIECE_COUNT} cells facing {self.__facing}>"

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

    def get_edge_values(self, facing: Facing):
        # Initialing edge's values variable
        edges_values = list()

        # Going through the '__cells' attribute to return the edge values
        for index in range(self.PIECE_COUNT):
            # Looking to determine which side of the face we need to return
            match [_facing for _facing in Facing if _facing not in (self.__facing, (self.__facing + 3))].index(facing):
                case Orientation.UP:
                    edges_values.append(self.__cells[0][index])

                case Orientation.RIGHT:
                    edges_values.append(self.__cells[index][self.PIECE_COUNT - 1])

                case Orientation.DOWN:
                    edges_values.append(self.__cells[self.PIECE_COUNT - 1][index])

                case Orientation.LEFT:
                    edges_values.append(self.__cells[index][0])

        # Returning the asked edge's values
        return edges_values

    def set_edge_values(self, facing: Facing, edgesValues: list[Cell]):
        # Going through the '__cells' attribute to return the edge values
        for index in range(self.PIECE_COUNT):
            # Looking to determine which side of the face we need to return
            match [_facing for _facing in Facing if _facing not in (self.__facing, (self.__facing + 3))].index(facing):
                case Orientation.UP:
                    self.__cells[0][index] = edgesValues[index]

                case Orientation.RIGHT:
                    self.__cells[index][self.PIECE_COUNT - 1] = edgesValues[index]

                case Orientation.DOWN:
                    self.__cells[self.PIECE_COUNT - 1][index] = edgesValues[index]

                case Orientation.LEFT:
                    self.__cells[index][0] = edgesValues[index]

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

    def __init__(self, faces_values: dict[Face]):
        self.__faces = [Face(facing=facing, pieceValues=face_values)
                        for facing, face_values in faces_values.items()]

    def rotate_clockwise(self):
        pass

    def rotate_counter_clockwise(self):
        pass

    def rotate_u_turn(self):
        pass


if __name__ == "__main__":
    piece_values = [[(1, Orientation.DOWN),
                     (5, Orientation.RIGHT),
                     (0, Orientation.RIGHT)],
                    [(6, Orientation.RIGHT),
                     (6, Orientation.DOWN),
                     (2, Orientation.RIGHT)],
                    [(6, Orientation.LEFT),
                     (4, Orientation.UP),
                     (9, Orientation.UP)]]

    new_edge = [Cell(value=value, value_orientation=value_orientation)
                for value, value_orientation in [(6, Orientation.DOWN),
                                                 (6, Orientation.RIGHT),
                                                 (6, Orientation.UP)]]

    print(piece_values)
    piece1 = Face(pieceValues=piece_values, facing=Facing.FRONT)
    print(piece1)
    piece1.print()
    piece1.rotate_clockwise()
    piece1.print()
    print(piece1.get_edge_values(facing=Facing.UP))
    piece1.rotate_counter_clockwise()
    piece1.print()
    print(piece1.get_edge_values(facing=Facing.RIGHT))
    piece1.rotate_u_turn()
    piece1.print()
    print(piece1.get_edge_values(facing=Facing.DOWN))
    piece1.print()
    piece1.set_edge_values(Facing.LEFT, new_edge)
    piece1.print()
