from flask import json, request

from webapp import db   
from webapp.models import Result
from webapp.main import bp

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
    print(search_term)


    result_objects = Result.query.all()

    results = {'search_term': search_term, 'places': []}

    for i in result_objects:
        results['places'].append({
            'id': i.id,
            'type': i.type,
            'name': i.name
        })
        
    return results