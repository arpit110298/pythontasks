from git import repo
import os

assert not Repo.delete_remote(origin).exists()
Repo = repo.Repo('/home/ar.sehgal/newrepo')

#os.system('git remote remove origin')
origin = Repo.create_remote('origin', 'https://github.com/arpit110298/test')
assert origin.exists()

Repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
origin.pull()
