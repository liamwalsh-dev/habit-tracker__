import typer

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from habit_tracker.core import save_habit, delete_habit, mark_done, load_habit
from datetime import date

app = typer.Typer()
console = Console()

@app.command()
def add(habit: str):
    """Add a new habit"""
    if save_habit(habit):
        console.print(f'[green]Привычка "{habit}" добавлена.[/green]')
    else:
        console.print(f'[red]Привычка "{habit}" уже существует.[/red]')

@app.command()
def show():
    """Show all habits"""
    habits = load_habit()
    if not habits:
        print('Привычек пока нет.')
        return
    
    table = Table(title="My Habits")
    table.add_column("№", style="cyan", width=4)
    table.add_column("Привычка", style="white")
    table.add_column("Статус", justify="center", width=8)

    for i, habit in enumerate(habits, 1):
        if habit['date'] == date.today().isoformat():
            status = "[green]✓[/green]"
        else:
            status = "[red]✗[/red]"
        table.add_row(str(i), habit['habit'], status)
    
    console = Console()
    console.print(table)

@app.command()
def done(habit: str):
    """Perform a habit"""
    if mark_done(habit):
        console.print(f'[green]Привычка "{habit}" выполнена сегодня ✓[/green]')
    else:
        console.print(f'[red]Привычка "{habit}" уже выполнена сегодня или не найдена.[/red]')

@app.command()
def delete(habit: str):
    """Delete habit"""
    if delete_habit(habit):
        console.print(f'[red]Привычка "{habit}" удалена.[/red]')
    else:
        console.print(f'[red]Привычка "{habit}" не найдена.[/red]')

@app.command()
def info():
    """Show information about the project"""
    console.print(Panel(
        "[cyan]Author:[/cyan] requeste\n"
        "[cyan]Version:[/cyan] 0.1.0\n"
        "[cyan]GitHub:[/cyan] https://github.com/requeste/habit-tracker\n"
        "[cyan]Description:[/cyan] Its tracker for real developers, created on the basis of jokes. Enter --help to see all the commands.\n\n"
        "[dark_violet]Want a version with English translation? Put your hopes on stars and it will come true.[/dark_violet]",
        title="[bold blue]Habit Tracker[/bold blue]",
        border_style="blue"
    ))

if __name__ == "__main__":
    app()