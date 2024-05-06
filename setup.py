#!/usr/bin/env python

from distutils.core import setup
                    
# Get git commit info to build version number/tag
#repo = git.Repo('.git')
#git_hash = repo.head.object.hexsha
#git_url = repo.remotes.origin.url
#v = repo.git.describe(always=True)
#if repo.is_dirty(): v += ".dirty"
v = 1.5

setup(name='wormdatamodel',
      version=v,
      description='Data models for whole brain imaging recordings.',
      author='Francesco Randi',
      author_email='francesco.randi@gmail.com',
      packages=['wormdatamodel','wormdatamodel.data','wormdatamodel.signal'],
      install_requires=['sklearn', 'matplotlib'],
     )
