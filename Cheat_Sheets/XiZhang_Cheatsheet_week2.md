XiZhang_cheatsheet

####request
What is GitHub and version control
What is a repo
The difference between local, remote, origin
The major actions and what they mean - Clone, Fork,
Commit, Push, Pull, Fetch (note this could lend itself to a graphic illustration)

###cheat sheet

Git: version control software, need download
GitHub: cloud based repo sharing, need to create account
Git Kraken: GUI (graphical user interface, means can click and point) for interaction with repos
Command line/Terminal/ Git  Bash: ways of providing commands directing to comp
SSH keys(secure shell): Way of doing secure file transfers how we pass back forth with GitHub
repo:a folder but not exactly same as a folder. cannot be under another repository. update using pull or push buttons of GitKraken. 

HAS_Tools (just a folder)
-Course-materal-21 (repo, can rename repo folder but not things within it)   where all assignments materials will be posted. You can’t nake changes. Pull only

--Assignments
--content
-forecasting21_git we do out competition you post forecast here, posh and pull only change your forecast
-homework_yourname_git  (your space do what you want, submit hw pull and pushing
--homework 1
--Submission
--cheat sheet
-class notes

GitHub: remote repository
=========================================
**Clone,Fork Commit,Push,Pull and Fetch

Clone is copying the remote repository to a local machine that can be done using a command “git clone”. Any changes made in this cloned repository can be shown in the original repository. 

Fork is copying a repository but with full control of the copied repository, which is a new repository and any changes to the forked repository will not be reflected to the original repository.

Commit is recording changes to files we made with a unique ID.

Push is used to upload committed local changes to the remote repository.

Pull is taking all changes from the remote repository to your local and update the local repository.
Fetch is a way to download all changes to your local and review it; however, fetch will not integrate all new changes with the local repository. 


‘：’： colon
===================
lists tupe of object:
squate brecket
separated bu commas, can be int float str.
mylist=['a','b','c','d']
mylist[2]='c'
mylist[0:2]=['a','b']
mylist[0:3:2](start, end ,count)=['a','c']
mylist[:2]=['a','b']
mylist[2:]=['c','d']
**mylist[3:0:-1]=['d','c','b']


letters=['a','b','c','d']
letters.append('t')
>letters=['a','b','c','d','t']
letters.insert(2,'m')
>letters=['a','b','m','c','d','t']


opratorssymbol that has an associate operator
:*+_/**
comparison:>,<,=>,=<,!=
logical: not or no
membership: in or not in
identity: is, isnot
assignment:+=
var=7
var=var+3   var+=3
var=var*3   var*=3

letters=['a','b','c','d','e','t']
spell 'bad','cat'
letters[1]+letters[0]+letters[3]
letters[1-6]+letters[0-6]+letters[3-6]
letters[1].append['a'].append['d']