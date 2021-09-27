# APP NAME

BLOG-SITE

# AUTHOR

Kinoti Gitonga

# DESCRIPTION

This is my personal blogging site where the writer can log in and write a blog and the users sign up ,log in, comment on, vote on or like the blog.

#### User Stories

- As a user I would like to view the blog posts submitted
- As a user I would like to comment on blog posts
- As a user I would like to view the most recent posts
- As a user I would like to alerted when a new post is made by joining a subscription.
- As a writer I would like to sign in to the blog.
- As a writer I would also like to create blog from the application.
- As a writer I would like to delete comments that I find insulting or degrading.
- As a writer I would like to update or delete blogs i have created.

## Installation steps

- $ git clone https://github.com/ikinoti/blog-site.git
- $ cd blog-site
- $ source virtual/bin/activate
- Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
- $ ./start.sh

# How it works

- A user needs to sign up
- A user the needs to sign in order to create a blog.

# Technologies Used

- HTML5/CSS
- Bootstrap
- Python3.8
- flask

# Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me through isaiah.gitonga@student.moringaschool.com or leave a commit here on github.

# License

- MIT License
