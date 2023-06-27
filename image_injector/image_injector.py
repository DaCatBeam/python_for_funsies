import click
import sys

JPG_END = bytes([0xFF, 0xD9]) 

@click.group()
def cli():
     """CLI Entry point
     """
     pass

@cli.command()
# TODO: Figure out why this is coming back as a tuple. Examples show it as an file object. Might be doing something wrong.
@click.argument('image_file', type=click.File('rb'), nargs=-1, required=True)
@click.option('-O', '--out-file', type=click.Path(exists=False), default='injected_image.jpg', help='The input image to inject.', required=False)

def create(image_file, out_file):
     image = image_file[0]
     try:
          file_bytes = bytearray(image.read())
          end_index = file_bytes.find(JPG_END)
     except FileNotFoundError:
          sys.stderr.write(f"Could not open image file, {image_file}.")
          sys.exit(1)
