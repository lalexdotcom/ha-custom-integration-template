"""Custom types for {{ cookiecutter.domain_name }}."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}ApiClient
    from .coordinator import {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}DataUpdateCoordinator


type {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}ConfigEntry = ConfigEntry[{{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}Data]


@dataclass
class {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}Data:
    """Data for the {{ cookiecutter.friendly_name }} integration."""

    client: {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}ApiClient
    coordinator: {{ cookiecutter.domain_name | replace('_', ' ') | title | replace(' ', '') }}DataUpdateCoordinator
    integration: Integration
