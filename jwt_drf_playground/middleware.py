from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from django.utils.functional import SimpleLazyObject


def get_token_user(request):
    """Return user from DRF token."""
    try:
        authenticator = JWTTokenUserAuthentication()
        return authenticator.authenticate(request)[0]
    except Exception as e:
        raise e


class AuthenticationTokenMiddleware:
    """Authentication middleware which return user from token."""

    def __init__(self, get_response):
        """Initializer."""
        self.get_response = get_response

    def __call__(self, request):
        """Response."""
        request.user = SimpleLazyObject(
            lambda: get_token_user(request)
        )

        return self.get_response(request)
