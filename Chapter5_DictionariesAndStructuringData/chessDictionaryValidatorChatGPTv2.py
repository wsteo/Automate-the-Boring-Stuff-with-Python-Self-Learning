def isValidChessBoard(board):
    # Counters to track the number of pieces for each player
    black_kings = white_kings = 0
    black_pieces = white_pieces = 0
    black_pawns = white_pawns = 0

    # Valid pieces and their counts
    valid_pieces = {'wpawn', 'bpawn', 'wknight', 'bknight', 'wbishop', 'bbishop',
                    'wrook', 'brook', 'wqueen', 'bqueen', 'wking', 'bking'}

    # Valid board coordinates
    valid_coordinates = set('12345678')  # Ranks
    valid_coordinates.update('abcdefgh')  # Files

    for square, piece in board.items():
        # Check if piece name is valid
        if piece not in valid_pieces:
            return False

        # Check if coordinates are valid
        if square[0] not in valid_coordinates or square[1] not in valid_coordinates:
            return False

        # Count pieces and check for kings
        if piece.startswith('b'):
            black_pieces += 1
            if piece == 'bking':
                black_kings += 1
        elif piece.startswith('w'):
            white_pieces += 1
            if piece == 'wking':
                white_kings += 1

        # Count pawns
        if piece == 'bpawn':
            black_pawns += 1
        elif piece == 'wpawn':
            white_pawns += 1

    # Check if each player has at most 16 pieces and at most 8 pawns
    if black_pieces > 16 or white_pieces > 16 or black_pawns > 8 or white_pawns > 8:
        return False

    # Check if each player has exactly one king
    if black_kings != 1 or white_kings != 1:
        return False

    return True

# Example usage:
board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(board))  # Output: True

# Test case with an invalid board (multiple black kings)
invalid_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '4d': 'bking'}
print(isValidChessBoard(invalid_board))  # Output: False

# Test case with an invalid board (exceeding pawn limit for white)
invalid_board_pawns = {
    '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking',
    '7a': 'wpawn', '8b': 'wpawn', '7c': 'wpawn', '8d': 'wpawn', '7e': 'wpawn', '8f': 'wpawn', '7g': 'wpawn', '8h': 'wpawn',
    '1a': 'bpawn', '2b': 'bpawn', '1c': 'bpawn', '2d': 'bpawn', '1e': 'bpawn', '2f': 'bpawn', '1g': 'bpawn', '2h': 'bpawn'
}

print(isValidChessBoard(invalid_board_pawns))  # Output: False
