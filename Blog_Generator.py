import os


def sysc_git(blog_path):
    os.chdir(blog_path)
    os.system("git status; git pull")


def creat_new_blog(blog_path, blog_name):
    print "\nGenerating the blog......"
    os.system("cp /Users/MICKEY/Github/BlogGenerator/templates/default.html " +
              blog_path + "/article/" + blog_name + ".html")
    os.system("cd " + blog_path + "/article ; atom " + blog_name + ".html")
    print "\nNew blog has been created, please edit it in Atom.\n"


def main():
    print "\nWelcome to the super simple Blog Generator v1.0\n"
    blog_path = "/Users/MICKEY/Github/michuang.github.io"
    path = raw_input("Is your bolg in: " + blog_path +
                     " ? if not, Enter \"N\",if yes, just pass:\n")
    if path.upper() == "N":
        blog_path = raw_input("Please enter your blog path:\n")
    sysc_git(blog_path)
    new_blog = raw_input("\nDo you want to start a new blog?(Y/N)\n")
    if new_blog.upper() == "Y":
        blog_name = raw_input("\nwhat is the name of your new blog?\n")
        if blog_name == "":
            blog_name = "new_blog"
    creat_new_blog(blog_path, blog_name)


main()
