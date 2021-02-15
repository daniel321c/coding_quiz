class Piece:
    def __init__(self, location, priority):
        # self.moves
        # self.rules
        self.location = location
        self.priority = priority

    def isValidMove (self, newX, newY):
        pass

    
class Board:
    def __init__(self, printer):
        self.pieces = self.createPieces()
        self.view = printer

    def move(self, x, y, newX, newY):

        piece =  self.pieces[x][y]

        if(piece is not None and piece.isValidMove(newX, newY)):
            self.pieces[newX][newY] = piece
            self.pieces[x][y] = None

    
    def createPieces(self):
        brd = [None for _ in range(8)]*8
        brd[0][0] = Queen()
        return brd

    def updateView(self):
        self.view.render()

class Printer:
    def __init__(self, board):
        self.board = board

    def render(self):
        for arr in self.board.getPieces():
            for piece in arr:
                if(piece is not None):
                    print(piece.name)
                else:
                    print('O')


class Queen (Piece):
    def __init__(self, location, priority):
        Piece.__init__(self, location, 2)
        
    def isValidMove(self, newLoc):
        if(newLoc[0] == self.location[0] and newLoc[1]!= self.location[1]):
            return True
        
        if(newLoc[1] == self.location[1] and newLoc[0]!=self.location[0]):
            return True
        
        return False

q = queen()
o = queen()
o.nextMove()


class Game:
    def __init__(self):
        pass
    
    def allPossibleMove(self, playerNo, location):

    
    def move(self, playerNO, location, newLocation)
