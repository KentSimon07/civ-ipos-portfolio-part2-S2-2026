import click
from task_manager import add_task
from file_handler import load_tasks

@click.command()
def cli():
    """Task Manager CLI."""

    click.echo("Task Manager CLI")

    choice = click.prompt("Enter your choice")

    if choice == "1":
        title = click.prompt("Enter task title")
        description = click.prompt("Enter task description")
        due_date = click.prompt("Enter due date (DD-MM-YYYY)")

        tasks = load_tasks()

        if add_task(tasks, title, description, due_date):
            click.echo("Task added succesfully")
        else:
            click.echo("Task was not added")
            

    elif choice == "2":
        click.echo("Delete Task")

    elif choice == "3":
        click.echo("List Task")

    elif choice == "4":
        click.echo("Exit")

    else:
        click.echo("Invalid Choice")


# Only start the program when main.py is run directly
if __name__ == "__main__":
    cli()