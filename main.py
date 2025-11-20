from game2dboard import Board

EMPTY = None
BLACK = "⚫"
WHITE = "⚪"
current = BLACK
total = 64

def mouse_fn(btn, row, col):    
    global current, total
    if b[row][col] is not None:
        b.title = "That tile is already taken!"
        return
    
    b[row][col] = current
    current = WHITE if current == BLACK else BLACK
    b.title = f"Othello! Turn: {'Black ⚫' if current == BLACK else 'White ⚪'}"


b = Board(8,8)         
b[3][3] = WHITE
b[4][3] = BLACK
b[3][4] = BLACK
b[4][4] = WHITE

b.title = "Othello!  Turn: Black ⚫"
b.cell_size = 80       
b.cell_color = "green"
b.on_mouse_click = mouse_fn
b.show()
