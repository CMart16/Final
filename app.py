from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')





@app.route('/gallery')
def gallery():
    image_paths = ['Week 146 (Nov. 26 - Dec. 2).jpg', 'Week 145 (Nov. 19 - 25).jpg', 'Week 144 (Nov. 12 - 18).jpg', 'Week 143 (Nov. 5 - 11).jpg',
                   'Week 142 (Oct. 29 - Nov 4).jpg', 'Week 141 (Oct. 22 - 28).jpg']
    width = 450
    height = 300
    return render_template('gallery.html', image_paths=image_paths, width=width, height=height)
if __name__ == '__main__':
    app.run(debug=True)
