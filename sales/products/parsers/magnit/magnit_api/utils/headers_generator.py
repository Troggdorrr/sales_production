class HeadersGenerator:
    @staticmethod
    def get_api_headers() -> dict:
        return {
            "x-app-version": "0.1.0",
            "x-device-id": "9fui44f7w2",
            "x-device-tag": "disabled",
            "x-platform-version": "window.navigator.userAgent",
        }
