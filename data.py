import os
import sys
class BColours:
    "Terminal colors, printing, and checking for color support"
    @staticmethod
    def supports_color():
        """
        Returns True if the running system's terminal supports color, and False
        otherwise.
        """
        plat = sys.platform
        supported_platform = plat != 'Pocket PC' and (
            plat != 'win32' or 'ANSICON' in os.environ)
        # isatty is not always implemented
        is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
        return supported_platform and is_a_tty
    #if color is supported, use it, otherwise, use nothing
    HEADER = '\033[95m' if supports_color() else ""
    OKBLUE = '\033[94m' if supports_color() else ""
    OKCYAN = '\033[96m' if supports_color() else ""
    OKGREEN = '\033[92m' if supports_color() else ""
    WARNING = '\033[93m' if supports_color() else ""
    FAIL = '\033[91m' if supports_color() else ""
    ENDC = '\033[0m' if supports_color() else ""
    BOLD = '\033[1m' if supports_color() else ""
    UNDERLINE = '\033[4m' if supports_color() else ""

    @classmethod
    def pretty_print(cls, text: str, color: str) -> None:
        print(color + str(text) + cls.ENDC)

    @classmethod
    def prettify(cls, text: str, color: str) -> str:
        "Returns a string with the color specified"
        return color + str(text) + cls.ENDC


categories = [
    {"id": 9, "name": "General Knowledge"},
    {"id": 10, "name": "Entertainment: Books"},
    {"id": 11, "name": "Entertainment: Film"},
    {"id": 12, "name": "Entertainment: Music"},
    {"id": 13, "name": "Entertainment: Musicals & Theatres"},
    {"id": 14, "name": "Entertainment: Television"},
    {"id": 15, "name": "Entertainment: Video Games"},
    {"id": 16, "name": "Entertainment: Board Games"},
    {"id": 17, "name": "Science & Nature"},
    {"id": 18, "name": "Science: Computers"},
    {"id": 19, "name": "Science: Mathematics"},
    {"id": 20, "name": "Mythology"},
    {"id": 21, "name": "Sports"},
    {"id": 22, "name": "Geography"},
    {"id": 23, "name": "History"},
    {"id": 24, "name": "Politics"},
    {"id": 25, "name": "Art"},
    {"id": 26, "name": "Celebrities"},
    {"id": 27, "name": "Animals"},
    {"id": 28, "name": "Vehicles"},
    {"id": 29, "name": "Entertainment: Comics"},
    {"id": 30, "name": "Science: Gadgets"},
    {"id": 31, "name": "Entertainment: Japanese Anime & Manga"},
    {"id": 32, "name": "Entertainment: Cartoon & Animations"}]
