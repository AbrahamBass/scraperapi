import click
import logging
from src.command import scrapy_command
import os

log_folder = os.path.join(os.path.dirname(__file__), 'src', 'record')
log_file = os.path.join(log_folder, 'record.log')

if not os.path.exists(log_folder):
    os.makedirs(log_folder)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj['logger'] = logging.getLogger("ScrapingApp")

cli.add_command(scrapy_command.css)
cli.add_command(scrapy_command.labels)
cli.add_command(scrapy_command.screenshot)

if __name__ == '__main__':
    cli()