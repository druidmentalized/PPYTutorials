from colorama import Fore, Style, init

from finance_tracker_project.config.config import SUCCESS_COLOR, ERROR_COLOR, PROMPT_OPTION_COLOR, \
    POSITIVE_OPERATION_COLOR, \
    NEGATIVE_OPERATION_COLOR, BULLET_COLOR, MENU_OPTION_COLOR, HEADER_COLOR, PROMPT_INFO_COLOR, INFO_COLOR

COLOR_MAP = {
    "Positive_operation": Fore.GREEN,
    "Negative_operation": Fore.RED,
    "Success": Fore.LIGHTGREEN_EX,
    "Error": Fore.LIGHTRED_EX,
    "Info": Fore.LIGHTYELLOW_EX,
    "Menu": Fore.BLUE,
    "Bullet": Fore.YELLOW,
    "Header": Fore.LIGHTBLUE_EX,
    "Prompt_option": Fore.LIGHTBLUE_EX,
    "Prompt_info": Fore.LIGHTWHITE_EX
}

# PRINT
def print_colored(content: str, color_key: str) -> None:
    color = COLOR_MAP.get(color_key, "")
    print(f"{color}{content}{Style.RESET_ALL}")

def print_positive(content: str) -> None:
    print_colored(content, POSITIVE_OPERATION_COLOR)

def print_negative(content: str) -> None:
    print_colored(content, NEGATIVE_OPERATION_COLOR)

def print_success(content: str) -> None:
    print_colored(content, SUCCESS_COLOR)

def print_error(content: str) -> None:
    print_colored(content, ERROR_COLOR)

def print_info(content: str) -> None:
    print_colored(content, INFO_COLOR)

def print_header(content: str) -> None:
    print_colored(content, HEADER_COLOR)

def print_option(bullet: str | int, content: str) -> None:
    number_str = f"{COLOR_MAP.get(BULLET_COLOR)}{bullet}.{Style.RESET_ALL}"
    content_str = f"{COLOR_MAP.get(MENU_OPTION_COLOR)}{content}{Style.RESET_ALL}"
    print(f"{number_str} {content_str}")

# INPUT
def input_colored(prompt: str, color_key: str) -> str:
    color = COLOR_MAP.get(color_key, "")
    return input(f"{color}{prompt}{Style.RESET_ALL}")

def input_option(prompt: str) -> str:
    return input_colored(prompt, PROMPT_OPTION_COLOR)

def input_info(prompt: str) -> str:
    return input_colored(prompt, PROMPT_INFO_COLOR)