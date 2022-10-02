import os
import sys


# Get all files under /posts
def get_posts():
    posts = []
    for root, dirs, files in os.walk('posts'):
        for file in files:
            posts.append(file)
    return posts

print(get_posts())

# append all posts to the README.md
def append_posts():
    posts = get_posts()
    with open("Template.md", "r") as template:
        template = template.read()
        
        with open("README.md", "w") as readme:
            readme.write(template)
            for post in posts:
                readme.write(f"- [{post}]({post})\n")
    
append_posts()  