import os


class generator():
    template_file = '/Users/MICKEY/Github/BlogGenerator/templates/default.html'
    git_path = "/Users/MICKEY/Github/michuang.github.io"

    def __init__(self, template_file, git_path):
        self.template_file = template_file
        self.git_path = git_path

    def sysc_git(git_path):
        # check if the path is valid
        # if not:
        git_path = raw_input(
            "The path is not valid, give me a good one")  # check again
        # if good:
        os.chdir(git_path)
        os.system('git status; git pull')

    def create_new(blog_path, blog_name='new_blog.html'):
        # check template file
        # if not:
        # break
        # if good:
        print '\nGenerating blog...'
        # copy the template file to the blog_path and change the blog_name
        # open the file with atom
