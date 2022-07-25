import typer

# generate a CLI from function definitions
# based on https://typer.tiangolo.com/

app = typer.Typer()

# python cli_typer.py hello --help
# python cli_typer.py hello  Clemens
@app.command()
def hello(name:str):
    print(f"Hello {name}")


# python cli_typer.py func --help
# python cli_typer.py func 45 -> 45
# python cli_typer.py func --no-p 45
# python cli_typer.py func --p 45 -> 46
@app.command()
def func(x:int, p:bool = False):
    if p:
        print(f"p = true, result -> {x+1}")
    else:
        print(f"p = false, result -> {x}")

# python cli_typer.py func2 --help
# python cli_typer.py func2 1 3 -> 4
@app.command()
def func2(x:int, y:int):
    res = x+y
    print(f"x+y={res}")

        

if __name__ == "__main__":
    app()
