import sqlite3
from flask import *

app = Flask(__name__)

conn = sqlite3.connect("my.db")
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
curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (3, 'Львів', 730000, 'Туристиче серце Західної України', 1256, 'https://ukr-prokat.com/wp-content/uploads/2020/07/lviv.jpg')")
curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (4, 'Івано-Франківськ', 270000, 'Аристократичне місто Західної України', 1939, 'https://upload.wikimedia.org/wikipedia/commons/b/bb/Ratush-01.jpg')")

curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (5, 'Чернівці', 280000, 'Одне з найколоритніших і найзатишніших міст України ', 1991, 'https://img.hotels24.ua/photos/ria/new_images/1123/112317/11231725/11231725m.jpg')")
curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (6, 'Харків', 1500000, 'Одне з найбільших та густонаселених міст України', 1654, 'https://www.city.kharkov.ua/assets/images/1(3).jpg')")
curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (7, 'Вінниця', 400000, 'Чудовий населений пункт з багатою історією', 1991, 'https://34travel.me/media/upload/images/2021/APRIL/ua-new/IMG_2948.jpg')")
curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (8, 'Луцьк', 230000, 'Місто Західної України з тисячолітньою історією', 1085, 'https://planetofhotels.com/guide/sites/default/files/styles/big_gallery_image/public/text_gallery/Lutsk-1.jpg')")

conn.commit()

curs.execute("SELECT * FROM cities")
data = curs.fetchall()
for d in data:
    print(d)
    
@app.route("/")
def index():
    return render_template('index.html', sities=data)

app.run(debug=True)