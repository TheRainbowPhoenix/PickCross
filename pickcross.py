from gint import *
import time

# --- Configuration & Colors ---
COL_BG      = C_RGB(28, 28, 24)  # Light greenish gray
COL_GRID    = C_RGB(10, 10, 8)   # Dark lines
COL_CELL    = C_RGB(24, 24, 20)  # Unfilled cell
COL_FILLED  = C_RGB(5, 5, 4)     # Hammered cell
COL_TEXT    = C_RGB(2, 2, 2)     # Deep black
COL_PENALTY = C_RGB(31, 5, 5)    # Red for time loss
COL_UI_BG   = C_RGB(22, 22, 18)  # Slightly darker gray for UI

# --- Level Database ---
LEVELS = [
    {
        "name": "Don't Eat",
        "data": [
            [0,0,0,1,1,1,1,0,0,0],
            [0,0,1,1,1,1,1,1,0,0],
            [0,1,1,0,0,0,0,1,1,0],
            [0,1,1,0,0,0,0,1,1,0],
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1],
            [0,0,1,1,1,1,1,1,0,0],
            [0,0,1,1,0,0,1,1,0,0],
            [0,0,1,1,0,0,1,1,0,0],
            [0,0,1,1,1,1,1,1,0,0]
        ]
    },
    {
        "name": "less than 3",
        "data": [
            [0,1,1,0,0,0,1,1,0,0],
            [1,1,1,1,0,1,1,1,1,0],
            [1,1,1,1,1,1,1,1,1,0],
            [1,1,1,1,1,1,1,1,1,0],
            [1,1,1,1,1,1,1,1,1,0],
            [0,1,1,1,1,1,1,1,0,0],
            [0,0,1,1,1,1,1,0,0,0],
            [0,0,0,1,1,1,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
    },
    {
        "name": "Doctor hate it",
        "data": [
            [0,0,0,0,1,1,0,0,0,0],
            [0,0,0,1,1,0,0,0,0,0],
            [0,0,1,1,1,1,1,0,0,0],
            [0,1,1,1,1,1,1,1,0,0],
            [1,1,1,1,1,1,1,1,1,0],
            [1,1,1,1,1,1,1,1,1,0],
            [1,1,1,1,1,1,1,1,1,0],
            [1,1,1,1,1,1,1,1,1,0],
            [0,1,1,1,1,1,1,1,0,0],
            [0,0,1,1,0,1,1,0,0,0]
        ]
    },
    {
        "name": "Go alone",
        "data": [
            [0,0,0,0,0,0,0,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,1,1,1,0,0],
            [0,0,0,0,1,1,1,0,0,0],
            [0,1,0,1,1,1,0,0,0,0],
            [0,1,1,1,1,0,0,0,0,0],
            [0,1,1,1,1,0,0,0,0,0],
            [1,1,1,0,1,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0,0,0,0]
        ]
    },
    {
        "name": "Mirror",
        "data": [
            [0,1,1,1,1,1,1,1,1,0],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,0,0,1,0,1],
            [1,0,1,0,0,0,0,1,0,1],
            [1,0,0,0,1,1,0,0,0,1],
            [1,0,1,0,0,0,0,1,0,1],
            [1,0,0,1,1,1,1,0,0,1],
            [1,1,0,0,0,0,0,0,1,1],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
    },
    {
        "name": "Floating",
        "data": [
            [0,0,1,1,1,1,0,0,0,0],
            [0,1,1,1,1,1,1,0,0,0],
            [0,1,1,1,0,0,1,0,0,0],
            [0,0,1,1,1,1,1,0,0,0],
            [0,0,0,1,1,1,1,1,1,0],
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,1,1,1,1,1,1,0,0],
            [0,0,0,1,1,1,1,0,0,0]
        ]
    },
    {
        "name": "Cozy",
        "data": [
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,0,1,1,1,0,0,0,0],
            [0,0,1,1,1,1,1,0,0,0],
            [0,1,1,1,1,1,1,1,0,0],
            [1,1,1,1,1,1,1,1,1,0],
            [0,1,1,0,0,0,1,1,0,0],
            [0,1,1,0,1,0,1,1,0,0],
            [0,1,1,0,1,0,1,1,0,0],
            [0,1,1,1,1,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
    },
    {
        "name": "Behind you",
        "data": [
            [0,0,1,1,1,1,1,0,0,0],
            [0,1,1,1,1,1,1,1,0,0],
            [1,1,0,1,1,1,0,1,1,0],
            [1,1,0,1,1,1,0,1,1,0],
            [1,1,1,1,0,1,1,1,1,0],
            [0,1,1,1,1,1,1,1,0,0],
            [0,0,1,1,1,1,1,0,0,0],
            [0,0,1,0,1,0,1,0,0,0],
            [0,0,1,1,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
    },
    {
        "name": "We'll Sea",
        "data": [
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,0,1,1,1,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,1,1,1,1,1,0,0,0],
            [0,1,0,0,1,0,0,1,0,0],
            [1,0,0,0,1,0,0,0,1,0],
            [1,0,0,0,1,0,0,0,1,0],
            [0,1,1,1,1,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
    },
    {
        "name": "Groove",
        "data": [
            [0,0,0,0,1,1,1,1,1,0],
            [0,0,0,1,1,1,1,1,1,0],
            [0,0,0,1,0,0,0,0,1,0],
            [0,0,0,1,0,0,0,0,1,0],
            [0,0,0,1,0,0,0,0,1,0],
            [0,1,1,1,0,0,1,1,1,0],
            [1,1,1,1,0,1,1,1,1,0],
            [1,1,1,1,0,1,1,1,1,0],
            [0,1,1,1,0,0,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
    }
]

# --- Game State ---
grid_size = 10
current_level_idx = 0
player_grid = []
hammer_mode = True
time_limit = 30 * 60
start_ticks = 0
penalty_seconds = 0
game_over = False
won = False
show_help = False

TILE_SIZE = 24
OFFSET_X = 60
OFFSET_Y = 130

def get_hints(line):
    hints = []
    count = 0
    for val in line:
        if val == 1: count += 1
        else:
            if count > 0: hints.append(count)
            count = 0
    if count > 0: hints.append(count)
    return hints if hints else [0]

def load_level(idx):
    global current_level_idx, player_grid, row_hints, col_hints, start_ticks, penalty_seconds, won, game_over, mistakes
    current_level_idx = idx
    solution = LEVELS[idx]["data"]
    player_grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    row_hints = [get_hints(row) for row in solution]
    col_hints = [get_hints([solution[r][c] for r in range(grid_size)]) for c in range(grid_size)]
    start_ticks = time.ticks_ms()
    penalty_seconds = 0
    won = False
    game_over = False
    mistakes = 0

def draw_static():
    dclear(COL_BG)
    # Top Bar
    drect(0, 0, DWIDTH, 35, COL_UI_BG)
    dtext(50, 10, COL_TEXT, "PHOEBE'S PICK CROSS")
    
    # Navigation Buttons
    drect(5, 5, 35, 30, COL_CELL)
    dtext(15, 10, COL_TEXT, "<")
    drect(DWIDTH-35, 5, DWIDTH-5, 30, COL_CELL)
    dtext(DWIDTH-25, 10, COL_TEXT, ">")
    drect(DWIDTH-70, 5, DWIDTH-40, 30, COL_CELL)
    dtext(DWIDTH-60, 10, COL_TEXT, "?")

    # Level Name
    lname = LEVELS[current_level_idx]["name"]
    dtext(OFFSET_X, 45, COL_TEXT, "Lv.{}: {}".format(current_level_idx+1, lname))
    
    # Draw Hints (Rows)
    for r in range(grid_size):
        h_str = " ".join(map(str, row_hints[r]))
        w, _ = dsize(h_str, None)
        dtext(OFFSET_X - w - 8, OFFSET_Y + r * TILE_SIZE + 5, COL_TEXT, h_str)
        
    # Draw Hints (Cols)
    for c in range(grid_size):
        hints = col_hints[c]
        for i, h in enumerate(reversed(hints)):
            dtext(OFFSET_X + c * TILE_SIZE + 6, OFFSET_Y - 15 - (i * 12), COL_TEXT, str(h))

def draw_grid():
    for r in range(grid_size):
        for c in range(grid_size):
            px = OFFSET_X + c * TILE_SIZE
            py = OFFSET_Y + r * TILE_SIZE
            val = player_grid[r][c]
            drect(px, py, px + TILE_SIZE - 2, py + TILE_SIZE - 2, COL_CELL if val != 1 else COL_FILLED)
            if val == 2:
                dline(px+4, py+4, px+TILE_SIZE-6, py+TILE_SIZE-6, COL_TEXT)
                dline(px+TILE_SIZE-6, py+4, px+4, py+TILE_SIZE-6, COL_TEXT)

    # UI Mode
    mode_y = OFFSET_Y + grid_size * TILE_SIZE + 25
    drect(OFFSET_X, mode_y, OFFSET_X + 160, mode_y + 35, COL_CELL)
    mode_text = "MODE: HAMMER" if hammer_mode else "MODE: MARK (X)"
    dtext(OFFSET_X + 15, mode_y + 10, COL_TEXT, mode_text)

def draw_timer():
    elapsed = time.ticks_diff(time.ticks_ms(), start_ticks) // 1000
    rem = max(0, time_limit - elapsed - penalty_seconds)
    time_str = "{:02d}:{:02d}".format(rem // 60, rem % 60)
    drect(DWIDTH - 75, 45, DWIDTH, 65, COL_BG)
    dtext(DWIDTH - 70, 48, COL_TEXT, time_str)
    return rem

def draw_help():
    drect(30, 100, DWIDTH-30, 400, COL_CELL)
    drect_border(30, 100, DWIDTH-30, 400, COL_CELL, 2, COL_TEXT)
    dtext(80, 120, COL_TEXT, "HELP / RULES")
    dtext(45, 160, COL_TEXT, "- Fill tiles matching counts")
    dtext(45, 185, COL_TEXT, "- HAMMER reveals picture")
    dtext(45, 210, COL_TEXT, "- MARK (X) helps planning")
    dtext(45, 235, COL_TEXT, "- Wrong hammer = Penalty!")
    dtext(45, 260, COL_TEXT, "- Arrow buttons = Prev/Next")
    dtext(80, 350, COL_TEXT, "Tap to Close")

def check_win():
    sol = LEVELS[current_level_idx]["data"]
    for r in range(grid_size):
        for c in range(grid_size):
            if sol[r][c] == 1 and player_grid[r][c] != 1: return False
    return True

def main():
    global hammer_mode, penalty_seconds, won, game_over, show_help, mistakes
    load_level(0)
    draw_static()

    while True:
        # Update Game
        if not game_over and not won and not show_help:
            rem = draw_timer()
            if rem <= 0: game_over = True
        
        # Draw Components
        draw_grid()
        if show_help: 
            draw_help()
        
        # Handle End State Modal
        if game_over or won:
            modal_y = 220
            drect(40, modal_y, 280, modal_y + 120, COL_CELL)
            drect_border(40, modal_y, 280, modal_y + 120, COL_CELL, 2, COL_TEXT)
            msg = "VICTORY!" if won else "GAME OVER"
            dtext(105, modal_y + 40, COL_TEXT, msg)
            dtext(75, modal_y + 70, COL_TEXT, "Tap to Next Level")
        
        dupdate()
        
        # Input Processing
        ev = pollevent()
        if ev.type == KEYEV_TOUCH_DOWN:
            # If game is over/won, any tap advances level
            if game_over or won:
                load_level((current_level_idx + 1) % len(LEVELS))
                draw_static()
                continue

            if show_help:
                show_help = False
                draw_static()
                continue

            # UI Buttons
            if ev.y < 35:
                if ev.x < 40: # Prev
                    load_level((current_level_idx - 1) % len(LEVELS))
                    draw_static()
                elif ev.x > DWIDTH - 40: # Next
                    load_level((current_level_idx + 1) % len(LEVELS))
                    draw_static()
                elif DWIDTH - 75 < ev.x < DWIDTH - 35: # Help
                    show_help = True
                continue

            # Grid Play
            if not game_over and not won:
                if OFFSET_X <= ev.x < OFFSET_X + grid_size * TILE_SIZE and \
                   OFFSET_Y <= ev.y < OFFSET_Y + grid_size * TILE_SIZE:
                    c, r = (ev.x - OFFSET_X) // TILE_SIZE, (ev.y - OFFSET_Y) // TILE_SIZE
                    if player_grid[r][c] == 0:
                        if hammer_mode:
                            if LEVELS[current_level_idx]["data"][r][c] == 1:
                                player_grid[r][c] = 1
                                if check_win():
                                    won = True
                                    # Redraw immediately to show the final block
                                    draw_grid()
                                    dupdate()
                            else:
                                mistakes += 1
                                loss = 120 if mistakes == 1 else (240 if mistakes == 2 else 480)
                                penalty_seconds += loss
                                dtext(ev.x, ev.y - 15, COL_PENALTY, "ERR!")
                                dupdate()
                                time.sleep(0.4)
                                draw_static()
                        else: 
                            player_grid[r][c] = 2
                    elif player_grid[r][c] == 2 and not hammer_mode:
                        player_grid[r][c] = 0
                
                # Mode Toggle
                mode_y = OFFSET_Y + grid_size * TILE_SIZE + 25
                if OFFSET_X <= ev.x <= OFFSET_X + 160 and mode_y <= ev.y <= mode_y + 35:
                    hammer_mode = not hammer_mode

        if ev.type == KEYEV_DOWN and ev.key == KEY_EXIT: 
            break

main()
