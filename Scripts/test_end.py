import pytest

from Base.base import UtilsDriver


@pytest.mark.run(order=1999)
class TestEnd:
    def test_end(self):
        # self.broswer = 'chrome'
        # UtilsDriver._quit_mis_driver = True
        UtilsDriver.set_quit_driver(True)
        UtilsDriver.quit_driver()
