"""{{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}Entity class."""

from __future__ import annotations

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import ATTRIBUTION
from .coordinator import {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}DataUpdateCoordinator


class {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}Entity(CoordinatorEntity[{{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}DataUpdateCoordinator]):
    """{{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}Entity class."""

    _attr_attribution = ATTRIBUTION

    def __init__(self, coordinator: {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}DataUpdateCoordinator) -> None:
        """Initialize."""
        super().__init__(coordinator)
        self._attr_unique_id = coordinator.config_entry.entry_id
        self._attr_device_info = DeviceInfo(
            identifiers={
                (
                    coordinator.config_entry.domain,
                    coordinator.config_entry.entry_id,
                ),
            },
        )
