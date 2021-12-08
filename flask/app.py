from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}} )

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:php123@localhost/p_final_games'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)
marshmallow = Marshmallow(app)

class Game(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), unique=True)
    platform = database.Column(database.String(15))
    genre = database.Column(database.String(25))
    classification = database.Column(database.String(25))

    def __init__(self, name, platform, genre, classification):
        self.name = name
        self.platform = platform
        self.genre = genre
        self.classification = classification

database.create_all()

class GameSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'name', 'platform', 'genre', 'classification')

game_schema = GameSchema()
games_schema = GameSchema(many=True)

@app.route('/')
def index():
    return "You are running NEEL_API"

@app.route('/api/create_game/', methods=['POST'])
def create_game():
    name = request.json['name']

    databaseGame = Game.query.filter_by(name=name).first()

    if databaseGame is None:
        platform = request.json['platform']
        genre = request.json['genre']
        classification = request.json['classification']
    
        new_game = Game(name, platform, genre, classification)

        database.session.add(new_game)
        database.session.commit()

        return game_schema.jsonify(new_game)
    
    return "0"  

@app.route('/api/games/', methods=['GET'])
def get_games():
    all_games = Game.query.all()
    result = games_schema.dump(all_games)

    return jsonify(result)

@app.route('/api/students/<id>', methods=['GET']) #DEFINIR SI AL FINAL SE USARA EL ENDPOINT
def get_student(id):
    #student = Student.query.get(id)

    #return student_schema.jsonify(student)
    #return id
    return "0"

#PUT Did not worked, I use GET instead
@app.route('/api/update_game/<name>', methods=['GET', 'PUT']) 
def update_game(name):
    game = Game.query.filter_by(name=name).first()

    if game is None:
        return "0"

    platform = request.json['platform']
    classification = request.json['classification']
    genre = request.json['genre']

    game.platform = platform
    game.classification = classification
    game.genre = genre 

    database.session.commit()
    return game_schema.jsonify(game)

#DELETE Did not worked, I use GET instead
@app.route('/api/delete_game/<id>', methods=['GET', 'DELETE']) 
def delete_game(id):
    game = Game.query.get(id)

    if game is None:
        return "0"

    database.session.delete(game)
    database.session.commit()

    return game_schema.jsonify(game)

if __name__ == "__main__":
    app.run(debug=True)


#cors = CORS(app, resources={r"/api/*": {"origins": "*"}} )
#@app.route('/api/v1.0/mensaje')
#def mensaje():
#    return "Running Flask server http://127.0.0.1:5000 Prueba NE"
