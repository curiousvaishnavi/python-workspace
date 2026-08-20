import numpy as np
import streamlit as st


# -----------------------------
# Game Logic
# -----------------------------

def check_winner(board):

    # Check rows and columns
    if 3 in np.sum(board, axis=1) or 3 in np.sum(board, axis=0):
        return "X"

    if -3 in np.sum(board, axis=1) or -3 in np.sum(board, axis=0):
        return "O"

    # Check diagonals
    if np.trace(board) == 3 or np.trace(np.fliplr(board)) == 3:
        return "X"

    if np.trace(board) == -3 or np.trace(np.fliplr(board)) == -3:
        return "O"

    # Check draw
    if 0 not in board:
        return "Draw"

    return None


# -----------------------------
# Initialize Game
# -----------------------------

if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)

if "current" not in st.session_state:
    st.session_state.current = 1

if "result" not in st.session_state:
    st.session_state.result = None


# -----------------------------
# Function to make a move
# -----------------------------

def make_move(row, col):

    board = st.session_state.board

    # Cell already occupied
    if board[row, col] != 0:
        return

    # Put X or O
    board[row, col] = st.session_state.current

    # Check winner
    result = check_winner(board)

    if result is not None:
        st.session_state.result = result
    else:
        # Switch player
        st.session_state.current *= -1


# -----------------------------
# Reset Game
# -----------------------------

def reset_game():
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.result = None


# -----------------------------
# UI
# -----------------------------

st.title("⭕ Tic-Tac-Toe ❌")

st.write("### Welcome to the Game!")

# Game is still running
if st.session_state.result is None:

    if st.session_state.current == 1:
        player = "X"
    else:
        player = "O"

    st.subheader(f"Player {player}'s Turn")

    # Create 3 rows
    for row in range(3):

        columns = st.columns(3)

        for col in range(3):

            cell = st.session_state.board[row, col]

            # Decide what to show inside button
            if cell == 1:
                symbol = "❌"
            elif cell == -1:
                symbol = "⭕"
            else:
                symbol = " "

            # Create button
            if columns[col].button(
                symbol,
                key=f"cell_{row}_{col}",
                use_container_width=True
            ):
                make_move(row, col)
                st.rerun()


# -----------------------------
# Game Over
# -----------------------------

else:

    result = st.session_state.result

    if result == "Draw":
        st.warning("🤝 Ooh! It's a Draw!")
    else:
        if result == "X":
            st.success("🎉 Player X Wins!")
        else:
            st.success("🎉 Player O Wins!")

    st.write("### Final Board")

    # Display final board
    for row in range(3):

        columns = st.columns(3)

        for col in range(3):

            cell = st.session_state.board[row, col]

            if cell == 1:
                symbol = "❌"
            elif cell == -1:
                symbol = "⭕"
            else:
                symbol = " "

            columns[col].button(
                symbol,
                key=f"final_{row}_{col}",
                use_container_width=True,
                disabled=True
            )

    st.button(
        "🔄 Play Again",
        on_click=reset_game
    )