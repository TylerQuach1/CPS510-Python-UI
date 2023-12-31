"""
CPS510, Sec 8, Team 12 - Assignment 9

Dante Romita
Eric Ren
Tyler Quach

"""


import cx_Oracle
import tkinter as tk
from tkinter import ttk

# Define some constant values
MAIN_WIDTH = 400
MAIN_HEIGHT = 650

LOGIN_WIDTH = 200
LOGIN_HEIGHT = 100

RESULTS_WIDTH = 500
RESULTS_HEIGHT = 300

GRID_PAD = 5

# Set up UI main window
main_window = tk.Tk()
main_window.title('Movie Database Interface')

# Position window at the center of the screen
main_window.geometry(
    f'{MAIN_WIDTH}x{MAIN_HEIGHT}+{int(main_window.winfo_screenwidth() / 2 - MAIN_WIDTH / 2)}+{int(main_window.winfo_screenheight() / 2 - MAIN_HEIGHT / 2)}')

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)

def create_movie_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""
            CREATE TABLE Movie(
                Title VARCHAR(255) NOT NULL,
                Avg_Score DECIMAL(2,1) NOT NULL,
                Release_Date DATE NOT NULL,
                Age_Rating VARCHAR(2) NOT NULL CHECK( Age_Rating IN ('G', 'PG','R')),
                Synopsis VARCHAR(4000),
            PRIMARY KEY (Title)
            )""")

        ttk.Label(results_window, text="Successfully Created Movie Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def drop_movie_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""DROP TABLE MOVIE""")
        ttk.Label(results_window, text="Successfully Dropped Movie Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def populate_movie_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')
    try:
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('Barbie', 7.1, '21-JUL-23', 'PG', 'Barbie suffers a crisis that leads her to question her world and her existence')
    """)
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('Oppenheimer', 8.6, '21-JUL-23', 'R', 'The story of American scientist, J. Robert Oppenheimer, and his role in the development of the atomic bomb.')
    """)
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('Interstellar', 8.7, '07-NOV-14', 'PG', 'When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.')
    """)
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('Joker', 8.4, '04-OCT-19', 'R', 'During the 1980s, a failed stand-up comedian is driven insane and turns to a life of crime and chaos in Gotham City while becoming an infamous psychopathic crime figure.')
    """)
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('The Notebook', 7.8, '25-JUN-04', 'PG', 'A poor yet passionate young man falls in love with a rich young woman, giving her a sense of freedom. However, social differences soon get in the way.')
    """)
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('Saw X', 7.1, '29-SEP-23', 'R', 'A sick and desperate John travels to Mexico for a risky and experimental medical procedure in hopes of a miracle cure for his cancer only to discover the entire operation is a scam to defraud the most vulnerable.')
    """)
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('The Shawshank Redemption', 9.4, '24-OCT-94', 'R', 'Over the course of several years, two convicts form a friendship, seeking consolation and, eventually, redemption through basic compassion.')
    """)
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('The Godfather', 9.2, '24-MAR-72', 'R', 'Don Vito Corleone, head of a mafia family, decides to hand over his empire to his youngest son Michael. However, his decision unintentionally puts the lives of his loved ones in grave danger.')
    """)
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('Forrest Gump', 8.8, '26-JUL-94', 'PG', 'The history of the United States from the 1950s to the 70s unfolds from the perspective of an Alabama man with an IQ of 75, who yearns to be reunited with his childhood sweetheart.')
    """)
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('Spider-Man: Across the Spider-Verse', 8.7, '2-JUN-23', 'PG', 'Miles Morales catapults across the Multiverse, where he encounters a team of Spider-People charged with protecting its very existence. When the heroes clash on how to handle a new threat, Miles must redefine what it means to be a hero.')
    """)
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('Coco', 8.4, '22-NOV-17', 'PG', 'Aspiring musician Miguel, confronted with his familys ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.')
    """)
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('Castaway', 7.8, '07-DEC-00', 'PG', 'A FedEx executive undergoes a physical and emotional transformation after crash landing on a deserted island.')
    """)
        ttk.Label(results_window, text="Successfully Populated Movie Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def create_customer_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""
            CREATE TABLE Customer (
            Customer_ID int NOT NULL,
            First_Name varchar(255) NOT NULL,
            Last_Name varchar(255) NOT NULL,
            Email varchar(255) NOT NULL,
            Pass varchar(255) NOT NULL,
            PRIMARY KEY (Customer_ID)
            )
            """)

        ttk.Label(results_window, text="Successfully Created Customer Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def drop_customer_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""DROP TABLE CUSTOMER""")
        ttk.Label(results_window, text="Successfully Dropped Customer Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def populate_customer_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')
    try:
        cursor.execute(
            """INSERT INTO CUSTOMER (CUSTOMER_ID, FIRST_NAME, LAST_NAME, EMAIL, PASS)
VALUES (1, 'Tyler', 'Quach', 'Tyler.Quach@torontomu.ca','12345678')
    """)
        cursor.execute(
            """
INSERT INTO CUSTOMER (CUSTOMER_ID, FIRST_NAME, LAST_NAME, EMAIL, PASS)
VALUES (2, 'Eric', 'Ren', 'eric.ren@torontomu.ca','12345678')
    """)
        cursor.execute(
            """INSERT INTO CUSTOMER (CUSTOMER_ID, FIRST_NAME, LAST_NAME, EMAIL, PASS)
VALUES (3,'Dante', 'Romita', 'Dante.Romita@torontomu.ca','12345678')
    """)
        cursor.execute(
            """INSERT INTO CUSTOMER (CUSTOMER_ID, FIRST_NAME, LAST_NAME, EMAIL, PASS)
VALUES (4, 'Billy', 'Bob', 'Billy.Bob@gmail.ca','12345678')
    """)
        cursor.execute(
            """INSERT INTO CUSTOMER (CUSTOMER_ID, FIRST_NAME, LAST_NAME, EMAIL, PASS)
VALUES (5, 'John', 'Doe', 'John.Doe@hotmail.ca','12345678')
    """)
        cursor.execute(
            """INSERT INTO CUSTOMER (CUSTOMER_ID, FIRST_NAME, LAST_NAME, EMAIL, PASS)
VALUES (6, 'Jake', 'Hall', 'JakeHall@gmail.com','12345678')
    """)
        cursor.execute(
            """INSERT INTO CUSTOMER (CUSTOMER_ID, FIRST_NAME, LAST_NAME, EMAIL, PASS)
VALUES (7, 'George', 'Bush', 'GeorgeBush@gmail.com','12345678')
    """)
        cursor.execute(
            """INSERT INTO CUSTOMER (CUSTOMER_ID, FIRST_NAME, LAST_NAME, EMAIL, PASS)
VALUES (8, 'Michael', 'Jackson', 'MichaelJackson@outlook.com','12345678')
    """)
        cursor.execute(
            """INSERT INTO CUSTOMER (CUSTOMER_ID, FIRST_NAME, LAST_NAME, EMAIL, PASS)
VALUES (9, 'Peter', 'Doyle', 'PeterDoyle@outlook.com','12345678')
    """)
        cursor.execute(
            """INSERT INTO CUSTOMER (CUSTOMER_ID, FIRST_NAME, LAST_NAME, EMAIL, PASS)
VALUES (10, 'Jon', 'Bongo', 'JonBongo@yahoo.com','12345678')    """)

        ttk.Label(results_window, text="Successfully Populated Customer Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
def create_genres_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""
            CREATE TABLE Genres (
            Genre_ID INT NOT NULL,
            Genre VARCHAR(255) NOT NULL,
            PRIMARY KEY (Genre_ID)
            )""")

        ttk.Label(results_window, text="Successfully Created Genres Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def drop_genres_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""DROP TABLE GENRES""")
        ttk.Label(results_window, text="Successfully Dropped Genres Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def populate_genres_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')
    try:
        cursor.execute(
            """INSERT INTO Genres (Genre_ID, GENRE)
VALUES (1, 'ACTION')
    """)
        cursor.execute(
            """INSERT INTO Genres (Genre_ID, GENRE)
VALUES (2, 'COMEDY')
    """)
        cursor.execute(
            """INSERT INTO Genres (Genre_ID, GENRE)
VALUES (3, 'DRAMA')
    """)
        cursor.execute(
            """INSERT INTO Genres (Genre_ID, GENRE)
VALUES (4, 'DOCUMENTARY')
    """)
        cursor.execute(
            """INSERT INTO Genres (Genre_ID, GENRE)
VALUES (5, 'INTERNATIONAL')
    """)
        cursor.execute(
            """INSERT INTO Genres (Genre_ID, GENRE)
VALUES (6, 'HORROR')
    """)
        cursor.execute(
            """INSERT INTO Genres (Genre_ID, GENRE)
VALUES (7, 'KIDS')
    """)
        cursor.execute(
            """INSERT INTO Genres (Genre_ID, GENRE)
VALUES (8, 'MUSIC')
    """)
        cursor.execute(
            """INSERT INTO Genres (Genre_ID, GENRE)
VALUES (9, 'SCI-FI')
    """)
        cursor.execute(
            """INSERT INTO Genres (Genre_ID, GENRE)
VALUES (10, 'FANTASY')
    """)
        cursor.execute(
            """INSERT INTO Genres (Genre_ID, GENRE)
VALUES (11, 'THRILLER')
    """)
        cursor.execute(
            """INSERT INTO Genres (Genre_ID, GENRE)
VALUES (12, 'SPORTS')
    """)
        cursor.execute(
            """INSERT INTO Genres (Genre_ID, GENRE)
VALUES (13, 'WESTERN')
    """)
        cursor.execute(
            """INSERT INTO Genres (Genre_ID, GENRE)
VALUES (14, 'ROMANCE')
    """)
        
        ttk.Label(results_window, text="Successfully Populated Genres Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def create_moviegenres_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""
            CREATE TABLE MovieGenres (
            MovieGenre_ID INT NOT NULL,
            Title VARCHAR(255) NOT NULL,
            Genre_ID INT NOT NULL,
            PRIMARY KEY (MovieGenre_ID),
            FOREIGN KEY (Title) REFERENCES Movie(Title),
            FOREIGN KEY (Genre_ID) REFERENCES Genres(Genre_ID)
            
            )""")

        ttk.Label(results_window, text="Successfully Created MovieGenres Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def drop_moviegenres_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""DROP TABLE MovieGenres""")
        ttk.Label(results_window, text="Successfully Dropped MovieGenres Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def populate_moviegenres_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')
    try:
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (1, 'Joker', 3)
    """)
        cursor.execute(
            """
INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (2, 'Joker', 11)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (3, 'Barbie', 2)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (4, 'Barbie', 10)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (5, 'Interstellar', 3)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (6, 'Interstellar', 4)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (7, 'Oppenheimer', 3)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (8, 'Oppenheimer', 4)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (9, 'The Notebook', 3)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (10, 'The Notebook', 14)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (11, 'Saw X', 11)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (12, 'Saw X', 6)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (13, 'The Shawshank Redemption', 3)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (14, 'The Godfather', 3)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (15, 'Forrest Gump', 3)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (16, 'Forrest Gump', 14)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (17, 'Spider-Man: Across the Spider-Verse', 1)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (18, 'Coco', 3)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (19, 'Castaway', 3)
    """)
        cursor.execute(
            """INSERT INTO MOVIEGENRES(MovieGenre_ID, Title, Genre_ID)
VALUES (20, 'Castaway', 14)
    """)
        
        ttk.Label(results_window, text="Successfully Populated Customer Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)        

def create_review_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""
            CREATE TABLE Review (
            Score INT NOT NULL CHECK(SCORE BETWEEN 0 AND 10),
            Message VARCHAR(4000) NOT NULL,
            Review_ID INT NOT NULL,
            Title VARCHAR(255) NOT NULL,
            Customer_ID int NOT NULL,

            PRIMARY KEY(Review_ID),
            FOREIGN KEY (Title) REFERENCES Movie(Title),
            FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)
            )""")

        ttk.Label(results_window, text="Successfully Created Review Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def drop_review_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""DROP TABLE Review""")
        ttk.Label(results_window, text="Successfully Dropped Review Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def populate_review_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')
    try:
        cursor.execute(
            """INSERT INTO REVIEW (SCORE, MESSAGE, REVIEW_ID, TITLE, CUSTOMER_ID)
VALUES (10, 'This movie was phenomenal! Ill be watching it at least 5 more times in theatres, guaranteed!', 1, 'Oppenheimer', 4)

    """)
        cursor.execute(
            """INSERT INTO REVIEW (SCORE, MESSAGE, REVIEW_ID, TITLE, CUSTOMER_ID)
VALUES (2, 'This movie was obnoxious', 2, 'Barbie', 5)
  """)
        cursor.execute(
            """INSERT INTO REVIEW (SCORE, MESSAGE, REVIEW_ID, TITLE, CUSTOMER_ID)
VALUES (9, 'We live in a society', 3, 'Joker', 1)
    """)
        cursor.execute(
            """INSERT INTO REVIEW (SCORE, MESSAGE, REVIEW_ID, TITLE, CUSTOMER_ID)
VALUES (8, 'A galactic journey of epic proportions! I liked it!', 4, 'Interstellar', 2)
    """)
        cursor.execute(
            """INSERT INTO REVIEW (SCORE, MESSAGE, REVIEW_ID, TITLE, CUSTOMER_ID)
VALUES (6, 'Intriguing.', 5, 'The Notebook', 3)
    """)
       
        ttk.Label(results_window, text="Successfully Populated Review Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def create_moderator_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""
            CREATE TABLE Moderator(
            Mod_ID INT NOT NULL,
            Pass VARCHAR(255) NOT NULL,
            Email VARCHAR(255) NOT NULL,

            PRIMARY KEY (Mod_ID)
            )
            """)

        ttk.Label(results_window, text="Successfully Created Moderator Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def drop_moderator_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""DROP TABLE MODERATOR""")
        ttk.Label(results_window, text="Successfully Dropped Moderator Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def populate_moderator_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')
    try:
        cursor.execute(
            """INSERT INTO MODERATOR(MOD_ID, EMAIL, PASS)
VALUES (1, 'Tyler.Quach@torontomu.ca','12345678')

    """)
        cursor.execute(
            """
INSERT INTO MODERATOR(MOD_ID, EMAIL, PASS)
VALUES (2,  'eric.ren@torontomu.ca','12345678')

    """)
        cursor.execute(
            """INSERT INTO MODERATOR(MOD_ID, EMAIL, PASS)
VALUES (3,  'Dante.Romita@torontomu.ca','12345678')

    """)

        ttk.Label(results_window, text="Successfully Populated Moderator Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def create_filmemployee_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""
            CREATE TABLE FilmEmployee (
            Full_Name VARCHAR (255) NOT NULL,
            Movie_Role VARCHAR (255) NOT NULL,
            Employee_ID INT NOT NULL,
            PRIMARY KEY(Employee_ID)
            )
            """)

        ttk.Label(results_window, text="Successfully Created FilmEmployee Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def drop_filmemployee_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""DROP TABLE FilmEmployee""")
        ttk.Label(results_window, text="Successfully Dropped FilmEmployee Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def populate_filmemployee_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')
    try:
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID) VALUES ('Margot Robbie', 'Actor', 1)
    """)
        cursor.execute(
            """
INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID) VALUES ('Ryan Gosling', 'Actor', 2)
    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES ('Greta Gerwig', 'Director', 3)

    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Leonardo DiCaprio', 'Actor', 4)

    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Will Smith', 'Actor', 5)
    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Emma Stone', 'Actor', 6)

    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Guillermo Del Toro', 'Director', 7)

    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Christopher Nolan', 'Director', 8)

    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Natalie Portman', 'Actor', 9)

    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Jennifer  Lawrence', 'Actor', 10)
""")    
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Kevin Greutert', 'Director', 11)
    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Morgan Freeman', 'Actor', 12)
    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Al Pacino', 'Actor', 13)
    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Shameik Moore', 'Actor', 14)
    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Hailee Steinfield', 'Actor', 15)
    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Tom Hanks', 'Actor', 16)
    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Lee Unkrich', 'Director', 17)
""")
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Frank Darabont', 'Director', 18)
    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Francis Ford Capola', 'Director', 19)
    """)
        cursor.execute(
            """INSERT INTO FILMEMPLOYEE(FULL_NAME, MOVIE_ROLE, EMPLOYEE_ID)
VALUES  ('Nick Cassavetes', 'Director', 20)
    """)

        ttk.Label(results_window, text="Successfully Populated FilmEmployee Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
def create_own_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""
           CREATE TABLE Own (
            Own_ID int NOT NULL,
            Customer_ID int NOT NULL,
            Title VARCHAR(255) NOT NULL,
            PRIMARY KEY (Own_ID),
            FOREIGN KEY (Title) REFERENCES Movie(Title),
            FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)
            )
            """)

        ttk.Label(results_window, text="Successfully Created Own Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def drop_own_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""DROP TABLE Own""")
        ttk.Label(results_window, text="Successfully Dropped Own Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def populate_own_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')
    try:
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (1, 1, 'Barbie')
    """)
        cursor.execute(
            """
INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (2, 1, 'Oppenheimer')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (3, 2, 'Oppenheimer')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (4, 2, 'Joker')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (5, 3, 'Joker')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (6, 3, 'The Notebook')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (7, 4, 'The Notebook')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (8, 4, 'Interstellar')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (9, 5, 'Interstellar')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (10, 5, 'Barbie')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (11, 6, 'Interstellar')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (12, 6, 'Barbie')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (13, 7, 'Coco')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (14, 7, 'The Shawshank Redemption')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (15, 8, 'Coco')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (16, 8, 'Spider-Man: Across the Spider-Verse')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (17, 10, 'Forrest Gump')
    """)
        cursor.execute(
            """INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (18, 10, 'The Godfather')
    """)

        ttk.Label(results_window, text="Successfully Populated Own Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
def create_workedon_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""
            CREATE TABLE WorkedOn (
            WorkedOn_ID INT NOT NULL,
            Employee_ID INT NOT NULL,
            Title VARCHAR(255) NOT NULL,
            FOREIGN KEY (Title) REFERENCES Movie(Title),
            FOREIGN KEY (Employee_ID) REFERENCES FilmEmployee(Employee_ID)
            )
            """)

        ttk.Label(results_window, text="Successfully Created WorkedOn Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def drop_workedon_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')

    try:
        cursor.execute("""DROP TABLE WorkedOn""")
        ttk.Label(results_window, text="Successfully Dropped WorkedOn Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def populate_workedon_table():
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')
    try:
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (1, 3, 'Barbie')

    """)
        cursor.execute(
            """
INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (2, 2, 'Barbie')

    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (3, 1, 'Barbie')

    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (4, 10, 'Interstellar')

    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (5, 4, 'Interstellar')

    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (6, 8, 'Interstellar')

    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (7, 9, 'Joker')

    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (8, 5, 'Joker')

    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (9, 7, 'Joker')

    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (10, 4, 'Oppenheimer')
 """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (11, 5, 'Oppenheimer')

    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (12, 8, 'Oppenheimer')

    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (13, 9, 'The Notebook')

    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (14, 6, 'The Notebook')

    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (15, 7, 'The Notebook')

    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (16, 11, 'Saw X')
    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (17, 12, 'The Shawshank Redemption')
 """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (18, 13, 'The Godfather')
    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (19, 14, 'Spider-Man: Across the Spider-Verse')
    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (20, 15, 'Spider-Man: Across the Spider-Verse')
    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (21, 16, 'Forrest Gump')
    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (22, 16, 'Castaway')
    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (23, 17, 'Coco')
    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (24, 18, 'The Shawshank Redemption')
    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (25, 19, 'The Godfather')
    """)
        cursor.execute(
            """INSERT INTO WORKEDON (WorkedOn_ID, EMPLOYEE_ID, TITLE)
VALUES  (26, 20, 'The Notebook')
    """)
        ttk.Label(results_window, text="Successfully Populated WorkedOn Table").pack(
                padx=GRID_PAD, pady=GRID_PAD)
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)

def query():
    # Set up UI results window
    results_window = tk.Toplevel(main_window)
    results_window.title('Results')


    try:
        values = cursor.execute(query_entry.get())

        statement = ((query_entry.get().split()[0]).upper())
        print (statement)
        if statement == "SELECT":
            
            for i, header in enumerate(cursor.description):
                ttk.Label(results_window, text=f'{header[0]}', font='bold').grid(
                    row=0, column=i, padx=GRID_PAD, pady=10)
            for i, value in enumerate(values):
                for j, field in enumerate(value):
                    
                    ttk.Label(results_window, text=f'{field}').grid(
                        row=i + 1, column=j, padx=GRID_PAD, pady=GRID_PAD)
        else:
            ttk.Label(results_window, text=("Successfully ran query\n", query_entry.get()), font='bold').pack(
                padx=GRID_PAD, pady=10)
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        ttk.Label(results_window, text=error.message).pack(
                padx=GRID_PAD, pady=GRID_PAD)


ttk.Label(main_window, text='Movie Table').grid(
    row=0, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_movie_table).grid(
    row=1, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_movie_table).grid(
    row=1, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_movie_table).grid(
    row=1, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='Customer Table').grid(
    row=2, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_customer_table).grid(
    row=3, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_customer_table).grid(
    row=3, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_customer_table).grid(
    row=3, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='Genres Table').grid(
    row=4, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_genres_table).grid(
    row=5, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_genres_table).grid(
    row=5, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_genres_table).grid(
    row=5, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='MovieGenres Table').grid(
    row=6, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_moviegenres_table).grid(
    row=7, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_moviegenres_table).grid(
    row=7, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_moviegenres_table).grid(
    row=7, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='Review Table').grid(
    row=8, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_review_table).grid(
    row=9, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_review_table).grid(
    row=9, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_review_table).grid(
    row=9, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='Moderator Table').grid(
    row=10, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_moderator_table).grid(
    row=11, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_moderator_table).grid(
    row=11, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_moderator_table).grid(
    row=11, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='Film Employee Table').grid(
    row=12, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_filmemployee_table).grid(
    row=13, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_filmemployee_table).grid(
    row=13, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_filmemployee_table).grid(
    row=13, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='Own Table').grid(
    row=14, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_own_table).grid(
    row=15, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_own_table).grid(
    row=15, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_own_table).grid(
    row=15, column=2, padx=GRID_PAD, pady=GRID_PAD)

ttk.Label(main_window, text='Worked On Table').grid(
    row=16, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_workedon_table).grid(
    row=17, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_workedon_table).grid(
    row=17, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_workedon_table).grid(
    row=17, column=2, padx=GRID_PAD, pady=GRID_PAD)

query_entry = ttk.Entry(main_window)
query_entry.grid(row=20, column=0, columnspan=2,
                 sticky=tk.EW, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Query', command=query).grid(
    row=20, column=2, padx=GRID_PAD, pady=GRID_PAD)

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
        dsn = """(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=oracle.scs.ryerson.ca)(Port=1521))(CONNECT_DATA=(SID=orcl)))"""
        connection = cx_Oracle.connect(
            user=username, password=password, dsn=dsn,encoding="UTF-8")
        cursor = connection.cursor()
    except:
        main_window.destroy()
        print("failed to log in")
        return

    main_window.wm_deiconify()
    login_window.destroy()


ttk.Button(login_window, text='Login', command=login).grid(
    column=1, row=2, sticky=tk.E, padx=GRID_PAD, pady=GRID_PAD)

# Run the app
if __name__ == '__main__':
    main_window.withdraw()
    login_window.mainloop()
