# AdamXweb.github.io
Creating a blog from previous site but based on Hugo

# Usage
On new clone, Dev branch is the hugo site pre-compiled.

Series of commands are:
`git checkout dev` to go to dev branch
`git submodule add -b master git@github.com:AdamXweb/AdamXweb.github.io.git public` to add the master branch into the public folder
After any changes are made, simply run `bash deploy.sh` this will pull latest changes from dev (if forestry is conencted then changes will be pulled), compile the site, then push the new site to the master branch, updating the live version.
