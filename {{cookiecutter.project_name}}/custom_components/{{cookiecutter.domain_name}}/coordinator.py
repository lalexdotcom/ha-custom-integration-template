"""DataUpdateCoordinator for {{ cookiecutter.domain_name }}."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import (
    {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}ApiClientAuthenticationError,
    {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}ApiClientError,
)

if TYPE_CHECKING:
    from .data import {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}ConfigEntry


# https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
class {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}DataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    config_entry: {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}ConfigEntry

    async def _async_update_data(self) -> Any:
        """Update data via library."""
        try:
            return await self.config_entry.runtime_data.client.async_get_data()
        except {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}ApiClientAuthenticationError as exception:
            raise ConfigEntryAuthFailed(exception) from exception
        except {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}ApiClientError as exception:
            raise UpdateFailed(exception) from exception
