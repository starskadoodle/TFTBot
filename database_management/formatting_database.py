# https://inloop.github.io/sqlite-viewer/
# https://tftactics.gg/champions/
# https://tactics.tools/
import sqlite3

x = sqlite3.connect("database1.db")
cursor = x.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Traits (
    trait_name varchar(255) PRIMARY KEY,
    trait_image BLOB
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Items (
    item_name varchar(255) PRIMARY KEY,
    item_image BLOB,
    play_rate DECIMAL(5, 2),
    top4_rate DECIMAL(5, 2),
    stats TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Units (
    unit_name varchar(255) PRIMARY KEY,
    unit_image BLOB,
    unit_cost INT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS UnitTraits (
    unit_name varchar(255),
    trait_name varchar(255),
    FOREIGN KEY (unit_name) REFERENCES Units(unit_name),
    FOREIGN KEY (trait_name) REFERENCES Traits(trait_name)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS UnitItems (
    unit_name varchar(255),
    item_name varchar(255),
    ui_playrate decimal(5, 2),
    ui_top4_rate decimal(5, 2),
    FOREIGN KEY (unit_name) REFERENCES Units(unit_name),
    FOREIGN KEY (item_name) REFERENCES Items(item_name)
)
''')

x.commit()
