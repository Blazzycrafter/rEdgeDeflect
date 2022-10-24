#!/usr/bin/python

import sys, webbrowser , ctypes


print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
ex_args=sys.argv.copy()
ex_args.remove(ex_args[0])

print(f"extern args: {ex_args}")


CL = ["microsoft-edge:"] #CatchList
UCL = ["http://", "https://"] #UnCatchList
DEBUG = False

def dprint(string):
    if DEBUG:
        print(string)

def catch(url:str):
    for i in UCL:
        if url.startswith(i):
            return url
    for i in CL:
        if url.startswith(i):
            dprint(f"before removed prefix: {url}")
            url = url.removeprefix(i)
            dprint(f"after removed prefix: {url}")
            return url

def browser(url:str): # Override
    webbrowser.open(catch(url))


def runall(ex_args):
    if len(ex_args) >= 1:
        for i in ex_args:
            browser(f"{i}")
    else:
        pass


def runsingle(ex_args):
    print("wich one?")
    for i in range(len(ex_args)):
        print(f"({i}) => {ex_args[i]}")
    while True:
        n=input("n>")
        try:
            browser(f"{ex_args[int(n)]}")
            exit()
        except IndexError:
            print("not in range...")

if len(ex_args) < 1:
    ctypes.windll.user32.MessageBoxW(0, f"""rEdgeDeflect
is a tool to replace forced browsers... like EDGE...


Technical Information:
if the first parameter is --single-argument
we starts the browser function...

else we ask you what you want to do...


BrowserFunction
if a link starts with one of these:
{UCL}

we relay it directly to the browser


else if we fount one of these:
{CL}

we remove it and then relay the url to your browser...


and the browser is your default browser
""", "rEdgeDeflect Information", 0)
    exit(-1)
else:
    pass
if ex_args[0] == "--single-argument":
    browser(f"{ex_args[1]}")
    exit()
else:
    print("can reconize this...")
    print("What to do?")
    print("(0) drop it an close")
    print("(1) run all")
    print("(2) run 1")
    cmd= input(">>")
    if cmd == "1":
        runall(ex_args)
    elif cmd == "2":
        runsingle(ex_args)
    elif cmd == "0":
        exit(-1)