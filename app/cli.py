# cli.py
import click
from dotenv import load_dotenv
load_dotenv()  # take env variables from .env

@click.command()
def main():
    print("I'm a beautiful CLI ✨")

@click.group()
def cli():
    pass


@cli.command()
def budgets():
    click.echo("Returned budgets")

@cli.command()
def transactions():
    click.echo("Returned transactions")

if __name__ == "__main__":
    main()
