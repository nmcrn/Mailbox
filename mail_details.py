from colorama import Fore

FROM_SECTION_INDEX = 0
TO_SECTION_INDEX = 2
CC_SECTION_INDEX = 4
HEAD_SECTION_INDEX = 6
BODY_SECTION_INDEX = 8


class Mail:
    def __init__(self):
        self.mail_src = ''
        self.mail_dst = []
        self.mail_cc = []
        self.mail_header = ''
        self.mail_body = ''

    def run(self):
        user_choice = input("input selector (FILE – 1, CONSOLE – 2)")
        if user_choice == '1':
            file = input("Enter file path")
            self.read_txt(file)
        else:
            self.set_info()
        user_choice = input("Do you want to print the mail message (Y/N)")
        if user_choice in ['y', 'Y', 'yes', 'Yes']:
            self.print_info_with_color()

    def set_info(self):
        self.mail_src = input('src: ')
        self.mail_dst = input('dst: ')
        self.mail_cc = input('cc: ')
        self.mail_header = input('header: ')
        self.mail_body = input('body: ')

    def print_info(self):
        info_string = (f"from: {self.mail_src}\n"
                       f"to: {' ; '.join(self.mail_dst)}\n\n"
                       f"cc: {' ; '.join(self.mail_cc)}\n\n"
                       f"header: {self.mail_header}\n"
                       f"body: {self.mail_body}")
        print(info_string)

    def print_info_with_color(self):
        info_string = (f"{Fore.BLUE}from: {self.mail_src}\n"
                       f"{Fore.RED}to: {' ; '.join(self.mail_dst)}\n\n"
                       f"{Fore.GREEN}cc: {' ; '.join(self.mail_cc)}\n\n"
                       f"{Fore.LIGHTBLUE_EX}header: {self.mail_header}\n"
                       f"{Fore.LIGHTYELLOW_EX}body: {self.mail_body}")
        print(info_string)

    def read_txt(self, mail_file):
        with open(mail_file, 'r') as file:
            lines = file.readlines()
        self.mail_src = lines[FROM_SECTION_INDEX][5:]
        self.mail_dst = lines[TO_SECTION_INDEX][3:].split()
        self.mail_cc = lines[CC_SECTION_INDEX][3:].split()
        self.mail_header = lines[HEAD_SECTION_INDEX][7:]
        self.mail_body = lines[BODY_SECTION_INDEX][5:]
        