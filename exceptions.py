# exceptions.py

class CustomDatabaseError(Exception):
    def __init__(self, message):
        super().__init__(message)


class CustomOtherError(Exception):
    def __init__(self, message):
        super().__init__(message)


class CustomLanguageError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"CustomLanguageError: {super().__str__()}"


class ComponentPropertyDataError(Exception):
    pass


class ComponentPropertyNotFoundError(ComponentPropertyDataError):
    pass


class ComponentPropertyDatabaseError(ComponentPropertyDataError):
    pass


class ComponentTypographyDataError(Exception):
    pass


class ComponentTypographyNotFoundError(ComponentTypographyDataError):
    pass


class ComponentTypographyDatabaseError(ComponentTypographyDataError):
    pass


class TokenKeyError(Exception):
    pass


class TokenKeyDatabaseError(TokenKeyError):
    pass


class TokenAvailabilityError(Exception):
    pass


class TokenAvailabilityDatabaseError(TokenAvailabilityError):
    pass
