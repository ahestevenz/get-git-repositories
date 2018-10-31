from __future__ import print_function
import os
import json
import shutil
import logging
import warnings
import subprocess
import datetime
import numpy as np

class bnGetGitRepos(object):

    def __init__(self, json_file, clone_ssh = False, reset_repos = False):
        logging.info('Initializing the repositories sync')
        self.clone_ssh = clone_ssh
        self.json_file = json_file
        self.reset_repos = reset_repos
        self.load_info()

    def clone_repo(self, url):
        console = self.run_process('cd %s && git clone %s'%(self.json_info['local_storage']['path'], url))
        logging.info(console.stdout)

    def reset_repo(self, repo):
        console = self.run_process('cd %s/%s  && git reset --hard'%(self.json_info['local_storage']['path'], repo))
        logging.info(console.stdout)

    def update_branches(self, repo):
            console = self.run_process('cd %s/%s  && git branch -a'%(self.json_info['local_storage']['path'], repo))
            branches =  [branch for branch in console.stdout.split('\n')]
            
            for (i, branch) in enumerate(branches):
                branch = self.format_branch_name(branch)
                logging.info('Repository: %s | Branch: %s '% (repo, branch))
                console = self.run_process('cd %s/%s  && git checkout %s && git pull origin %s'%(self.json_info['local_storage']['path'], repo, branch,branch))
                logging.info(console.stdout)
            
    def update_repos(self):  
        if not os.path.isdir(self.json_info['local_storage']['path']):
            logging.info(('The local repository storage %s does not exists. Making a new one...')%self.json_info['local_storage']['path'])
            os.makedirs(self.json_info['local_storage']['path'])
              
        for (k, repo) in self.json_info['repos'].items():
            logging.info('Repository: %s '% repo)
            if not os.path.isdir(os.path.join(self.json_info['local_storage']['path'],repo)):
                logging.info(('The git repository does not exists. Cloning %s ...')%repo)
                if (self.clone_ssh):
                    self.clone_repo(os.path.join(self.json_info['git-server']['url-ssh'],repo))
                else:
                    self.clone_repo(os.path.join(self.json_info['git-server']['url-https'],repo))
            if (self.reset_repos): 
                logging.info(('Resetting repository: %s')%repo)
                self.reset_repo(repo)
            try:
                self.update_branches(repo)
            except Exception as e:
                logging.error(("Something went wrong with the following repository: %s . Please check! Error: %s ")%(repo,e))

    
    def load_info(self):
        with open(self.json_file) as f:
            self.json_info = json.load(f) 
            logging.info(('Path to local repositories storage: %s'%(self.json_info['local_storage']['path'])))
            logging.info(('URL to remote HTTPS Git server: %s'%(self.json_info['git-server']['url-https'])))
            logging.info(('URL to remote SSH Git server: %s'%(self.json_info['git-server']['url-ssh'])))
    
    def format_branch_name(self, branch, origin = 'origin'):
        branch = branch.replace('*',' ')
        branch = branch.replace(('remotes/%s/')%(origin),' ')
        branch = branch.replace(('HEAD -> %s/')%(origin),' ')
        return branch

    def run_process(self, cmd):
        console = subprocess.run(cmd, shell=True, universal_newlines=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return console

