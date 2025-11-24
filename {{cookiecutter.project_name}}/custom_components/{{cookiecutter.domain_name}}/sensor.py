"""Sensor platform for {{ cookiecutter.domain_name }}."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription

from .entity import {{ cookiecutter.class_name_prefix }}Entity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import BlueprintDataUpdateCoordinator
    from .data import {{ cookiecutter.class_name_prefix }}ConfigEntry

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="{{ cookiecutter.domain_name }}",
        name="Integration Sensor",
        icon="mdi:format-quote-close",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: {{ cookiecutter.class_name_prefix }}ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities(
        {{ cookiecutter.class_name_prefix }}Sensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class {{ cookiecutter.class_name_prefix }}Sensor({{ cookiecutter.class_name_prefix }}Entity, SensorEntity):
    """{{ cookiecutter.domain_name }} Sensor class."""

    def __init__(
        self,
        coordinator: BlueprintDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def native_value(self) -> str | None:
        """Return the native value of the sensor."""
        return self.coordinator.data.get("body")
