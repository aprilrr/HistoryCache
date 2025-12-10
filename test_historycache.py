# test_historycache.py
"""
Tests for HistoryCache module.
"""

import unittest
from historycache import HistoryCache

class TestHistoryCache(unittest.TestCase):
    """Test cases for HistoryCache class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HistoryCache()
        self.assertIsInstance(instance, HistoryCache)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HistoryCache()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
