import unittest
from click.testing import CliRunner

# Import the CLI from main.py
from main import cli


class TestCLI(unittest.TestCase):

    def test_cli_help(self):
        # Creates a fake command-line environment
        runner = CliRunner()

        # Pretends the user ran: python main.py --help
        result = runner.invoke(cli, ["--help"])

        # 0 means the program ran successfully
        self.assertEqual(result.exit_code, 0)

        # Check that Click generated a help page
        self.assertIn("Usage", result.output)


# Run the tests when test_cli.py is executed directly
if __name__ == "__main__":
    unittest.main()