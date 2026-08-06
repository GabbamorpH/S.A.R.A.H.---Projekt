"""
Tests für Shelly API Wrapper
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from src.shelly_api import ShellyAPI


class TestShellyAPI:
    """Test Suite für ShellyAPI"""
    
    def setup_method(self):
        """Setup vor jedem Test"""
        self.device_ip = "192.168.1.50"
        self.api = ShellyAPI(self.device_ip)
    
    # ==========================================
    # INITIALIZATION TESTS
    # ==========================================
    
    def test_init_creates_correct_base_url(self):
        """Test: Init erstellt korrekte Base URL"""
        assert self.api.base_url == "http://192.168.1.50"
        assert self.api.device_ip == "192.168.1.50"
        assert self.api.timeout == 5
    
    def test_init_with_custom_timeout(self):
        """Test: Custom Timeout wird akzeptiert"""
        api = ShellyAPI("192.168.1.50", timeout=10)
        assert api.timeout == 10
    
    # ==========================================
    # CONTROL TESTS
    # ==========================================
    
    def test_control_turn_on_valid(self):
        """Test: Turn on funktioniert"""
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = {}
            mock_get.return_value = mock_response
            
            result = self.api.control("on")
            
            assert result is True
            mock_get.assert_called_once()
    
    def test_control_turn_off_valid(self):
        """Test: Turn off funktioniert"""
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_get.return_value = mock_response
            
            result = self.api.control("off")
            
            assert result is True
    
    def test_control_invalid_action_raises_error(self):
        """Test: Ungültige Action wirft ValueError"""
        with pytest.raises(ValueError):
            self.api.control("invalid")
    
    def test_turn_on_shortcut(self):
        """Test: turn_on() ist Shortcut für control('on')"""
        with patch.object(self.api, 'control') as mock_control:
            mock_control.return_value = True
            result = self.api.turn_on()
            mock_control.assert_called_once_with("on", 0)
    
    def test_turn_off_shortcut(self):
        """Test: turn_off() ist Shortcut für control('off')"""
        with patch.object(self.api, 'control') as mock_control:
            mock_control.return_value = True
            result = self.api.turn_off()
            mock_control.assert_called_once_with("off", 0)
    
    # ==========================================
    # STATUS TESTS
    # ==========================================
    
    def test_is_on_returns_true_when_on(self):
        """Test: is_on() gibt True zurück wenn Gerät an"""
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = {
                'relays': [{'ison': True}]
            }
            mock_get.return_value = mock_response
            
            result = self.api.is_on()
            
            assert result is True
    
    def test_is_on_returns_false_when_off(self):
        """Test: is_on() gibt False zurück wenn Gerät aus"""
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = {
                'relays': [{'ison': False}]
            }
            mock_get.return_value = mock_response
            
            result = self.api.is_on()
            
            assert result is False
    
    def test_get_power_returns_float(self):
        """Test: get_power() gibt Float zurück"""
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = {
                'meters': [{'power': 42.5}]
            }
            mock_get.return_value = mock_response
            
            result = self.api.get_power()
            
            assert isinstance(result, float)
            assert result == 42.5
    
    # ==========================================
    # CONNECTIVITY TESTS
    # ==========================================
    
    def test_is_reachable_returns_true(self):
        """Test: is_reachable() gibt True wenn erreichbar"""
        with patch.object(self.api, 'status') as mock_status:
            mock_status.return_value = {}
            result = self.api.is_reachable()
            assert result is True
    
    def test_is_reachable_returns_false_on_error(self):
        """Test: is_reachable() gibt False bei Fehler"""
        with patch.object(self.api, 'status') as mock_status:
            mock_status.side_effect = Exception("Connection failed")
            result = self.api.is_reachable()
            assert result is False


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
