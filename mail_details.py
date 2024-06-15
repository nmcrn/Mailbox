from colorama import Fore


class Mail:
    def __init__(self):
        self.mail_src = ''
        self.mail_dst = ''
        self.mail_cc = ''
        self.mail_header = ''
        self.mail_body = ''

    def run(self):
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
                       f"to: {self.mail_dst}\n"
                       f"cc: {self.mail_cc}\n"
                       f"header: {self.mail_header}\n"
                       f"body: {self.mail_body}")
        print(info_string)

    def print_info_with_color(self):
        info_string = (f"{Fore.BLUE}from: {self.mail_src}\n"
                       f"{Fore.RED}to: {self.mail_dst}\n"
                       f"{Fore.GREEN}cc: {self.mail_cc}\n"
                       f"{Fore.LIGHTBLUE_EX}header: {self.mail_header}\n"
                       f"{Fore.LIGHTYELLOW_EX}body: {self.mail_body}")
        print(info_string)
