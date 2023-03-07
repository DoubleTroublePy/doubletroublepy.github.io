# create a new post
import sys
import os
import datetime

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Usage: python newPost.py <post title>")
        sys.exit(1)

    title = sys.argv[1]
    title = title.replace(' ', '-')

    # get the current date
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")

    # create the post file
    filename = date + '-' + title + '.md'
    filepath = os.path.join('_posts', filename)
    if os.path.exists(filepath):
        print('File already exists: ' + filepath)
        sys.exit(1)

    # write the post file
    with(open(filepath, 'w')) as f:
        f.write('---\n')
        f.write('layout: post\n')
        f.write('title: ' + title + '\n')
        f.write('date: ' + date + '\n')
        f.write('---\n\n')
    