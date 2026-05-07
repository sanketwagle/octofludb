import parsec as p
import re


def clean_host(x):
    x = re.sub(";.*", "", x.strip().lower())
    if "scrofa" in x:
        x = "swine"
    elif "pig" in x and "pigeon" not in x:
        x = "swine"
    elif "porcine" in x:
        x = "swine"
    elif "boar" in x:
        x = "swine"
    elif "sapiens" in x:
        x = "human"
    # cannot contain digits
    x = re.findall("^[^0-9]+$|$", x)[0]
    x = None if x == "" else x
    return x


p_host = clean_host #p.regex(re.compile("swine|human", re.IGNORECASE))
