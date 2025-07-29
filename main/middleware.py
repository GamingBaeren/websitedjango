from django.urls import resolve

class LogResolvedViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resolver_match = resolve(request.path_info)
        print(f"Resolved URL {request.path_info} to view {resolver_match.view_name} ({resolver_match.func})")
        response = self.get_response(request)
        return response
