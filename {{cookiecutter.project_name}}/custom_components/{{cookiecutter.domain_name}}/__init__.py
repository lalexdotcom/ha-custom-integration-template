"""
Custom integration to integrate {{ cookiecutter.domain_name }} with Home Assistant.

For more details about this integration, please refer to
https://github.com/ludeeus/{{ cookiecutter.domain_name }}
"""

from __future__ import annotations

from datetime import timedelta
from typing import TYPE_CHECKING

from homeassistant.const import CONF_PASSWORD, CONF_USERNAME, Platform
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.loader import async_get_loaded_integration

from .api import {{ cookiecutter.class_name_prefix }}ApiClient
from .const import DOMAIN, LOGGER
from .coordinator import BlueprintDataUpdateCoordinator
from .data import {{ cookiecutter.class_name_prefix }}Data

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant

    from .data import {{ cookiecutter.class_name_prefix }}ConfigEntry

PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.SWITCH,
]


# https://developers.home-assistant.io/docs/config_entries_index/#setting-up-an-entry
async def async_setup_entry(
    hass: HomeAssistant,
    entry: {{ cookiecutter.class_name_prefix }}ConfigEntry,
) -> bool:
    """Set up this integration using UI."""
    coordinator = BlueprintDataUpdateCoordinator(
        hass=hass,
        logger=LOGGER,
        name=DOMAIN,
        update_interval=timedelta(hours=1),
    )
    entry.runtime_data = {{ cookiecutter.class_name_prefix }}Data(
        client={{ cookiecutter.class_name_prefix }}ApiClient(
            username=entry.data[CONF_USERNAME],
            password=entry.data[CONF_PASSWORD],
            session=async_get_clientsession(hass),
        ),
        integration=async_get_loaded_integration(hass, entry.domain),
        coordinator=coordinator,
    )

    # https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
    await coordinator.async_config_entry_first_refresh()

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: {{ cookiecutter.class_name_prefix }}ConfigEntry,
) -> bool:
    """Handle removal of an entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


async def async_reload_entry(
    hass: HomeAssistant,
    entry: {{ cookiecutter.class_name_prefix }}ConfigEntry,
) -> None:
    """Reload config entry."""
    await hass.config_entries.async_reload(entry.entry_id)
