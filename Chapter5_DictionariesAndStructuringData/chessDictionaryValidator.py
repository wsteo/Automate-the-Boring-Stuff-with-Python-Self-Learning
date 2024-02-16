chessBoard = []
chessBoardWidth = "abcdefgh"
chessBoardLength = 8


def generateChessBoard():
    for x in range(chessBoardLength, 0, -1):
        for y in range(len(chessBoardWidth)):
            chessBoard.append(str(x) + chessBoardWidth[y])


chessPieceList = []


def generateChessPiece():
    color = ["w", "b"]
    pieceType = ["pawn", "knight", "bishop", "rook", "queen", "king"]
    for i in range(len(color)):
        for y in range(len(pieceType)):
            chesspiece = color[i] + pieceType[y]
            if chesspiece not in chessPieceList:
                chessPieceList.append(chesspiece)


def isValidChessBoard(chessBoardCase):
    # Track number of chess piece on the provided chessboard
    chessPieceCounter = {}
    for k, v in chessBoardCase.items():
        chessPieceCounter.setdefault(v, 0)
        chessPieceCounter[v] = chessPieceCounter[v] + 1

    # All pieces must be on a valid space from '1a' to '8h', that is, a piece can’t be on space '9z'
    for k, v in chessBoardCase.items():
        if not int(k[0]) > 9 and int(k[0]) < 0:
            return False

        if k[1] not in "abcdefgh":
            return False

    # Each player can only have at most 16 pieces, at most 8 pawns
    numberOfBlackPiece = 0
    numberOfWhitePiece = 0
    numberOfbpawn = 0
    numberOfwpawn = 0
    for k, v in chessBoardCase.items():
        if v[0] == "b":
            numberOfBlackPiece += 1
            if v[1:] == "pawn":
                numberOfbpawn += 1
        if v[0] == "w":
            numberOfWhitePiece += 1
            if v[1:] == "pawn":
                numberOfwpawn += 1

    if numberOfWhitePiece > 16 or numberOfBlackPiece > 16:
        return False

    if numberOfwpawn > 8 or numberOfbpawn > 8:
        return False

    # Only one white king and one black king
    if "wking" in chessPieceCounter or "bking" in chessPieceCounter:
        if chessPieceCounter["wking"] > 1:
            return False

        if chessPieceCounter["bking"] > 1:
            return False

    return True


generateChessBoard()
generateChessPiece()


def runTest(testcase, expected_result):
    expected_result_valid = expected_result
    print(isValidChessBoard(testcase) == expected_result_valid)


# Default test case
testcase1 = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bqueen",
    "3e": "wking",
}
runTest(testcase1, True)

# 2 wkings
testcase2 = {
    "1h": "bking",
    "3e": "wking",
    "4e": "wking",
}
runTest(testcase2, False)

# invalid space = 9z
testcase3 = {
    "9z": "bking",
    "3e": "wking",
}
runTest(testcase3, False)

# max number of pawn is 8
testcase5 = {
    "1h": "bking",
    "3e": "wking",
    "1a": "bpawn",
    "3a": "bpawn",
    "5a": "bpawn",
    "7b": "bpawn",
    "8b": "bpawn",
    "6b": "bpawn",
    "4c": "bpawn",
    "7c": "bpawn",
    "1c": "bpawn",
}
runTest(testcase5, False)
