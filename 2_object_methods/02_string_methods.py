text = "  python programming  "
print(text.strip())
print(text.upper())
print(text.strip().title())
print(text.replace("python", "Java"))
print(text.split())


raw_text = "  python programming for DATA analysis  "

# Removing spaces and changing letter case
clean_text = raw_text.strip()
print("strip():", clean_text)
print("lower():", clean_text.lower())
print("upper():", clean_text.upper())
print("title():", clean_text.title())
print("capitalize():", clean_text.capitalize())
print("swapcase():", clean_text.swapcase())

# Searching and checking string content
print("find('programming'):", clean_text.find("programming"))
print("count('a'):", clean_text.lower().count("a"))
print("startswith('python'):", clean_text.lower().startswith("python"))
print("endswith('analysis'):", clean_text.lower().endswith("analysis"))
print("'DATA' is uppercase:", "DATA".isupper())

# Replacing, splitting and joining strings
updated_text = clean_text.replace("DATA", "business data")
words = updated_text.split()
joined_text = " | ".join(words)
print("replace():", updated_text)
print("split():", words)
print("join():", joined_text)

# Formatting a string
course = "Advanced Python"
participants = 24
print("format():", "{} has {} participants".format(course, participants))
print(f"f-string: {course} has {participants} participants")
