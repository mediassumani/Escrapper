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
        scrapper = Escrapper("https://github.com/")
        assert scrapper._clean_data is None
        scrapper.download_data()
        scrapper.clean_up_data()
        assert scrapper._clean_data is not None

    def test_write_in_file(self):

        scrapper = Escrapper("https://www.simplyscripts.com/scripts/familyguy2.html")
        assert scrapper.is_data_written_in_file is False

        scrapper.download_data()
        scrapper.clean_up_data()
        text_file = "tester.txt"
        scrapper.write_in_file(text_file)
        assert scrapper.is_data_written_in_file is True


if __name__ == "__main__":
    unittest.main()
