from flask import Flask, jsonify, request
from extensions import db, migrate
from models import Episode, Guest, Appearance
from serialization import serialize_episode, serialize_guest, serialize_appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

# Add this route to handle root URL requests
@app.route('/')
def home():
    return 'Welcome to the Late Show API'


# GET /episodes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([serialize_episode(ep, include_appearances=False) for ep in episodes])

# GET /episodes/<int:id>
@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    return jsonify(serialize_episode(episode))

# GET /guests
@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([serialize_guest(g) for g in guests])

# POST /appearances
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.json
    errors = []
    
    # Validate rating
    if 'rating' not in data or not (1 <= data['rating'] <= 5):
        errors.append('Rating must be between 1 and 5')
    
    # Check existence of episode and guest
    if not Episode.query.get(data.get('episode_id')):
        errors.append('Episode not found')
    if not Guest.query.get(data.get('guest_id')):
        errors.append('Guest not found')
    
    if errors:
        return jsonify({'errors': errors}), 400
    
    appearance = Appearance(
        rating=data['rating'],
        episode_id=data['episode_id'],
        guest_id=data['guest_id']
    )
    db.session.add(appearance)
    db.session.commit()
    
    return jsonify({
        'id': appearance.id,
        'rating': appearance.rating,
        'episode_id': appearance.episode_id,
        'guest_id': appearance.guest_id,
        'episode': serialize_episode(appearance.episode, include_appearances=False),
        'guest': serialize_guest(appearance.guest)
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
