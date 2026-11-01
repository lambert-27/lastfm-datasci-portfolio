def clean_text(s):
    s = s.str.replace(r'\s*[\(\[].*?[\)\]]', '', regex=True) 
    s = s.str.replace(r'\s*-.*$', '', regex=True)
    s = s.str.replace(r'[^\w\s]', '', regex=True)
    return s.str.replace(r'\s+', ' ', regex=True).str.strip()

def clean_artist(s):
    s = s.str.lower().str.split('/').str[0].str.split('&').str[0]
    return s.str.replace(r'[^\w\s]', '', regex=True).str.replace(r'\s+', ' ', regex=True).str.strip()