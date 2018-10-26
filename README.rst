Download Git Repositories
=========================

**get-git-repositories** is a python package which synchronizes git repositories from any Git cloud service. 

**bnGetGitRepos** 
------------------

Python class that sync git repositories from a Git server (cloud service or private server) specified in a JSON file. 

**repos.json**
--------------

This JSON file specifies the repositories which will be syncronized, and it must be written with the format described below.

}
    {
    "git-server" : {
    "url-https"  : "https://ahestevenz@github.com/ahestevenz/",
    "url-ssh"  : "git@github.com:ahestevenz/"
    },
    "local_storage" : {
    "path"  : "/Users/ahestevenz/Desktop/repos"
    },
    "repos" : {
    "1"  : "project-1",
    "2"  : "project-2",
    "3"  : "project-3"
    }
}

Finally, run the command!
-------------------------
.. code-block:: bash

    (dev) ahestevenz@galactica:~ $ bn-get-repositories -h
    usage: bn-get-repositories [-h] [-j JSON_FILE] [-ssh CLONE_SSH]
                            [-r RESET_REPOS] [-v] [-p output.prof]

    Welcome

    optional arguments:
    -h, --help            show this help message and exit
    -j JSON_FILE, --json_file JSON_FILE
                            JSON file with repos information (default:
                            "/Users/ahestevenz/.userfiles/conf/repos.json")
    -ssh CLONE_SSH, --clone_ssh CLONE_SSH
                            flag to enable clone repositories throw SSH key
                            (default: "False")
    -r RESET_REPOS, --reset_repos RESET_REPOS
                            flag to reset all the repositories (default: "False")
    -v, --verbose         Increase logging output (default: INFO)(can be
                            specified several times)
    -p output.prof, --profile output.prof
                            Run with profiling and store output in given file

