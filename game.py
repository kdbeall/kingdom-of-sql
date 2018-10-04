import sqlite3
import shlex
from img2ascii import get_ascii

"""
    Manage the game state.
"""

def start_game():
    print(get_ascii("./assets/intro-castle.png", 0.15, 0.08))
    print("\n")
    print(
    """ 
    Welcome to Kingdom of SQL! Kingdom of SQL is a
    text-based adventure game to learn about SQL in 
    a cyber-medieval setting.
    """
    )
    level_one()

def play():
    while True:
        cmd, *args = shlex.split(input('> '))
        if cmd=='quit' or cmd=='exit':
            break
        elif cmd=='help':
            print('...')
        else:
            print('Unknown command: {}'.format(cmd))


def level_one():
    table_name = "goblins"
    new_field = "name"
    field_type = "TEXT"

    conn = sqlite3.connect("kos_db.sqlite")
    c = conn.cursor()
    try:
        c.execute('CREATE TABLE {tn} ({nf} {ft})'\
            .format(tn=table_name, nf=new_field, ft=field_type))
        c.execute("INSERT INTO goblins VALUES ('bill')")
        c.execute("INSERT INTO goblins VALUES ('will')")
        conn.commit()
    except sqlite3.Error:
        pass

    c.execute("SELECT * FROM goblins;")
    rows = c.fetchall()
    for row in rows:
        print(row)

    c.execute("SELECT * FROM goblins;")
    rows2 = c.fetchall()
    assert(rows == rows2)
    c.close()

if __name__ == "__main__":
    play()
    #start_game()