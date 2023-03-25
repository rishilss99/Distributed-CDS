from flask import Flask, Response, request, redirect, url_for, flash, render_template, jsonify
from flask_login import LoginManager, current_user, login_required, login_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from webhdfs.webhdfs import PyWebHdfsClient
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '<your-secret-key>' # test:'!F;7j[p#9X^f)kGKLzDqR~sA&*Cm@E1)'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
hdfs = PyWebHdfsClient(host='35.89.209.197', port='50070', user_name='ubuntu')

# Create a login manager
login_manager = LoginManager(app)

# Define a user class
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

# Define a user loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/upload', methods=['GET', 'POST'])
@login_required
@app.route('/user/ubuntu/tr<path:hdfs_path>', methods=['DELETE'])
def hdfs_delete_file(hdfs_path):
    # Delete a file from HDFS
    hdfs.delete_file_dir(hdfs_path)
    return jsonify({'message': 'File deleted successfully.'})
# def upload():
#     if request.method == 'POST':
#         file = request.files['file']
#         webhdfs.create_file('/path/to/file/' + file.filename, file)
#         flash('File uploaded successfully')
#         return redirect(url_for('index'))
#     return render_template('upload.html')

# @app.route('/download/<path:file_path>', methods=['GET'])
# @login_required
# def download(file_path):
#     file_contents = webhdfs.read_file(file_path)
#     return Response(file_contents, mimetype='application/octet-stream')

if __name__ == '__main__':
    db.create_all()
    app.run()
