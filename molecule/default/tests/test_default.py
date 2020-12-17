import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', [
  'tor', 'torsocks', #'torbrowser-launcher'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed

def test_tor_is_started(host):
    service = host.service('tor')
    if "{{ tor_service_enabled }}":
        assert not service.is_enabled
        assert not service.is_running