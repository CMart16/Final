from flask import Flask, render_template
import random
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def main():
    pictures = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg', '20.jpg', '21.jpg']
    random_number = random.randint(0, len(pictures)-1)
    picture = pictures[random_number]
    return render_template('main.html', picture=picture)

@app.route('/gallery')
def gallery():
    image_paths = ['Week 146 (Nov. 26 - Dec. 2).jpg', 'Week 145 (Nov. 19 - 25).jpg', 'Week 144 (Nov. 12 - 18).jpg', 'Week 143 (Nov. 5 - 11).jpg',
                   'Week 142 (Oct. 29 - Nov 4).jpg', 'Week 141 (Oct. 22 - 28).jpg']
    width = 450
    height = 300
    return render_template('gallery.html', image_paths=image_paths, width=width, height=height)
if __name__ == '__main__':
    app.run(debug=True)
