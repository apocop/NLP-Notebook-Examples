import gettext

gettext.install('greeting')

def greet():
    age = 25
    print(_('Hi'))
    print(_("What's up?"))
    print(_('I am %s years old!') % (age))
    print('\n')

def select_language(language):
    lang = gettext.translation('greeting', localedir='locale', languages=[language], fallback=True)
    lang.install()


# Default language 'English'.
greet()

# Change language to Spanish.
select_language('es')
greet()

# Change language to English.
select_language('en')
greet()

# Change language to Hebrew.
select_language('he')
greet()


# 1. Mark strings as translatable.
#  python C:\Users\Joel\Anaconda3\Tools\i18n\pygettext.py -d greeting greeting.py
#  python C:\Users\Joel\Anaconda3\Tools\i18n\msgfmt.py greeting