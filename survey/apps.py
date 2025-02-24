"""
Survey Application Configuration
"""


from django.apps import AppConfig


class SurveyConfig(AppConfig):
    """
    Application Configuration for survey.
    """
    name = 'survey'
    verbose_name = 'survey'

    # Set urls for lms usage
    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': None,  # This removes the automatic namespace
                'relative_path': 'urls',
            }
        }
    }

    def ready(self):
        """
        Connect signal handlers.
        """
        from survey import signals  # pylint: disable=unused-import
