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