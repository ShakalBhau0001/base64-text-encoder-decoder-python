import base64 as bs

from rich import box
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.rule import Rule
from rich.table import Table
from rich.text import Text

console = Console()


def print_banner():
    console.clear()
    banner = Text()
    banner.append("██████████  ████████  ██      ██  ██████████\n",style="bold cyan",)
    banner.append("    ██      ██          ██  ██        ██\n",style="bold cyan",)
    banner.append("    ██      ██████        ██          ██\n",style="bold blue",)
    banner.append("    ██      ██          ██  ██        ██\n",style="bold blue",)
    banner.append("    ██      ████████  ██      ██      ██\n\n",style="bold magenta",)
    banner.append(" Base64 • Text Encoder • Text Decoder ",style="dim white",)
    console.print(
        Panel(
            Align.center(banner),
            border_style="cyan",
            box=box.DOUBLE_EDGE,
        )
    )


def divider(title=""):
    console.print(
        Rule(
            title,
            style="cyan",
        )
    )


def success(message):
    console.print(f"\n[bold green]✔[/bold green] {message}\n")


def error(message):
    console.print(f"\n[bold red]✘[/bold red] {message}\n")


def info(message):
    console.print(f"[bold yellow]ℹ[/bold yellow] {message}")


def encode_text(text):
    encoded = bs.b64encode(text.encode("utf-8"))
    return encoded.decode("utf-8")


def decode_text(encoded_text):
    decoded = bs.b64decode(encoded_text,validate=True)
    return decoded.decode("utf-8")


def menu():
    table = Table(
        title="Main Menu",
        title_style="bold cyan",
        box=box.DOUBLE_EDGE,
        border_style="cyan",
        padding=(0, 2),
    )
    table.add_column(
        "Option",
        justify="center",
        style="bold yellow",
    )
    table.add_column("Action",style="green",)
    table.add_row("1","🔒 Encode Text",)
    table.add_row("2","🔓 Decode Text",)
    table.add_row("3","ℹ About",)
    table.add_row("0","🚪 Exit",)
    console.print(table)


def encode_menu():
    divider("🔒 Encode Text")
    text = Prompt.ask("[bold cyan]Enter text[/bold cyan]")
    try:
        result = encode_text(text)
        console.print(
            Panel(
                result,
                title="Encoded Base64",
                border_style="green",
                box=box.ROUNDED,
            )
        )
    except Exception as e:  # noqa: BLE001
        error(str(e))


def decode_menu():
    divider("🔓 Decode Text")
    encoded_text = Prompt.ask("[bold cyan]Enter Base64 text[/bold cyan]")
    try:
        result = decode_text(encoded_text)
        console.print(
            Panel(
                result,
                title="Decoded Text",
                border_style="green",
                box=box.ROUNDED,
            )
        )
    except Exception:  # noqa: BLE001
        error("Invalid Base64 input.")


def about():
    divider("ℹ About Toolkit")
    table = Table(
        show_header=True,
        header_style="bold cyan",
        box=box.ROUNDED,
        border_style="cyan",
    )
    table.add_column("Property",style="yellow",)
    table.add_column("Value",style="green",)
    table.add_row("Purpose","Base64 Text Encoding & Decoding",)
    table.add_row("Encoding","Base64",)
    table.add_row("Character Encoding","UTF-8",)
    table.add_row("Encode Method","Base64",)
    table.add_row("Decode Validation","Strict",)
    table.add_row("Language","Python",)
    table.add_row("UI","Rich CLI",)
    console.print(table)


def main():
    while True:
        print_banner()
        menu()
        choice = Prompt.ask(
            "\n[bold cyan]Select Option[/bold cyan]",
            choices=["1", "2", "3", "0"],
            default="1",
        )
        if choice == "1":
            encode_menu()
        elif choice == "2":
            decode_menu()
        elif choice == "3":
            about()
        elif choice == "0":
            console.print()
            console.print(
                Panel(
                    Align.center(
                        Text(
                            "See You Soon! | Stay safe, stay secure. 🕵️",
                            style="bold cyan",
                        )
                    ),
                    border_style="magenta",
                    box=box.DOUBLE_EDGE,
                )
            )
            break
        Prompt.ask(
            "\n[dim]Press Enter to return to menu…[/dim]",
            default="",
        )


if __name__ == "__main__":
    main()
