def spider_0():
    """Stage 0 — empty web, no wrong guesses yet."""
    return (
        "   |\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "___|___"
    )


def spider_1():
    """Stage 1 — silk drops from the web."""
    return (
        "   |\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "   .\n"
        "___|___"
    )


def spider_2():
    """Stage 2 — head appears."""
    return (
        "   |\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "   o\n"
        "___|___"
    )


def spider_3():
    """Stage 3 — body grows."""
    return (
        "   |\n"
        "   |\n"
        "   |\n"
        "   o\n"
        "  ( )\n"
        "___|___"
    )


def spider_4():
    """Stage 4 — two legs sprout."""
    return (
        "   |\n"
        "   |\n"
        "   |\n"
        "   o\n"
        " /( )\\\n"
        "___|___"
    )


def spider_5():
    """Stage 5 — four legs."""
    return (
        "   |\n"
        "   |\n"
        "   |\n"
        "   o\n"
        "//( )\\\\\n"
        "___|___"
    )


def spider_6():
    """Stage 6 — full spider with all eight legs."""
    return (
        "   |\n"
        "   |\n"
        "   |\n"
        "  /o\\\n"
        "//( )\\\\\n"
        "//_|_\\\\"
    )


def spider_7():
    """Stage 7 — the spider starts spreading its web."""
    return (
        "\\  |  /\n"
        " \\ | / \n"
        "  \\|/  \n"
        "  /o\\  \n"
        "//( )\\\\\n"
        "//_|_\\\\"
    )


def spider_8():
    """Stage 8 — the web is complete. Game over."""
    return (
        "\\--|--/\n"
        " \\ | / \n"
        "--\\|/--\n"
        "  /o\\  \n"
        "//( )\\\\\n"
        "//_|_\\\\"
    )
