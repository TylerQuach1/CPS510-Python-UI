import cx_Oracle
import tkinter as tk
from tkinter import ttk


# Define some constant values
MAIN_WIDTH = 400
MAIN_HEIGHT = 600

LOGIN_WIDTH = 200
LOGIN_HEIGHT = 100

RESULTS_WIDTH = 500
RESULTS_HEIGHT = 300

GRID_PAD = 5

# Set up UI main window
main_window = tk.Tk()
main_window.title('Clothing Store Application')

# Position window at the center of the screen
main_window.geometry(
    f'{MAIN_WIDTH}x{MAIN_HEIGHT}+{int(main_window.winfo_screenwidth() / 2 - MAIN_WIDTH / 2)}+{int(main_window.winfo_screenheight() / 2 - MAIN_HEIGHT / 2)}')

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)



# Set up UI login window
login_window = tk.Toplevel(main_window)
login_window.title('Login')

# Position window at the center of the screen
login_window.geometry(
    f'{LOGIN_WIDTH}x{LOGIN_HEIGHT}+{int(main_window.winfo_screenwidth() / 2 - LOGIN_WIDTH / 2)}+{int(main_window.winfo_screenheight() / 2 - LOGIN_HEIGHT / 2)}')

login_window.wm_protocol('WM_DELETE_WINDOW', lambda: main_window.destroy())

login_window.columnconfigure(0, weight=1)
login_window.columnconfigure(1, weight=3)

ttk.Label(login_window, text='Username:').grid(
    row=0, column=0, sticky=tk.W, padx=GRID_PAD, pady=GRID_PAD)
username_entry = ttk.Entry(login_window)
username_entry.grid(row=0, column=1, sticky=tk.EW,
                    padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(login_window, text='Password:').grid(
    row=1, column=0, sticky=tk.W, padx=GRID_PAD, pady=GRID_PAD)
password_entry = ttk.Entry(login_window, show='*')
password_entry.grid(row=1, column=1, sticky=tk.EW,
                    padx=GRID_PAD, pady=GRID_PAD)


def login():  # Handle login logic
    username = username_entry.get()
    password = password_entry.get()

    if len(username) == 0 or len(password) == 0:
        print('Please enter username and password')
        return

    global connection, cursor

    # Ryerson database connection
    try:
        connection = cx_Oracle.connect(
            user=username, password=password, dsn=cx_Oracle.makedsn('oracle.scs.ryerson.ca', 1521, sid='orcl'))
        cursor = connection.cursor()
    except:
        print('Error while logging in')
        main_window.destroy()
        return

    main_window.wm_deiconify()
    login_window.destroy()


ttk.Button(login_window, text='Login', command=login).grid(
    column=1, row=2, sticky=tk.E, padx=GRID_PAD, pady=GRID_PAD)

# Run the app
if __name__ == '__main__':
    main_window.withdraw()
    login_window.mainloop()