from website import create_app
app = create_app()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cfwhbgvrhbfh-hvvrgv'
    
if __name__ == '__main__':
    app.run(debug=True)