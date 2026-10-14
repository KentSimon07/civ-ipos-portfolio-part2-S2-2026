import unittest
from click.testing import CliRunner

# Import the CLI from main.py
from main import cli


class TestCLI(unittest.TestCase):

    def test_cli_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Usage", result.output)


# Run the tests when test_cli.py is executed directly
if __name__ == "__main__":
    unittest.main()
