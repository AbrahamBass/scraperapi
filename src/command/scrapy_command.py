import os
import uuid
import click
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from src.service.browser_service import SeleniumBrowser


@click.command()
@click.option('--home', help='Specify the number of greetings to display.')
@click.option('--label', help='Specify the label to use for the greetings.')
@click.pass_context
def labels(ctx, home, label):
    if not home or not label:
        ctx.fail('The name and label are required')
    else:
        browser = SeleniumBrowser()
        logger = ctx.obj['logger']

        try:
            browser.get(home)
            logger.info(f"Successfully accessed the URL: {home}")
        except WebDriverException as e:
            logger.error(f'Error accessing URL: {e}')
            ctx.fail('The provided URL is invalid. Please check the URL and try again.')

        
        try:
            elems = browser.find_elements(By.TAG_NAME, label)
            click.echo('Loading...')
            logger.info("Data fetched successfully")
            for e in elems:
                print(f"{e.text} - {e.get_attribute('id')} - {e.get_attribute('class')}")
            click.echo('Finished...')
        except NoSuchElementException as e:
            logger.error(f'Error accessing element on the page: {e}')
            ctx.fail('The specified element could not be found on the page. Please check the selector and try again.')


@click.command()
@click.option('--home', help='Specify the number of greetings to display.')
@click.option('--selector', help='Specify the selector to use for the greetings.')
@click.pass_context
def css(ctx, home, selector):
    if not home or not selector:
        ctx.fail('The home and selector are required')
    else:
        browser = SeleniumBrowser()
        logger = ctx.obj['logger']

        try:
            browser.get(home)
            logger.info(f"Successfully accessed the URL: {home}")
        except WebDriverException as e:
            logger.error(f'Error accessing URL: {e}')
            ctx.fail('The provided URL is invalid. Please check the URL and try again.')

        
        try:
            elems = browser.find_elements(By.CSS_SELECTOR, selector)
            click.echo('Loading...')
            logger.info("Data fetched successfully")
            for e in elems:
                print(f"{e.tag_name} - {e.text} - {e.get_attribute('id')} - {e.get_attribute('class')}")
            click.echo('Finished...')
        except NoSuchElementException as e:
            logger.error(f'Error accessing element on the page: {e}')
            ctx.fail('The specified element could not be found on the page. Please check the selector and try again.')

    
@click.command()
@click.option('--home', help='Specify the number of greetings to display.')
@click.pass_context
def screenshot(ctx, home):
    if not home:
        ctx.fail('The home are required')
    else:
        browser = SeleniumBrowser()
        logger = ctx.obj['logger']

        try:
            browser.get(home)
            logger.info(f"Successfully accessed the URL: {home}")
        except WebDriverException as e:
            logger.error(f'Error accessing URL: {e}')
            ctx.fail('The provided URL is invalid. Please check the URL and try again.')

        screenshot_folder = "src/screenshots"
        screenshot_filename = f"{uuid.uuid4()}.png"
        screenshot_path = os.path.join(screenshot_folder, screenshot_filename)
        
        try:
            click.echo('Loading...')
            logger.info("screenshot successfully")
            success = browser.save_screenshot(screenshot_path)
            if success:
                click.echo("screenshot successfully")
                click.echo('Finished...')
            else:
                raise Exception('Image could not be saved')
        except Exception as e:
            logger.error(f'Error saving the image: {e}')
            ctx.fail('The image could not be saved. Please check the file path and permissions, and try again.')

