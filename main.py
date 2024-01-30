class Cell:
    def __init__(self, value: int, orientation: int):
        # 'Cell' object attributes affectations
        self.__value: int = value
        self.__orientation: int = orientation

    def __repr__(self):
        # 'Cell' object representation in string
        return f"<Cell object with value={self.__value} and orientation={self.__orientation}>"

    @property
    def value(self):
        # Return the internal 'value' variable
        return self.__value

    @property
    def orientation(self):
        # Return the internal 'orientation' variable
        return self.__orientation


class Piece:
    PIECE_VALUE_INDEX = 0
    PIECE_ORIENTATION_INDEX = 1

    def __init__(self, pieceValues: list[tuple[int, int]]):
        # 'Piece' object attribute initialization
        self.__cells: list[Cell] = list()

        # Going through the input to store information using attributes
        for indexValue in range(len(pieceValues)):
            self.__cells.append(Cell(value=pieceValues[indexValue][self.PIECE_VALUE_INDEX],
                                     orientation=pieceValues[indexValue][self.PIECE_ORIENTATION_INDEX]))

    def __repr__(self):
        # 'Piece' object representation in string
        return f"<Piece object with {len(self.__cells)} cells>"

    def cell(self, index: int):
        # Return one of the 'cell' variable
        return self.__cells[index]

    @property
    def cells(self):
        # Return the internal 'cells' variable
        return self.__cells


class Face:
    def __init__(self, faceValues: list[list[tuple[int, int]]]):
        # 'Face' object attribute initialization
        self.__pieces: list[Piece] = list()

        # Going through the input to store information using attributes
        for indexValue in range(len(faceValues)):
            self.__pieces.append(Piece(pieceValues=faceValues[indexValue]))

    def __repr__(self):
        # 'Face' object representation in string
        return f"<Piece object with {len(self.__pieces)} pieces>"

    def piece(self, index: int):
        # Return one of the 'piece' variable
        return self.__pieces[index]

    @property
    def pieces(self):
        # Return the internal 'pieces' variable
        return self.__pieces


if __name__ == "__main__":
    FacesValues = [[(3, 3),
                    (8, 0),
                    (5, 1)],
                   [(0, 0),
                    (0, 2)],
                   [(1, 1),
                    (3, 0),
                    (0, 0)],
                   [(8, 2),
                    (8, 0)],
                   [(2, 3)],
                   [(9, 1),
                    (0, 3)],
                   [(6, 1),
                    (7, 0),
                    (7, 0)],
                   [(3, 1),
                    (2, 0)],
                   [(9, 0),
                    (4, 0),
                    (9, 1)]
                   ]

    print(FacesValues)

    piece1 = Face(faceValues=FacesValues)

    print(piece1)
    print(piece1.pieces)
    print(piece1.piece(index=2))
