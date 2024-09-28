import sys
import ssl
import urllib3

from utils.core import main
from utils.helpers import print_banner, log, mrh


ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == "__main__":
    while True:
        try:
            print_banner()
            main()
        except KeyboardInterrupt:
            print()
            log(mrh + f"Successfully logged out of the bot\n")
            sys.exit()
