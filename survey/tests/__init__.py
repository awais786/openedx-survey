import sys
from unittest.mock import Mock

import sys
from unittest.mock import Mock


mock_openedx = Mock()
mock_openedx.core.djangolib.markup.HTML = Mock()
mock_openedx.core.djangoapps.user_api.accounts = Mock()
mock_openedx.core.djangoapps.user_api.accounts.signals = Mock()
mock_openedx.core.djangoapps.user_api.accounts.signals.USER_RETIRE_LMS_MISC = Mock()

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
