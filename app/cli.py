# cli.py
import click
from .ynab_service import YnabService
from dotenv import load_dotenv
import logging

load_dotenv()  # take env variables from .env

ynab = YnabService()
logger = logging.getLogger()
@click.command()
def main():
    logging.basicConfig(level=logging.INFO)
    print("I'm a beautiful CLI ✨")


@click.group()
def cli():
    pass


@cli.command()
def budgets():
    return ynab.get_budgets()
    click.echo("Returned budgets")


@cli.command()
def transactions():
    click.echo("Returned transactions")


if __name__ == "__main__":
    main()
