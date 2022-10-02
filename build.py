import os
import sys
from turtle import pos

post_path = "posts"
template_path = "templates"


class Post:
    def __init__(self, title, time, path):
        self.title = title
        self.time = time
        self.path = path

    def __str__(self):
        return f"{self.title} {self.time} {self.path}"


def get_posts():
    """
    Get all files under /posts
    Sort them by date
    """
    posts = []
    for root, dirs, files in os.walk(post_path):
        for file in files:
            curr_title = get_title(f"{root}/{file}")
            curr_time = get_created_time(f"{root}/{file}")

            posts.append(Post(title=curr_title,
                              time=curr_time,
                              path=f"{root}/{file}"))

    posts.sort(key=lambda x: x.time, reverse=True)

    # posts = os.chdir(post_path)
    # posts.sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)

    return posts


def get_created_time(file):
    """
    Get the created time of a post
    """
    return os.path.getmtime(file)


def get_title(file):
    """
    Get the title of a post
    """
    with open(file, "r") as f:
        title = f.readline().strip("#").strip()
        if title == "":
            title = "No Title"
        return title


def append_posts():
    posts = get_posts()
    with open(f"{template_path}/home.md", "r") as template:
        template = template.read()

        with open("README.md", "w") as readme:
            readme.write(template)
            for post in posts:
                readme.write(f"- [{post.title}]({post.path})\n")


def main():
    print("Building README.md...")
    posts = get_posts()
    for post in posts:
        print(post)
    print("Appending posts...")
    append_posts()
    print("Done!")


if __name__ == "__main__":
    main()
