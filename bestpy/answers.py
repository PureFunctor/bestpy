import platform


def os() -> str:
    name = platform.system()

    # Replacing "Darwin", since it might be confusing for macOS users
    if name == "Darwin":
        name = "macOS"

    return name


answers = {
    # region: Tech
    "language": "Python",
    "programming_language": "Python",
    "pep": [
        0,
        1,
        5,
        7,
        8,
        10,
        11,
        387,
        20,
        13,
        101,
        257,
        287,
        8016,
        8000,
        8002,
        8102,
        484,
    ],
    "package": "Bestpy",
    "phone": [
        "iPhone",
        "Nokia",
        "OnePlus",
        "Huawei",
        "Samsung Galaxy",
        "BlackBerry",
        "Google Pixel",
        "Sony Experia",
    ],
    "company": [
        "Apple",
        "Samsung",
        "Nokia",
        "Google",
        "Facebook",
        "Microsoft",
        "Sony",
        "Huawei",
        "IBM",
        "Intel",
        "Adobe",
        "Cisco",
        "Dell",
        "Oracle",
        "Klurio",
        "McDonald's",
    ],
    "ide": [
        "PyCharm",
        "Thonny",
        "Spyder",
        "Atom",
        "VSCode",
        "Sublime Text",
        "Vim",
        "NeoVim",
        "Emacs",
        "Vi",
        "Nano",
        "Notepad",
        "IDLE",
        "Notepad++",
        "Elvis",
        "TextEdit",
    ],
    "package_manager": [
        "apt",
        "cabal",
        "cargo",
        "chocolatey",
        "conda",
        "nimble",
        "nix",
        "npm",
        "nuget"
        "pacman",
        "pip",
        "pkg",
        "portage",
        "rpm",
        "scoop",
        "spago",
        "winget",
        "yarn",
    ],
    "developer": [
        "Guido van Rossum",
        "Vestergurkan",
        "Gustav",
        "Dennis Ritchie",
        "Bjarne Stroustrup",
        "James Gosling",
        "Linus Torvalds",
        "Anders Hejlsberg",
        "Brian Kernighan",
        "Ken Thompson",
        "Donald Knuth",
        "Steve Wozniak",
        "Richard Stallman",
    ],
    # endregion
    # region: Education
    "subject": [
        "computer science",
        "biology",
        "maths",
        "chemistry",
        "physics",
        "social sciences",
        "natural sciences",
        "music",
        "language",
        "geography",
        "history",
        "dance",
        "design",
        "physical education",
        "religion",
        "design",
        "psychology",
        "sociology",
        "health",
        "physiology",
    ],
    "teacher_name": ["Dave", "Mary", "Frank"],
    "console": [
        "PlayStation 5",
        "Xbox Series X",
        "Xbox Series S",
        "PlayStation 4 Pro",
        "PlayStation 4 Slim",
        "PlayStation 4",
        "Nintendo Switch",
        "Xbox One X",
        "Xbox One S",
        "Xbox One",
        "Wii U",
        "Playstation 3 Super Slim",
        "PlayStation 3 Slim",
        "PlayStation 3",
        "Xbox 360",
        "Wii",
        "PlayStation 2",
        "PlayStation",
        "Xbox",
        "Gamecube",
    ],
    "grade": "A",
    "gpa": [4.0, 5.0],
    "enter": 99.9,
    "gcse": 9,
    "school": [
        "Harvard University",
        "MIT",
        "Stanford University",
        "Oxford University",
        "Yale University",
        "Chalmers",
        "KTH",
        "Princeton University",
        "University of Michigan",
        "Cornell University",
        "TU Delft",
        "UC Berkeley",
    ],
    "learning_method": ["active recall", "spaced repetition", "deep thinking"],
    # endregion
    # region: Time
    "year": range(2100),
    "month": [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ],
    "date": range(1, 32),
    "weekday": ["monday", "tuesday", "wednesday", "thursday", "friday"],
    "day": [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ],
    "time_period": [
        "stone age",
        "bronze age",
        "classical antiquity",
        "iron age",
        "renaissance",
        "industrial age",
        "atomic age",
        "space age",
        "information age",
    ],
    "week": range(1, 53),
    # endregion
    "os": os,
    "cult": "Gurkult",
}
