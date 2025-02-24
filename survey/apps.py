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

    # Set LMS urls for LTI endpoints
    # Urls are under /api/lti_consumer/
    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'survey',
                'relative_path': 'urls',
            }
        }
    }

    def ready(self):
        """
        Connect signal handlers.
        """
        from survey import signals  # pylint: disable=unused-import
