"""Sensor platform for {{ cookiecutter.domain_name }}."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription

from .entity import {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}Entity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}DataUpdateCoordinator
    from .data import {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}ConfigEntry

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="{{ cookiecutter.domain_name }}",
        name="Integration Sensor",
        icon="mdi:format-quote-close",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities(
        {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}Sensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}Sensor({{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}Entity, SensorEntity):
    """{{ cookiecutter.domain_name }} Sensor class."""

    def __init__(
        self,
        coordinator: {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}DataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def native_value(self) -> str | None:
        """Return the native value of the sensor."""
        return self.coordinator.data.get("body")
