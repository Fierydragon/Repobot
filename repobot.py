#!/usr/bin/env python
# encoding: utf-8

from empolyee import EmployCommit
from github import Github
import datetime

input_username = input("Please input user name:")
input_password = input("Please input password:")

github_obj = Github(input_username, input_password)

while True:
    print("You can input these command to get useful message:")
    print(repr("contribution").ljust(15), "- Get author's all commit.")
    print(repr("exit").ljust(15), "- Exit this program.")
    
    input_command = input("select:")

    if input_command == "contribution":
        contributions = {}
        for repo in github_obj.get_user().get_repos():
            print(repo.name)
        input_repo_name = input("select a repo:")
        
        repo_obj = github_obj.get_user().get_repo(input_repo_name)

        print("In %s repository, please input a branch:" % (input_repo_name))
        branch_name = input("Branch:")

        commits = repo_obj.get_commits(sha=branch_name, since=datetime.datetime.now() - datetime.timedelta(999), until=datetime.datetime.now())

        for commit in commits:
            author_name = commit.author.login

            commit_dic = {
                "author": commit.author.login,
                "sha": commit.sha,
                "message": commit.commit.message,
                "url": commit.url,
                "time": commit.last_modified
            }

            if author_name in contributions:
                contributions[author_name].add_commit_tot()
                contributions[author_name].add_commits(commit_dic)
            else:
                contributions[author_name] = EmployCommit(name=author_name, commit_tot=1, commits=[commit_dic])

        for key in contributions:
            contributions[key].show_commit()
            contributions[key].write_2_md()
        print("\n")

    elif input_command == "exit":
        break

    print("*" * 60)