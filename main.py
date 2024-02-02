import copy
import enum


class Orientation(enum.Enum):
	UP = 0
	RIGHT = 1
	DOWN = 2
	LEFT = 3


class Facing(enum.Enum):
	FRONT = 0
	BACK = 1
	UP = 2
	DOWN = 3
	RIGHT = 4
	LEFT = 5


class Cell:
	def __init__(self, value: int, valueOrientation: Orientation):
		# 'Cell' object attributes affectations
		self.__value: int = value
		self.__valueOrientation: Orientation = valueOrientation
	
	def __repr__(self):
		# 'Cell' object representation in string
		return f"<Cell object with value={self.__value} and valueOrientation={self.__valueOrientation}>"
	
	@property
	def value(self):
		# Return the internal 'value' variable
		return self.__value
	
	@property
	def valueOrientation(self):
		# Return the internal 'valueOrientation' variable
		return self.__valueOrientation


class Face:
	PIECE_COUNT = 3
	PIECE_VALUE_INDEX = 0
	PIECE_ORIENTATION_INDEX = 1
	
	def __init__(self, pieceValues: list[list[tuple[int, int]]]):
		# 'Face' object attribute initialization
		self.__cells: list[list[Cell | None]] = [[None for _ in range(self.PIECE_COUNT)]
		                                         for _ in range(self.PIECE_COUNT)]
		
		# Going through the input to store information in the '__cells' attribute
		for xIndex in range(self.PIECE_COUNT):
			for yIndex in range(self.PIECE_COUNT):
				self.__cells[xIndex][yIndex] = \
					Cell(value=pieceValues[xIndex][yIndex][self.PIECE_VALUE_INDEX],
					     valueOrientation=pieceValues[xIndex][yIndex][self.PIECE_ORIENTATION_INDEX])
	
	def __repr__(self):
		# 'Face' object representation
		return f"<Piece object with {self.PIECE_COUNT}x{self.PIECE_COUNT} cells>"
	
	def print(self):
		# 'Face' object displayed in string
		print("'Face' object displayed in string :")
		print('\n'.join(str([self.__cells[xIndex][yIndex].value for yIndex in range(self.PIECE_COUNT)])
		                for xIndex in range(self.PIECE_COUNT)))
	
	def cell(self, facing: Facing):
		# Return one of the 'cell' variable
		pass
	
	@property
	def cells(self):
		# Return the internal 'cells' variable
		return self.__cells
	
	def rotateClockwise(self):
		# Saving the current state of the '__cells' attribute
		cells = copy.deepcopy(self.__cells)
		
		# Going through the input to store information in the '__cells' attribute
		for xIndex in range(self.PIECE_COUNT):
			for yIndex in range(self.PIECE_COUNT):
				self.__cells[yIndex][self.PIECE_COUNT - xIndex - 1] = cells[xIndex][yIndex]
	
	def rotateCounterClockwise(self):
		# Saving the current state of the '__cells' attribute
		cells = copy.deepcopy(self.__cells)
		
		# Going through the input to store information in the '__cells' attribute
		for xIndex in range(self.PIECE_COUNT):
			for yIndex in range(self.PIECE_COUNT):
				self.__cells[self.PIECE_COUNT - yIndex - 1][xIndex] = cells[xIndex][yIndex]
	
	def rotateUTurn(self):
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
	piece1 = Face(pieceValues=piece_Values)
	print(piece1)
	piece1.print()
	piece1.rotateClockwise()
	piece1.print()
	piece1.rotateCounterClockwise()
	piece1.print()
	piece1.rotateUTurn()
	piece1.print()
