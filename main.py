import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    content = os.environ["content"]
    delimiterOne = os.environ["delimiterOne"]
    delimiterTwo = os.environ["delimiterTwo"]

    output = content.partition(delimiterOne)[2].partition(delimiterTwo)[0].strip()

    my_output = f"{output}"

    print(f"::set-output name=match::{my_output}")


if __name__ == "__main__":
    main()
