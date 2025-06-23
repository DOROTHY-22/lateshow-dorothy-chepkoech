def serialize_episode(episode, include_appearances=True):
    data = {
        'id': episode.id,
        'date': episode.date,
        'number': episode.number
    }
    if include_appearances:
        data['appearances'] = [serialize_appearance(a) for a in episode.appearances]
    return data

def serialize_guest(guest):
    return {
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation
    }

def serialize_appearance(appearance):
    return {
        'id': appearance.id,
        'rating': appearance.rating,
        'episode_id': appearance.episode_id,
        'guest_id': appearance.guest_id,
        'guest': serialize_guest(appearance.guest)
    }
