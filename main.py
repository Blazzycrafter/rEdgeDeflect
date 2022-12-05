import sys, webbrowser, ctypes, os, json

with open('settings.json', 'r') as f:
    settings = json.load(f)

Alias_Commands = settings['Alias_Commands']
CL = settings['CL'] #CatchList
UCL = settings['UCL'] #UnCatchList
icof = settings['icof'] #InstaCloceOnFound (GitHub issue #1)
DEBUG = settings['Debug']

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
ex_args=sys.argv.copy()
mypath=ex_args[0]

if not '\\' in mypath:
    mypath = os.path.abspath(os.curdir)+'\\'+mypath
    x=''

ex_args.remove(ex_args[0])

print(f'Extern arguments: {ex_args}')

for ex_arg in ex_args:
    for icofi in icof:
        if ex_arg.lower() == icofi.lower():
            exit()

def dprint(string: str) -> print:
    '''Only prints if DEBUG is true.

    Args:
        string (str): String to print.

    Returns:
        print: Prints the string.
    '''
    if DEBUG: 
        print(string)

def browser(url: str) -> webbrowser.open:
    '''Opens the URL in your default browser.

    Args:
        url (str): URL to open

    Returns:
        webbrowser.open: Opens the URL.
    '''
    for CLI in CL:
        if url.startswith(CLI):
            dprint(f'Before prefix removal: {url}')
            url = url.removeprefix(CLI)
            dprint(f'After prefix removal: {url}')
    webbrowser.open(url, 2)

if len(ex_args) < 1:
    ctypes.windll.user32.MessageBoxW(0, f'''
rEdgeDeflect is a tool to replace forced browsers like Microsoft Edge.


Technical Information:
If the first parameter is --single-argument your default browser will be opened with the url behind --single-argument
If not, a terminal will open and ask you what to do.


BrowserFunction:
If a link starts with one of these ({UCL}), your default browser will be opened with the url.
If the searchbar argument is on of these ({CL}), it will be replaced and yourdefault browser will be opened with the url.

Still in development!
''', 'rEdgeDeflect Information', 0)
    exit(-1)
else:
    pass

def EdgeReplace():
    '''Makes an backup of edge.'''
    os.chdir(r'C:\Program Files (x86)\Microsoft\Edge\Application')
    dirlist = os.listdir()
    dprint(dirlist)
    if 'msedge.exe.bak' in dirlist:
        print('msedge backup found...')
        print('Replace? Y/n')
        if input('>>').lower() == 'y':
            os.remove('msedge.exe.bak')
            open('msedge.exe.bak', 'wb').write(open('msedge.exe', 'rb').read())
    else:
        os.rename('msedge.exe', 'msedge.exe.bak')
    open('msedge.exe','wb').write(open(mypath,'rb').read())

def callcmd():
    '''Opens the EdgeDeflect console.'''
    print('EdgeDeflect Console')
    cmd=input('>>')
    if cmd.lower() == 'ReplaceOnce'.lower():
        EdgeReplace()

if __name__ == '__main__':
    if ex_args[0] == '--single-argument':
        browser(ex_args[1])
        exit()
    elif ex_args[0].lower() in Alias_Commands:
        callcmd()
        exit()
    else:
        print('Can\'t reconize this.')
        print('What to do?')
        print('(0) Exit')
        print('(1) Run all')
        print('(2) Run single')
        cmd= input('>>')
        if cmd == '1':
            if len(ex_args) >= 1:
                for ex_arg in ex_args:
                    browser(ex_arg)
        elif cmd == '2':
            print('Which one?')
            for ex_arg_index in range(len(ex_args)):
                print(f'({ex_arg_index}) => {ex_args[ex_arg_index]}')
            while True:
                n=input('n>')
                try:
                    browser(ex_args[int(n)])
                    exit()
                except IndexError:
                    print('Not in range.')
        elif cmd == '0':
            exit(-1)
