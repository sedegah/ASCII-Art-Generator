import argparse
from ascii_generator.convert import image_to_ascii
from termcolor import colored

def main():
    parser = argparse.ArgumentParser(description='Convert image to ASCII art.')
    parser.add_argument('image', help='Path to input image')
    parser.add_argument('--width', type=int, default=100, help='Output ASCII width')
    parser.add_argument('--charset', default='dense', choices=['dense', 'sparse', 'binary'], help='Charset type')
    parser.add_argument('--color', action='store_true', help='Enable colored ASCII output')

    args = parser.parse_args()

    ascii_art = image_to_ascii(args.image, width=args.width, charset_name=args.charset)

    if args.color:
        for line in ascii_art.splitlines():
            print(colored(line, 'cyan'))
    else:
        print(ascii_art)

if __name__ == '__main__':
    main()
