import datetime
import pathlib

REPO_DIR = pathlib.Path(__file__).parent.resolve()

QUESTIONS = {
    "NAME": "Your first/last name",
    "EMAIL": "Your email address",
    "PROJECT": "The name of the project",
}


def replace_in_file_names(qanda: dict[str, str]):
    for path in REPO_DIR.glob("**/*"):
        if ".git" not in path.parts:
            if path.is_file() or path.is_dir():
                for q, a in qanda.items():
                    path.rename(path.with_name(path.name.replace(q, a)))


def replace_in_files(qanda: dict[str, str]):
    for path in REPO_DIR.glob("**/*"):
        if ".git" not in path.parts:
            if path.is_file():
                text = path.read_text()
                for q, a in qanda.items():
                    text = text.replace(q, a)
                path.write_text(text)


if __name__ == "__main__":
    qanda = {"YEAR": str(datetime.datetime.now().year)}
    for key, question in QUESTIONS.items():
        value = input(question + ": ")
        qanda[key] = value.strip()

    replace_in_file_names(qanda)
    replace_in_files(qanda)

    print("Done!")