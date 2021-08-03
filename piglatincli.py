import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand
def piglatin(data):
    a = str(data)
    a = a.lower()
    a = a + a[0]+'ay'
    a = list(a)
    a.remove(a[0])

    a = ''.join(a)
    print(a)
def english(data):
    a = data.lower()
    for i in range(1, 3):
        a = a[:-1]

    a =  a[len(a)-1]+a[0:len(a)-1]
    print(a)
@click.group(
    cls=HelpColorsGroup, help_headers_color="yellow", help_options_color="cyan"
)
@click.version_option('0.1.0')
def main():
    """PigLatinCli: Convert English To Pig Latin\n
    iglatinclipay: onvertcay nglisheay otay igpay atinlay"""
    pass
@main.command('en2pig', help = 'English To Piglatin')
@click.argument('content', nargs=-1)
def en2pl(content):
    llist = []
    content = list(content)
    for x in range(len(content)):
        a = str(content[x])
        a = a.lower()
        a = a + a[0]+'ay'
        a = list(a)
        a.remove(a[0])

        a = ''.join(a)
        llist.append(a)
        text = ' '.join(llist)
    print(text)
    
 
    
            
@main.command('pl2en', help = 'Piglatin To English')
@click.argument('content', nargs=-1)
def pl2en(content):
    llist = []
    content = list(content)
    for x in range(len(content)):
        data = content[x]
        a = data.lower()
        for i in range(1, 3):
            a = a[:-1]

        a =  a[len(a)-1]+a[0:len(a)-1]
        llist.append(a)
    text = ' '.join(llist)
    print(text)
    

        


if __name__ == '__main__':
    main()