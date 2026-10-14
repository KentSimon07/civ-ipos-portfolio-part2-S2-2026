
import unittest
from click.testing import CliRunner
from main import cli


class TestCLI(unittest.TestCase):

    def test_cli_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Usage", result.output)


if __name__ == "__main__":
    unittest.main()
