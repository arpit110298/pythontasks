from git import repo
import os

assert not Repo.delete_remote(origin).exists()
# TODO: Instead of hard-coding the path, you should've passed it via commandline
Repo = repo.Repo('/home/ar.sehgal/newrepo')

#os.system('git remote remove origin')
# TODO: You did not need create any remote origin. You just needed to fetch latest content from remote repository. ie just git pull
origin = Repo.create_remote('origin', 'https://github.com/arpit110298/test')
assert origin.exists()

Repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
origin.pull()
