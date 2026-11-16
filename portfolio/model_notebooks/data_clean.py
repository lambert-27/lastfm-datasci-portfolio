# Mark Lambert - C00192497

# track & album are cleaned names so the same track matches across both datasets when merging
def clean_text(s):
    # removes anything in brackets () [] plus whitespace
    s = s.str.replace(r'\s*[\(\[].*?[\)\]]', '', regex=True) 
    # remove from first - and onwards (Song - Remastered) 
    s = s.str.replace(r'\s*-.*$', '', regex=True)
    # remove other punctuation
    s = s.str.replace(r'[^\w\s]', '', regex=True)
    # remove other whitespaces that repeat and trim
    return s.str.replace(r'\s+', ' ', regex=True).str.strip()

# artist names are cleaned so the same artist matches across both datasets when merging
def clean_artist(s):
    # lowercase and remove & for artists that have features
    s = s.str.lower().str.split('/').str[0].str.split('&').str[0]
    # remove punctuation, repeateed whitespace and trim
    return s.str.replace(r'[^\w\s]', '', regex=True).str.replace(r'\s+', ' ', regex=True).str.strip()