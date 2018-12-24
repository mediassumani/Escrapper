import unittest
from scrapper import Escrapper

class TestEscrapper(unittest.TestCase):

    def test_init(self):
        scrapper = Escrapper("https://www.simplyscripts.com/scripts/familyguy2.html")
        assert scrapper._raw_data is None
        assert scrapper._clean_data is None
        assert scrapper.url is not None

    def download_data(self):
        scrapper = Escrapper("https://www.simplyscripts.com/scripts/familyguy2.html")
        raw_data = scrapper.download_data()
        assert scrapper.status_code == 200
        assert raw_data is not None


    def test_clean_up_data(self):
        pass

    def test_write_in_file(self):
        pass


if __name__ == "__main__":
    unittest.main()
