testing

This week, you will be on a small team working on a project. 
Your team should use feature branches for development. 
You can use GitHub issues to keep track of what needs to be done 
and who is working on what.

Use your combined creativity and good judgment to make decisions as you work. 
Users expect to see some common features in web applications. 
If they are not mentioned in the project's description, you should still do them. 
For example: in the code snippet application, users should have avatar images. 
You don't have to handle file uploads yourself -- you could use Gravatar with 
django-gravatar -- but you need some way of handling that.

In addition to those small features, come up with your own features to make your 
project unique. You will likely use this project in your portfolio, so make it 
something you can be proud of.

No starter repo is provided, so you will have to run the django-admin commands 
to create a new project.

Rules for all projects
Your application should be styled. It should be usable and aesthetically neutral, 
at a minimum. You can use a library or you can write custom css, or both. It is up to you.
Your application must include a README.md file with instructions on how to run it. 
Take a look at this site on README basics for a good markdown template you can follow, 
and links to example READMEs.
Your application should be able to run from scratch by downloading the repo, running 
pipenv install, pipenv shell, python manage.py migrate, and python manage.py runserver. 
If there are any other steps necessary, please put them in the README.md file.
Stretch goal for each project: trying new things
Teams should consider trying something they don't know how to do on their project. This could be a Python or JavaScript library they haven't used before or a feature of Django they haven't tried.

The Projects
Your team should choose one of these options.

Option 1: Code Snippet Manager
You need a good way to manage snippets of code you reuse often. You are going to build 
a web application that has these goals:

Logged in users can add code snippets.
Logged in users can search their own code snippets and get results.
Each user has a profile page that shows their public code snippets. Other users can copy 
a snippet with one click, adding it to their library of snippets.
How snippets work
A snippet has code (required), a language (required), a title (optional), and 
whatever other fields make sense. Some ideas to consider: a description or a list of tags.

If you copy a snippet by clicking the copy button (or whatever UI element is used for 
this purpose), there's a link back to the original snippet. The easiest way to do this 
is with a foreign key. One should be able to see how many times a snippet has been copied.

The reason why we copy snippets instead of "favorite" them is that they can change. 
The original snippet creator can edit their snippet; the copying user can edit their copy.

How search works
Search should look for terms in the title, in other fields like a description or tags, 
and in the language field. If I search for "javascript auth," I should see any snippets 
I have about authentication using JavaScript. See search in the Django documentation for 
some ideas.

How much of this is JavaScript?
This can vary, but the two parts that definitely need JavaScript are syntax highlighting 
and copying a code snippet to your clipboard.

For syntax highlighting, check out Prism.js or Highlight.js.

See this article on native browser copy to clipboard for ideas on how to copy to clipboard.