import sqlite3
from flask import *

app = Flask(__name__)

conn = sqlite3.connect("/home/valdemar/Desktop/test_db/my.db")
conn.row_factory = sqlite3.Row
curs = conn.cursor()

curs.execute("DROP TABLE IF EXISTS cities")

curs.execute("""
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER, 
    name_ VARCHAR(50), 
    population_ INTEGER, 
    description_ TEXT, 
    year_of_foundation DATE, 
    image_ VARCHAR(255)
)
""")
curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (1, 'Одеса', 1000000, 'Перлина у моря', 1794, 'https://osama.com.ua/wp-content/uploads/2021/12/36.jpg')")
curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (2, 'Київ', 3000000, 'Столиця України', 430, 'https://www.nta.ua/wp-content/uploads/2022/02/kyyiv.jpg')")

conn.commit()

curs.execute("SELECT * FROM cities")
data = curs.fetchall()
for d in data:
    print(d)
    
@app.route("/")
def index():
    return render_template('index.html', sities=data)

app.run(debug=True)