from fixtures.pages.main_page import auth, quit_browser, get_list_os


def get_os():
    """
    1. Auth on the page
    2. Proceed to a page with available OS
    3. Get the name of each OS
    4. Show them on the terminal
    """
    auth()
    os = get_list_os()
    quit_browser()
    if not os:
        print("There aren't available OS for download or the CAPTCHA was not passed")
    else:
        print(os)


get_os()
