import bleach

def clean_text(text):
    if not text:
        return
    
    allowed_tags, allowed_attributes, allowed_styles = [],[],[]

    text = bleach.clean(
        text,
        allowed_tags,
        allowed_attributes,
        allowed_styles,
        strip=True,
        strip_comments=True,
    ).strip()

    return text