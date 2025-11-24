"""Binary sensor platform for {{ cookiecutter.domain_name }}."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)

from .entity import {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}Entity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}DataUpdateCoordinator
    from .data import {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}ConfigEntry

ENTITY_DESCRIPTIONS = (
    BinarySensorEntityDescription(
        key="{{ cookiecutter.domain_name }}",
        name="{{ cookiecutter.friendly_name}} Binary Sensor",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the binary_sensor platform."""
    async_add_entities(
        {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}BinarySensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}BinarySensor({{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}Entity, BinarySensorEntity):
    """{{ cookiecutter.domain_name }} binary_sensor class."""

    def __init__(
        self,
        coordinator: {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}DataUpdateCoordinator,
        entity_description: BinarySensorEntityDescription,
    ) -> None:
        """Initialize the binary_sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def is_on(self) -> bool:
        """Return true if the binary_sensor is on."""
        return self.coordinator.data.get("title", "") == "foo"
