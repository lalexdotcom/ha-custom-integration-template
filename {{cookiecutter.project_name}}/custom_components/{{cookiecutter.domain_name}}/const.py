"""Constants for {{ cookiecutter.domain_name }}."""

from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

DOMAIN = "{{ cookiecutter.domain_name }}"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
