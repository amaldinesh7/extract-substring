import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    content = os.environ["INPUT_CONTENT"]
    delimiterOne = os.environ["INPUT_DELIMITERONE"]
    delimiterTwo = os.environ["INPUT_DELIMITERTWO"]

    output = content.partition(delimiterOne)[2].partition(delimiterTwo)[0].strip().replace('\n', '%0A')

    print(f"""::set-output name=match::'{output}'""")
    os.system(f'echo "::set-output name=changelog_content::{output}"')


if __name__ == "__main__":
    main()
