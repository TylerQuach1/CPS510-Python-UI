import cx_Oracle
import tkinter as tk
from tkinter import ttk

# Define some constant values
MAIN_WIDTH = 400
MAIN_HEIGHT = 800

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
    VALUES ('Coco', 8.4, '22-NOV-17', 'PG', 'Aspiring musician Miguel, confronted with his family's ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.')
    """)
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('Castaway', 78, '07-DEC-00', 'PG', 'A FedEx executive undergoes a physical and emotional transformation after crash landing on a deserted island.')
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
VALUES (10, 'Jon', ‘Bongo', 'JonBongo@yahoo.com','12345678')    """)

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
            Genre_ID VARCHAR(255) NOT NULL,
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
    VALUES ('Coco', 8.4, '22-NOV-17', 'PG', 'Aspiring musician Miguel, confronted with his family's ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.')
    """)
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('Castaway', 78, '07-DEC-00', 'PG', 'A FedEx executive undergoes a physical and emotional transformation after crash landing on a deserted island.')
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
            MovieGenreID INT PRIMARY KEY,
            Title VARCHAR(255) NOT NULL,
            GenreID INT,
            FOREIGN KEY (Title) REFERENCES Movies(Title),
            FOREIGN KEY (GenreID) REFERENCES Genres(GenreID)
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
VALUES (10, 'Jon', ‘Bongo', 'JonBongo@yahoo.com','12345678')    """)

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
            Score DECIMAL(2,1) NOT NULL CHECK(SCORE BETWEEN 0 AND 10),
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
    VALUES ('Coco', 8.4, '22-NOV-17', 'PG', 'Aspiring musician Miguel, confronted with his family's ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.')
    """)
        cursor.execute(
            """INSERT INTO MOVIE (TITLE, AVG_SCORE, RELEASE_DATE, AGE_RATING, SYNOPSIS)
    VALUES ('Castaway', 78, '07-DEC-00', 'PG', 'A FedEx executive undergoes a physical and emotional transformation after crash landing on a deserted island.')
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
VALUES (10, 'Jon', ‘Bongo', 'JonBongo@yahoo.com','12345678')    """)

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
VALUES (10, 'Jon', ‘Bongo', 'JonBongo@yahoo.com','12345678')    """)

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
VALUES (10, 'Jon', ‘Bongo', 'JonBongo@yahoo.com','12345678')    """)

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
VALUES (10, 'Jon', ‘Bongo', 'JonBongo@yahoo.com','12345678')    """)

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

    values = cursor.execute(query_entry.get())
    for i, value in enumerate(values):
        for j, field in enumerate(value):
            ttk.Label(results_window, text=f'{field}').grid(
                row=i, column=j, padx=GRID_PAD, pady=GRID_PAD)
            
ttk.Label(main_window, text='Movie Table').grid(
    row=2, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_movie_table).grid(
    row=3, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_movie_table).grid(
    row=3, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_movie_table).grid(
    row=3, column=2, padx=GRID_PAD, pady=GRID_PAD)


ttk.Label(main_window, text='Customer Table').grid(
    row=0, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create Table', command=create_customer_table).grid(
    row=1, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop Table', command=drop_customer_table).grid(
    row=1, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate Table', command=populate_customer_table).grid(
    row=1, column=2, padx=GRID_PAD, pady=GRID_PAD)

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
"""
ttk.Label(main_window, text='All Tables').grid(
    row=14, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Create all Tables', command=create_all_table).grid(
    row=15, column=0, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Drop all Tables', command=drop_all_table).grid(
    row=15, column=1, padx=GRID_PAD, pady=GRID_PAD)
ttk.Button(main_window, text='Populate all Tables', command=populate_all_table).grid(
    row=15, column=2, padx=GRID_PAD, pady=GRID_PAD)
"""
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
        return

    main_window.wm_deiconify()
    login_window.destroy()


ttk.Button(login_window, text='Login', command=login).grid(
    column=1, row=2, sticky=tk.E, padx=GRID_PAD, pady=GRID_PAD)

# Run the app
if __name__ == '__main__':
    main_window.withdraw()
    login_window.mainloop()