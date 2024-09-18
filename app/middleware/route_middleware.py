from flask import request, jsonify
def check_route_exists(app):
    def middleware():
        adapter = app.url_map.bind('')
        try:
            adapter.match(request.path, method=request.method)
        except:
            return jsonify({'message': 'Method not implemented'}), 501
    return middleware