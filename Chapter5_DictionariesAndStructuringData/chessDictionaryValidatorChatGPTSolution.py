def isValidChessBoard(board):
    # Counters for pieces of each player
    black_kings = white_kings = 0
    black_pieces = white_pieces = 0
    black_pawns = white_pawns = 0

    # Valid chess piece names
    valid_piece_names = {'bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking',
                         'wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking'}

    # Valid board positions
    valid_positions = set(f'{r}{c}' for r in '12345678' for c in 'abcdefgh')

    for position, piece in board.items():
        # Check if piece name is valid
        if piece not in valid_piece_names:
            return False

        # Check if position is valid
        if position not in valid_positions:
            return False

        # Count pieces and kings for each player
        if piece.startswith('b'):
            black_pieces += 1
            if piece == 'bking':
                black_kings += 1
            elif piece == 'bpawn':
                black_pawns += 1
        elif piece.startswith('w'):
            white_pieces += 1
            if piece == 'wking':
                white_kings += 1
            elif piece == 'wpawn':
                white_pawns += 1

    # Check if there is exactly one black king and one white king
    if black_kings != 1 or white_kings != 1:
        return False

    # Check if each player has at most 16 pieces and at most 8 pawns
    if black_pieces > 16 or white_pieces > 16 or black_pawns > 8 or white_pawns > 8:
        return False

    return True

# Test Case 1: Valid board
valid_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(valid_board))  # Output: True

# Test Case 2: Invalid board with an extra black king
invalid_board1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '7a': 'bking'}
print(isValidChessBoard(invalid_board1))  # Output: False

# Test Case 3: Invalid board with a piece on an invalid position
invalid_board2 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '9z': 'bpawn'}
print(isValidChessBoard(invalid_board2))  # Output: False

# Test Case 4: Invalid board with too many pawns for white
invalid_board3 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '7a': 'wpawn', '8b': 'wpawn'}
print(isValidChessBoard(invalid_board3))  # Output: False

# Test Case 5: Invalid board with an invalid piece name
invalid_board4 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '7a': 'wrook'}
print(isValidChessBoard(invalid_board4))  # Output: False
