import rest_framework


def get_default_serializer_context_mocker():
    from django.conf import settings
    mocker_class_str =\
        getattr(settings, 'DEFAULT_SERIALIZER_CONTEXT_MOCKER', None)
    return rest_framework.settings.import_from_string(
        mocker_class_str, 'DEFAULT_SERIALIZER_CONTEXT_MOCKER'
    )


def get_serializer_context_mocker():
    default_mocker = get_default_serializer_context_mocker()
    default_lambda_mocker = lambda: {}

    mocker = default_mocker or default_lambda_mocker

    return mocker


def create_serializer(serializer):
    context_mocker = get_serializer_context_mocker()
    return serializer(context=context_mocker())
