import click

@click.group()
def cli():
     """CLI Entry point
     """
     pass

@cli.command()
@click.argument('image_file', type=click.File(lazy=True), nargs=-1, required=True)
@click.option(
     '-O',
     '--out-file',
     type=click.Path(exists=False),
     default='injected_image.jpg',
     help='The input image to inject.'
)
def create(image_file, out_file):
     pass
