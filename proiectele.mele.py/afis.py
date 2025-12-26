import time
from rich.console import Console 

console = Console()

def print_line_slowly(text, duration=1.0):
    total_chars = len(text)
    delay = duration / total_chars 
    for char in text:
        console.print(f"[bold magenta]{char}[/bold magenta]", end="")
        time.sleep(delay)
    console.print()
    time.sleep(0.2)

def printlyrics():
    lines = [
        ("Magnificat in secula", 2.2),
        ("Happy nation", 2.8), 
        ("Living in a happy nation", 1.5),
        ("Where the people understand", 3.1),
        ("And dream of perfect man", 2.0)
    ]

    for line, duration in lines:
        print_line_slowly(line, duration=duration)

if __name__ == "__main__":
    printlyrics()