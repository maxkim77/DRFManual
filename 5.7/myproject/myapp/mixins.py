# myapp/mixins.py

class LoggingMixin:
    def log_request(self, request):
        # 요청에 대한 로깅 로직
        print(f"LoggingMixin: Request made to {request.path} with method {request.method}")

    def log_response(self, response):
        # 응답에 대한 로깅 로직
        print(f"LoggingMixin: Response status: {response.status_code}")
