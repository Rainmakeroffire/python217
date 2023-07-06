import sqlite3
from csv import reader


def display(query):
    for num, line in enumerate(query, 1):
        print(num, *line)
    print()


with sqlite3.connect('base.db') as base:
    cur = base.cursor()

    script = """
        CREATE TABLE IF NOT EXISTS standings (
            club_id INTEGER PRIMARY KEY AUTOINCREMENT,
            position INTEGER NOT NULL,
            club TEXT NOT NULL,
            points INTEGER,
            goals INTEGER
        );
        
        CREATE TABLE IF NOT EXISTS players (
            player_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            nationality TEXT NOT NULL,
            club_id INTEGER REFERENCES "standings" (club_id)
        );
        
        CREATE TABLE IF NOT EXISTS rating (
            player_id INTEGER REFERENCES "players" (player_id),
            position INTEGER NOT NULL,
            goals INTEGER,
            games INTEGER
        );
    """

    try:
        cur.executescript(script)
    except sqlite3.Error as e:
        print(f'An error occurred when executing the script: {e}')
        if base:
            base.rollback()
    else:
        if base:
            base.commit()

    with open('clubs.csv', 'r', encoding='utf-8') as file:
        csv_reader = reader(file)
        data = [tuple(row) for row in csv_reader]
        table_columns = cur.execute("PRAGMA table_info(standings)").fetchall()
        column_names = [col[1] for col in table_columns if col[1] != 'club_id']
        query = f'INSERT INTO standings ({", ".join(column_names)}) VALUES ({", ".join(["?"] * len(column_names))})'
        cur.executemany(query, data)

    players = [
        ('Lewandowski', 'Poland', 1),
        ('Benzema', 'France', 2),
        ('Griezmann', 'France', 3),
        ('Morata', 'Spain', 3),
        ('Jackson', 'Senegal', 5)
    ]

    for player in players:
        cur.execute('INSERT INTO players VALUES (NULL, ?, ?, ?)', player)

    cur.execute('INSERT INTO rating VALUES (1, 1, 23, 34)')
    cur.execute('INSERT INTO rating VALUES (2, 2, 19, 24)')
    cur.execute('INSERT INTO rating VALUES (3, 3, 15, 38)')
    cur.execute('INSERT INTO rating VALUES (4, 4, 13, 36)')
    cur.execute('INSERT INTO rating VALUES (5, 5, 12, 26)')

    # show the players with the best goal per game ratio
    query = cur.execute('SELECT name, ROUND(goals / CAST(games AS FLOAT), 2) '
                        'FROM players p, rating r '
                        'WHERE p.player_id = r.player_id '
                        'ORDER BY 2 DESC').fetchall()

    display(query)

    # show how many goals were scored by the top scorers in each team
    query = cur.execute('SELECT club, SUM(r.goals) '
                        'FROM standings s, players p, rating r '
                        'WHERE s.club_id = p.club_id AND p.player_id = r.player_id '
                        'GROUP BY 1 '
                        'ORDER BY 2 DESC').fetchall()

    display(query)

    # show the number of goals scored by players from Madrid
    query = cur.execute('SELECT SUM(r.goals) '
                        'FROM standings s, players p, rating r '
                        'WHERE s.club_id = p.club_id AND p.player_id = r.player_id AND s.club LIKE "%Madrid%"'
                        ).fetchone()

    print(*query, '', sep='\n')

    # show the percentage of goals scored by each club's top scorers
    query = cur.execute('SELECT s.club, ROUND(SUM(r.goals) * 100.0 / s.goals, 2) '
                        'FROM standings s '
                        'LEFT JOIN players p ON s.club_id = p.club_id '
                        'LEFT JOIN rating r ON p.player_id = r.player_id '
                        'WHERE r.goals IS NOT NULL '
                        'GROUP BY s.club '
                        'ORDER BY 2 DESC').fetchall()

    display(query)

    # show the number of clubs represented by top scorers, the number of top scorers and their goal per game ratio
    # for each country
    query = cur.execute('SELECT p.nationality, COUNT(s.club), COUNT(r.player_id), '
                        'ROUND(AVG(r.goals / CAST(r.games AS FLOAT)), 2) '
                        'FROM players p '
                        'LEFT JOIN standings s ON s.club_id = p.club_id '
                        'LEFT JOIN rating r ON p.player_id = r.player_id '
                        'GROUP BY 1 '
                        'ORDER BY 4 DESC ').fetchall()

    display(query)






