from flask import jsonify

def handle_bad_request(e):
    response = jsonify({'error': 'Bad Request', 'message': str(e)})
    response.status_code = 400
    return response

def handle_not_found(e):
    response = jsonify({'error': 'Not Found', 'message': str(e)})
    response.status_code = 404
    return response

def handle_internal_server_error(e):
    response = jsonify({'error': 'Internal Server Error', 'message': str(e)})
    response.status_code = 500
    return response
