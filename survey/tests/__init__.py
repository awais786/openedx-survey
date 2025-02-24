import sys
from unittest.mock import Mock

import sys
from unittest.mock import Mock

def _mock_third_party_modules():
    mock_openedx = Mock()

    # Mock 'openedx.core.djangolib.markup.HTML'
    mock_openedx.core.djangolib.markup.HTML = Mock()

    # Mock 'openedx.core.djangoapps.user_api.accounts.signals'
    mock_openedx.core.djangoapps.user_api.accounts = Mock()
    mock_openedx.core.djangoapps.user_api.accounts.signals = Mock()

    # Mock 'USER_RETIRE_LMS_MISC'
    mock_openedx.core.djangoapps.user_api.accounts.signals.USER_RETIRE_LMS_MISC = Mock()

    # Mock 'openedx.core.djangoapps.user_api.accounts.tests.retirement_helpers.fake_completed_retirement'
    mock_openedx.core.djangoapps.user_api.accounts.tests = Mock()
    mock_openedx.core.djangoapps.user_api.accounts.tests.retirement_helpers = Mock()
    mock_openedx.core.djangoapps.user_api.accounts.tests.retirement_helpers.fake_completed_retirement = Mock()

    # Mock 'xmodule.modulestore.tests.django_utils.ModuleStoreTestCase'
    mock_xmodule = Mock()
    mock_xmodule.modulestore = Mock()
    mock_xmodule.modulestore.tests = Mock()
    mock_xmodule.modulestore.tests.django_utils = Mock()
    mock_xmodule.modulestore.tests.django_utils.ModuleStoreTestCase = Mock()

    # Mock 'xmodule.modulestore.tests.factories.CourseFactory'
    mock_xmodule.modulestore.tests.factories = Mock()
    mock_xmodule.modulestore.tests.factories.CourseFactory = Mock()

    mock_openedx.core.djangoapps.site_configuration = Mock()
    mock_openedx.core.djangoapps.site_configuration.helpers = Mock()

    # Register mocks in sys.modules
    sys.modules["openedx"] = mock_openedx
    sys.modules["openedx.core"] = mock_openedx.core
    sys.modules["openedx.core.djangolib"] = mock_openedx.core.djangolib
    sys.modules["openedx.core.djangolib.markup"] = mock_openedx.core.djangolib.markup
    sys.modules["openedx.core.djangolib.markup.HTML"] = mock_openedx.core.djangolib.markup.HTML

    sys.modules["openedx.core.djangoapps"] = mock_openedx.core.djangoapps
    sys.modules["openedx.core.djangoapps.user_api"] = mock_openedx.core.djangoapps.user_api
    sys.modules["openedx.core.djangoapps.user_api.accounts"] = mock_openedx.core.djangoapps.user_api.accounts
    sys.modules[
        "openedx.core.djangoapps.user_api.accounts.signals"] = mock_openedx.core.djangoapps.user_api.accounts.signals
    sys.modules["openedx.core.djangoapps.user_api.accounts.tests"] = mock_openedx.core.djangoapps.user_api.accounts.tests
    sys.modules[
        "openedx.core.djangoapps.user_api.accounts.tests.retirement_helpers"] = mock_openedx.core.djangoapps.user_api.accounts.tests.retirement_helpers

    sys.modules["openedx.core.djangoapps.site_configuration"] = mock_openedx.core.djangoapps.site_configuration
    sys.modules[
        "openedx.core.djangoapps.site_configuration.helpers"] = mock_openedx.core.djangoapps.site_configuration.helpers


    sys.modules["xmodule"] = mock_xmodule
    sys.modules["xmodule.modulestore"] = mock_xmodule.modulestore
    sys.modules["xmodule.modulestore.tests"] = mock_xmodule.modulestore.tests
    sys.modules["xmodule.modulestore.tests.django_utils"] = mock_xmodule.modulestore.tests.django_utils
    sys.modules["xmodule.modulestore.tests.factories"] = mock_xmodule.modulestore.tests.factories

    mock_common = Mock()
    mock_common.djangoapps = Mock()
    mock_common.djangoapps.edxmako = Mock()
    mock_common.djangoapps.edxmako.shortcuts = Mock()
    mock_common.djangoapps.edxmako.shortcuts.render_to_response = Mock()

    sys.modules["common"] = mock_common
    sys.modules["common.djangoapps"] = mock_common.djangoapps
    sys.modules["common.djangoapps.edxmako"] = mock_common.djangoapps.edxmako
    sys.modules["common.djangoapps.edxmako.shortcuts"] = mock_common.djangoapps.edxmako.shortcuts

