import unittest
from gencontent import *


class TestHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        from_file = open("./content/index.md", "r")
        markdown_content = from_file.read()
        from_file.close()
        title = extract_title(markdown_content)

        self.assertEqual(
            title,
            "Tolkien Fan Club"
        )

if __name__ == "__main__":
    unittest.main()
