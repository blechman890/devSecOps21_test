def split_filename(filename):
    parts = filename.rsplit('.', 1)
    if len(parts) == 2:
        name, ext = parts
    else:
        name, ext = filename, ""
    return name, ext
print(split_filename("report.pdf"))