"""DataUpdateCoordinator for {{ cookiecutter.domain_name }}."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import (
    {{ cookiecutter.class_name_prefix }}ApiClientAuthenticationError,
    {{ cookiecutter.class_name_prefix }}ApiClientError,
)

if TYPE_CHECKING:
    from .data import {{ cookiecutter.class_name_prefix }}ConfigEntry


# https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
class BlueprintDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    config_entry: {{ cookiecutter.class_name_prefix }}ConfigEntry

    async def _async_update_data(self) -> Any:
        """Update data via library."""
        try:
            return await self.config_entry.runtime_data.client.async_get_data()
        except {{ cookiecutter.class_name_prefix }}ApiClientAuthenticationError as exception:
            raise ConfigEntryAuthFailed(exception) from exception
        except {{ cookiecutter.class_name_prefix }}ApiClientError as exception:
            raise UpdateFailed(exception) from exception
