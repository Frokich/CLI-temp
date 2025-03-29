import curses
import sys

def print_message(stdscr, message):
    stdscr.clear()
    stdscr.addstr(0, 0, message)
    stdscr.refresh()
    stdscr.getch()

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(0)  # Make getch() blocking
    stdscr.timeout(100)  # Set a timeout for getch()

    current_row = 0
    menu = [
        "Option 1",
        "Option 2",
        "Option 3",
        "Exit"
    ]
    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        for idx, row in enumerate(menu):
            x = width // 2 - len(row) // 2
            y = height // 2 - len(menu) // 2 + idx
            if idx == current_row:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, row)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(menu) - 1:  # Exit option
                break
            print_message(stdscr, f"You selected {menu[current_row]}")

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
# This script creates a simple text-based menu using the curses library.
# It allows the user to navigate through options using the arrow keys and select an option with Enter.
# The selected option is displayed in a message box.
# The script handles keyboard interrupts and other exceptions gracefully.   
# To run this script, make sure you have the curses library available in your Python environment.
# Note: This script is designed to be run in a terminal that supports curses.
# Make sure to run it in a terminal, not in an IDE or text editor.
# The script will exit gracefully when the user presses Ctrl+C or selects the exit option.

