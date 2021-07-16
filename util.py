from pathlib import Path
import time
import json


def get_words_and_prefixes(listname):
    # return get_words(listname), get_prefixes(listname)
    # TODO: Find out why this^^ takes longer than the lines below
    words = get_words(listname)
    return words, get_prefixes_from_words(words)


def get_wordlist_filename(listname):
    return f"{listname}.txt"


def get_words(listname):
    with open(get_wordlist_filename(listname)) as f:
        return set(line.strip() for line in f)


def get_prefix_filename(listname):
    return f"{listname}-prefixes.json"


def get_prefixes(listname):
    prefix_file = Path(get_prefix_filename(listname))
    if prefix_file.is_file():
        with open(prefix_file) as fp:
            return json.load(fp)
    else:
        return create_prefixes(listname)


def get_prefixes_from_words(words):
    start = time.time()
    prefixes = set()
    for word in words:
        word_so_far = ""
        for char in word[:-1]:
            word_so_far += char
            prefixes.add(word_so_far)
    end = time.time()
    print(
        f"Prefix creation took {end -start} seconds.\nThere are {len(prefixes)} prefixes."
    )
    return prefixes


def create_prefixes(listname):
    start = time.time()
    prefixes = set()
    for word in get_words(listname):
        word_so_far = ""
        for char in word[:-1]:
            word_so_far += char
            prefixes.add(word_so_far)
    end = time.time()
    print(
        f"Prefix creation took {end -start} seconds.\nThere are {len(prefixes)} prefixes."
    )
    with open(get_prefix_filename(listname), "w") as f:
        json.dump(sorted(list(prefixes)), f, indent=2)
    return prefixes


def get_board_input(human_input):
    human_input = human_input.upper()
    has_q = "Q" in human_input
    rows = human_input.split()
    grid = [list(row) for row in rows]
    if not has_q:
        return grid
    return [["Qu" if char == "Q" else char for char in row] for row in grid]
