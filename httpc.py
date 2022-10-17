import argparse

# httpc (get|post) [-v] (-h "k:v")* [-d inline-data] [-f file] URL
parser = argparse.ArgumentParser(add_help=False)

subparser = parser.add_subparsers()
parser_list = subparser.add_parser('help')
parser_list.add_argument('help_type', nargs='?', default='help', choices=['help','get','post'])

parser.add_argument('command', nargs='?' , type=str, choices=['get', 'post'])
parser.add_argument('-v', dest='verbose', action='store_true')
parser.add_argument('-d', dest='data', type=str)
parser.add_argument('-f', dest='file', type=str)
parser.add_argument('-url', dest='url', type=str)
args = parser.parse_args()
print(vars(args))

if args.help_type == 'help':
    print('\nhttpc is a curl-like application but supports HTTP protocol only.\nUsage:\n\thttpc.py command ' \
        '[arguments]\nThe commands are:\n\tget\texecutes a HTTP GET request and prints the response.\n\tpost\t' \
        'executes a HTTP POST request and prints the response.\n\thelp\tprints this screen.\n\n' \
        'Use "httpc help [command]" for more information about a command.\n')
elif args.help_type == 'get':
    print('\nusage: httpc get [-v] [-h key:value] URL\n\nGet executes a HTTP GET request for a given URL.\n\t-v' \
        '\t\tPrints the detail of the response such as protocol, status, and headers.\n\t-h key:value\t' \
        'Associates headers to HTTP Request with the format "key:value".\n')
elif args.help_type == 'post':
    print('\nusage: httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL\n\nPost executes a HTTP ' \
        'POST request for a given URL with inline data or from file.\n\t-v\t\tPrints the detail of the ' \
        'response such as protocol, status, and headers.\n\t-h key:value\tAssociates headers to HTTP Request ' \
        'with the format "key:value".\n\t-d string\tAssociates an inline data to the body HTTP POST request.' \
        '\n\t-f file\t\tAssociates the content of a file to the body HTTP POST request.\n\nEither [-d] or [-f] ' \
        'can be used but not both.')
