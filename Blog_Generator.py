import os

blog_path = "~/Github/michuang.github.io"
path = raw_input(
    "Is your bolg in: ~/Github/michuang.github.io ? if not, Enter N:\n")

if path.upper() == "N":
    blog_path = raw_input("Please enter your blog path:\n")

os.system("cd " + blog_path + "; git status")
os.system("cd " + blog_path + "; git pull")

new_blog = raw_input("Do you want to start a new blog?(Y/N)\n")
if new_blog.upper() == "Y":
    blog_name = raw_input("what is the name of your blog?\n")
    if blog_name == "":
        blog_name = "new_blog"
    os.system("cp templates/default.html " + blog_path + "/article/" +
              blog_name + ".html")
    os.system("cd " + blog_path + "/article ; ./" + blog_name + ".html")
