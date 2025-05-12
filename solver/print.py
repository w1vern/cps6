

def md_print(md_text: str) -> None:
    with open("test.md", 'w') as file:
        file.write(md_text)