import os


def sync_git(blog_path):
    os.chdir(blog_path)
    os.system("git status; git pull")


# create and auto open the blog
def creat_new_blog(blog_path, blog_file):
    print "\nGenerating the blog......"
    os.system("cp /Users/MICKEY/Github/BlogGenerator/templates/default.html " +
              blog_path + "/article/" + blog_file)
    os.chdir(blog_path + "/article")
    print "\nNew blog has been created, please edit it in Atom.\n"
    os.system("atom " + blog_file)


def main():
    print "\nWelcome to the super simple Blog Generator v1.0\n"
    blog_path = "/Users/MICKEY/Github/michuang.github.io"
    path = raw_input("Is your bolg in: " + blog_path +
                     " ? if not, Enter \"N\",if yes, just pass:\n")
    if path.upper() == "N":
        blog_path = raw_input("Please enter your blog path:\n")

    sync_git(blog_path)

    new_blog = raw_input("\nDo you want to start a new blog?(Y/N)\n")
    if new_blog.upper() == "Y":
        blog_file = raw_input(
            "\nwhat is the file of your new blog?\n") + ".html"
        if blog_file == ".html":
            blog_file = "new_blog.html"

    creat_new_blog(blog_path, blog_file)


main()
