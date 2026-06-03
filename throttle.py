from rest_framework.throttling import AnonRateThrottle


class UserSignupTrottle(AnonRateThrottle):
    scope = "sign_up_throttle"
    