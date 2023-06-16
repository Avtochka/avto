from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'
# db = SQLAlchemy(app)

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))
#     description = db.Column(db.Text)

#     def __repr__(self):
#         return f"Post(title='{self.title}', description='{self.description}')"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/edit')
def edit():
    # title = request.args['title']
    # category = request.args['category']
    # content = request.args['content']
    
    # print(title,category,content)
    return render_template('editors.html')

@app.route('/loginin')
def loginin():
    return render_template('loginin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/suggested')
def suggested():
    return render_template('suggested.html')



if __name__=="__main__":
    app.run(debug=True)
