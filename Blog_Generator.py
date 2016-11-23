import os

print "\nWelcome to the super simple Blog Generator v1.0\n"
blog_path = "~/Github/michuang.github.io"
path = raw_input(
    "Is your bolg in: ~/Github/michuang.github.io ? if not, Enter \"N\",if yes, just pass:\n")

if path.upper() == "N":
    blog_path = raw_input("Please enter your blog path:\n")

os.system("cd " + blog_path + "; git status")
os.system("cd " + blog_path + "; git pull")

new_blog = raw_input("\nDo you want to start a new blog?(Y/N)\n")
if new_blog.upper() == "Y":
    blog_name = raw_input("\nwhat is the name of your new blog?\n")
    if blog_name == "":
        blog_name = "new_blog"

    print "\nGenerating the blog......"
    os.system("cp templates/default.html " + blog_path + "/article/" +
              blog_name + ".html")
    os.system("cd " + blog_path + "/article ; atom " + blog_name + ".html")
    print "\nNew blog has been created, please edit it in Atom.\n"
