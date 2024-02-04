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
        self.__cells: list[list[Cell | None]] = [[None for _ in range(self.PIECE_COUNT)]
                                                 for _ in range(self.PIECE_COUNT)]

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

    def getEdge(self, facing: Facing):
        # Initialing edge's values variable
        edgesValues = list()

        # Going through the '__cells' attribute to return the edge values
        for index in range(self.PIECE_COUNT):
            # Looking to determine which side of the face we need to return
            match [_facing for _facing in Facing if _facing not in (self.__facing, (self.__facing + 3))] \
                  .index(facing):
                case Orientation.UP:
                    edgesValues.append(self.__cells[0][index])

                case Orientation.RIGHT:
                    edgesValues.append(self.__cells[index][self.PIECE_COUNT - 1])

                case Orientation.DOWN:
                    edgesValues.append(self.__cells[self.PIECE_COUNT - 1][index])

                case Orientation.LEFT:
                    edgesValues.append(self.__cells[index][0])

        # Returning the asked edge's values
        return edgesValues

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


if __name__ == "__main__":
    piece_Values = [[(1, 2),
                     (5, 1),
                     (0, 1)],
                    [(6, 1),
                     (6, 2),
                     (2, 1)],
                    [(6, 3),
                     (4, 0),
                     (9, 0)]]

    print(piece_Values)
    piece1 = Face(pieceValues=piece_Values, facing=Facing.FRONT)
    print(piece1)
    piece1.print()
    piece1.rotate_clockwise()
    piece1.print()
    print(piece1.getEdge(facing=Facing.UP))
    piece1.rotate_counter_clockwise()
    piece1.print()
    print(piece1.getEdge(facing=Facing.RIGHT))
    piece1.rotate_u_turn()
    piece1.print()
    print(piece1.getEdge(facing=Facing.DOWN))
    piece1.print()
    print(piece1.getEdge(facing=Facing.LEFT))
