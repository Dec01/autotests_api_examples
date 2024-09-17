class PathsServices:

    services_paths = {
        'health_check': {
            'service_path_v1': '/v1/_health',
            'service_endpoints_path': {
                'general_path': {
                    'url': '',
                    'methods': ['GET']
                }
            }
        }
    }

class MethodsList:
    methods = {
        'GET': 'GET', 'POST': 'POST', 'PATCH': 'PATCH', 'PUT': 'PUT', 'DELETE': 'DELETE'
    }