config.load_autoconfig()

# Set Default Search Engine
c.url.searchengines = {
	'DEFAULT': 'https://search.brave.com/search?q={}',
	'yt': 'https://www.youtube.com/results?search_query={}',
	'sp': 'https://www.startpage.com/do/search?q={}',
	'al': 'https://www.almaany.com/ar/dict/ar-ar/{}',
	'en': 'https://www.almaany.com/ar/dict/ar-en/{}',
	'jp': 'https://shinjikai.app/search?term={}',
	'r': 'https://www.reddit.com/search/?q={}',
	'gh': 'https://www.github.com/search?q={}'
    'gl': 'https://gitlab.com/search?search={}',
    'ask': 'https://search.brave.com/ask?q={}',
    'fh': 'https://flathub.org/apps/search?q={}',
    'i': 'https://icons8.jp/icons/set/{}',
    'km': 'https://keyman.com/keyboards?q={}',
    't': 'https://trakt.tv/search?query={}',
    'y': 'https://search.yahoo.co.jp/search?p={}',
    'ae': 'https://www.arabeyes.org/index.php?title=%D8%AE%D8%A7%D8%B5:%D8%A8%D8%AD%D8%AB&search={}',
    'l': 'https://lemmy.world/search?q={}',
    'm': 'https://mastodon.social/deck/search?q={}',
    'bs': 'https://bsky.app/search?q={}'
}

# Show Search Suggestions as you type
c.completion.quick = True

# How many Search Suggestions to show
c.completion.height = '50%'

# Show web history in fulfillments
c.completion.web_history.max_items = 1000

# Set Opening Page
c.url.start_pages = ['https://www.yahoo.co.jp']

# Set New Tab Page
c.url.default_page = 'https://www.yahoo.co.jp'

#Adblock lists
c.content.blocking.enabled = True
c.content.blocking.method = 'both'
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt"
]

#Fonts
c.fonts.default_family = 'Jua, "Kosugi Maru", Amiri, Solitreo, "Tengwar Telcontar"'
c.fonts.web.family.standard = "Tengwar Telcontar"
c.fonts.web.family.serif = "Amiri"
c.fonts.web.family.sans_serif = "Harmattan"
c.fonts.web.family.fixed = "NoName Fixed"

#Display Language
c.content.headers.accept_language = 'ar,ja;q=0.9'

# Type: UniqueCharString
c.hints.chars = 'aoeuidhtnspkgmyxfb'
