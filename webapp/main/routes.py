from flask import json, request

from webapp import db   
from webapp.models import Result
from webapp.main import bp

from webapp.main.mocks.places import results as google_places
from webapp.main.mocks.place_details import details as google_place_details
from webapp.main.response_handlers.google_places import get_fields

@bp.route('/health')
def health():
    return '', 200

@bp.route('/ready')
def ready():
    return '', 200

@bp.route('/test', methods=['GET'])
def test():
    return 'Working'

@bp.route('/search', methods=['GET', 'POST'])
def search():
    r = json.loads(request.data.decode('utf-8'))
    search_term = r['search_term']

    places = get_fields(google_places)

    results = {'search_term': search_term, 'places': places}
        
    return results

@bp.route('/place_details', methods=['GET'])
def place_details():
    print
    return {'details': google_place_details['result']}