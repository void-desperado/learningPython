def formattedName(first,last,middle=None):
    if middle==None:
        return f"{first.title()} {last.title()}"
    else:
        return f"{first.title()} {middle.title()} {last.title()}"