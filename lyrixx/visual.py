from pyfiglet import Figlet
import shutil

f = Figlet(font="mono12")


def render(text, center=True):
    rendered = f.renderText(text)
    if center:
        term = shutil.get_terminal_size()
        text_lines = len(rendered.splitlines())
        padding = (term.lines - text_lines) // 2
        print("\n" * padding, end="")
        print(
            *[x.center(term.columns) for x in rendered.split("\n")],
            sep="\n",
        )
    else:
        print(rendered)
