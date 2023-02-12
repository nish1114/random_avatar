from multiavatar.multiavatar import multiavatar
from uuid import uuid4
from cairosvg import svg2png
import string
import secrets
import pyfiglet
import argparse
import os

def create_random_avatar():
    source = string.ascii_letters + string.digits
    random_string = ''.join((secrets.choice(source) for i in range(52)))
    svgCode = multiavatar(random_string, None, None)
    return svgCode

def svg_code_to_png(svg_code,n):
    MYDIR = ("media")
    CHECK_FOLDER = os.path.isdir(MYDIR)

    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
    svg2png(bytestring=svg_code,write_to='media/{}.png'.format(n))

def create_avatar(number_of_avatars=1):
    for i in range(number_of_avatars):
        svg_code = create_random_avatar()
        svg_code_to_png(svg_code=svg_code,n=i)

def main():
    ascii_banner = pyfiglet.figlet_format("CREATE N NUMBER OF AVATARS")
    print(ascii_banner)
    parse_results = parse_command_line()
    if bool(parse_results):
        number_of_avatar=parse_results
    else:
        number_of_avatars_banner = pyfiglet.figlet_format("ENTER NUMBER OF AVATARS TO CREATE:\n")
        print(number_of_avatars_banner)
        number_of_avatar = None
        while number_of_avatar==None:
            try:
                number_of_avatar = int(input())
            except ValueError as e:
                error_banner = pyfiglet.figlet_format("KINDLY ENTER NUMBER:\n")
                print(error_banner)
                number_of_avatar = None
    create_avatar(number_of_avatar)

def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="Creates n avatars",default=0)
    args = parser.parse_args()
    return args.n


main()
