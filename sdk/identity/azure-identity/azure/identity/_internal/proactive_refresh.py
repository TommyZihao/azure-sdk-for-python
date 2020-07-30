# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import abc
import logging
import time
from typing import TYPE_CHECKING

from .._constants import DEFAULT_REFRESH_OFFSET, DEFAULT_TOKEN_REFRESH_RETRY_DELAY

try:
    ABC = abc.ABC
except AttributeError:  # Python 2.7, abc exists, but not ABC
    ABC = abc.ABCMeta("ABC", (object,), {"__slots__": ()})  # type: ignore

if TYPE_CHECKING:
    # pylint:disable=ungrouped-imports,unused-import
    from typing import Any, Optional
    from azure.core.credentials import AccessToken

_LOGGER = logging.getLogger(__name__)


class ProactiveRefresh(ABC):
    def __init__(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        self._last_refresh_time = 0
        super(ProactiveRefresh, self).__init__(*args, **kwargs)

    @abc.abstractmethod
    def _acquire_token_silently(self, *scopes, **kwargs):
        # type: (*str, **Any) -> Optional[AccessToken]
        """Attempt to acquire an access token from a cache or by redeeming a refresh token"""

    @abc.abstractmethod
    def _request_token(self, *scopes, **kwargs):
        # type: (*str, **Any) -> AccessToken
        """Request an access token from the STS"""

    def _should_refresh(self, token):
        # type: (AccessToken) -> bool
        now = int(time.time())
        if token.expires_on - now > DEFAULT_REFRESH_OFFSET:
            return False
        if now - self._last_refresh_time < DEFAULT_TOKEN_REFRESH_RETRY_DELAY:
            return False
        return True

    def _get_token_impl(self, *scopes, **kwargs):
        # type: (*str, **Any) -> AccessToken
        if not scopes:
            raise ValueError('"get_token" requires at least one scope')

        try:
            token = self._acquire_token_silently(*scopes)
            if not token:
                token = self._request_token(*scopes)
            elif self._should_refresh(token):
                try:
                    self._last_refresh_time = int(time.time())
                    token = self._request_token(*scopes, **kwargs)
                except Exception:  # pylint:disable=broad-except
                    pass
            _LOGGER.info("%s.get_token succeeded", self.__class__.__name__)
            return token

        except Exception as ex:
            _LOGGER.warning(
                "%s.get_token failed: %s", self.__class__.__name__, ex, exc_info=_LOGGER.isEnabledFor(logging.DEBUG)
            )
            raise
