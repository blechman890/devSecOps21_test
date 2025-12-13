def split_name(full_name, /,*, separator=" "):
    name_parts = full_name.split(separator)
    first_name = name_parts[0]
    # last_name_parts = name_parts[1:]
    last_name = name_parts[-1] # separator.join(last_name_parts)
    print(f"\nFirst Name: {first_name}. \nLast Name: {last_name}.")
    return first_name, last_name

split_name("Ilya Blechman")
# split_name("Moshe Ben-David", separator=" ")