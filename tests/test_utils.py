import utils
import netaddr


def test_mac_has_broadcast_addr():
    assert str(utils.MAC.broadcast) == 'ff:ff:ff:ff:ff:ff'
    assert utils.MAC.broadcast == netaddr.EUI('ff:ff:ff:ff:ff:ff')


def test_mac_takes_argument_and_creates_eui_object():
    assert utils.MAC('11:22:33:44:55:66') == netaddr.EUI('11:22:33:44:55:66')
    assert utils.MAC('12:34:56:78:9a:bc') == netaddr.EUI('12:34:56:78:9a:bc')


def test_mac_has_valid_str_representation():
    assert str(utils.MAC('11:22:33:44:55:66')) == '11:22:33:44:55:66'
    assert str(utils.MAC('12:34:56:78:9a:bc')) == '12:34:56:78:9a:bc'


def test_mac_returns_correct_bool():
    assert bool(utils.MAC('ff:ff:ff:ff:ff:ff')) is False
    assert bool(utils.MAC('12:34:56:78:9a:bc')) is True


def test_host_takes_argument_ip_and_sets_ip_attr_as_netaddr_ipaddress_object():
    assert utils.Host('1.2.3.4').ip == netaddr.IPAddress('1.2.3.4')
    assert utils.Host('23.22.11.58').ip == netaddr.IPAddress('23.22.11.58')


def test_host_takes_optional_mac_argument_and_sets_mac_attr_as_eui_object():
    assert utils.Host('1.2.3.4', mac='12:34:56:78:9a:bc').mac \
        == netaddr.EUI('12:34:56:78:9a:bc')
    assert utils.Host('1.1.1.1', mac='ab:cd:ef:12:34:56').mac \
        == netaddr.EUI('ab:cd:ef:12:34:56')
    assert utils.Host('1.1.1.1').mac is None


def test_host_default_mac_returns_correct_bool():
    assert bool(utils.Host('1.2.3.4', mac='12:34:56:78:9a:bc').mac) is True
    assert bool(utils.Host('1.2.3.4', mac='ff:ff:ff:ff:ff:ff').mac) is False
    assert bool(utils.Host('1.2.3.4').mac) is False


def test_host_has_vendor_attribute_and_is_correctly_set():
    assert utils.Host('1.2.3.4', mac='b4:99:ba:00:00:00').vendor \
        == 'Hewlett Packard'
    assert utils.Host('1.2.3.4', mac='00:50:ba:00:00:00').vendor \
        == 'D-Link Corporation'
