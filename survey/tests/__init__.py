import sys
from unittest.mock import Mock

mock_openedx = Mock()
mock_openedx.core.djangolib.markup.HTML = Mock()

sys.modules["openedx"] = mock_openedx
sys.modules["openedx.core"] = mock_openedx.core
sys.modules["openedx.core.djangolib"] = mock_openedx.core.djangolib
sys.modules["openedx.core.djangolib.markup"] = mock_openedx.core.djangolib.markup
