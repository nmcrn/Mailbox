from mail_details import get_info, print_info,print_info_with_color


def start_mail():
    mail_info = get_info()
    user_choice = input("Do you want to print the mail message (Y/N)")
    if user_choice in ['y', 'Y', 'yes', 'Yes']:
        print_info_with_color(mail_info)


def main():
    start_mail()


if __name__ == '__main__':
    main()
