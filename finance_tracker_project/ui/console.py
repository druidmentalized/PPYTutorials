from colorama import Fore, Style, init

from finance_tracker_project.config.config import SUCCESS_COLOR, ERROR_COLOR, INFO_COLOR, POSITIVE_OPERATION_COLOR, \
    NEGATIVE_OPERATION_COLOR

COLOR_MAP = {
    "Positive_operation": Fore.GREEN,
    "Negative_operation": Fore.RED,
    "Success": Fore.LIGHTGREEN_EX,
    "Error": Fore.LIGHTRED_EX,
    "Info": Fore.LIGHTCYAN_EX
}

def print_colored(text: str, color_key: str):
    color = COLOR_MAP.get(color_key, "")
    print(f"{color}{text}{Style.RESET_ALL}")

def print_positive(text: str):
    print_colored(text, POSITIVE_OPERATION_COLOR)

def print_negative(text: str):
    print_colored(text, NEGATIVE_OPERATION_COLOR)

def print_success(text: str):
    print_colored(text, SUCCESS_COLOR)

def print_error(text: str):
    print_colored(text, ERROR_COLOR)

def print_info(text: str):
    print_colored(text, INFO_COLOR)