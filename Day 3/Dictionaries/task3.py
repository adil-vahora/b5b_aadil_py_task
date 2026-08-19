library = {
    "B101": {
        "title": "Python Basics",
        "author": "John Smith",
        "copies": 3
    },
    "B102": {
        "title": "Data Science",
        "author": "Alice Brown",
        "copies": 5
    },
    "B103": {
        "title": "Machine Learning",
        "author": "David Lee",
        "copies": 2
    }
}

# Issue book B101
if library["B101"]["copies"] > 0:
    library["B101"]["copies"] -= 1

print(library)