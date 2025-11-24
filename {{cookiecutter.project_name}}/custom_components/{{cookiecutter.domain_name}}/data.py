"""Custom types for {{ cookiecutter.domain_name }}."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import {{ cookiecutter.class_name_prefix }}ApiClient
    from .coordinator import {{ cookiecutter.class_name_prefix }}DataUpdateCoordinator


type {{ cookiecutter.class_name_prefix }}ConfigEntry = ConfigEntry[{{ cookiecutter.class_name_prefix }}Data]


@dataclass
class {{ cookiecutter.class_name_prefix }}Data:
    """Data for the Blueprint integration."""

    client: {{ cookiecutter.class_name_prefix }}ApiClient
    coordinator: {{ cookiecutter.class_name_prefix }}DataUpdateCoordinator
    integration: Integration
