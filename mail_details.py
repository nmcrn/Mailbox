from typing import Dict
from colorama import Fore


def get_info() -> Dict[str,str]:
    mail_src = input('src: ')
    mail_dst = input('dst: ')
    mail_cc = input('cc: ')
    mail_header = input('header: ')
    mail_body = input('body: ')

    return {
        'mail_src': mail_src,
        'mail_dst': mail_dst,
        'mail_cc': mail_cc,
        'mail_header': mail_header,
        'mail_body': mail_body
    }


def print_info(info: Dict[str, str]):
    info_string = (f"from: {info['mail_src']}\n"
                   f"to: {info['mail_dst']}\n"
                   f"cc: {info['mail_cc']}\n"
                   f"header: {info['mail_header']}\n"
                   f"body: {info['mail_body']}")
    print(info_string)


def print_info_with_color(info: Dict[str, str]):
    info_string = (f"{Fore.BLUE}from: {info['mail_src']}\n"
                   f"{Fore.RED}to: {info['mail_dst']}\n"
                   f"{Fore.GREEN}cc: {info['mail_cc']}\n"
                   f"{Fore.LIGHTBLUE_EX}header: {info['mail_header']}\n"
                   f"{Fore.LIGHTYELLOW_EX}body: {info['mail_body']}")
    print(info_string)
