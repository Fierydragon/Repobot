# !/usr/bin/env python
# encoding: utf-8

class EmployCommit:
    def __init__(self, name, commit_tot=0, commits=[]):
        self.name = name
        self.commit_tot = commit_tot
        self.commits = commits

    def add_commit_tot(self):
        self.commit_tot += 1
    
    def add_commits(self, commit):
        self.commits.append(commit)
    
    def show_commit(self):
        for commit in self.commits:
            print()
            print(repr(commit['sha']).ljust(20), repr(commit['time'].ljust(20)))
            print(repr(commit['url']))
            print()

    def write_2_md(self):
        file_name = self.name + '-commit-list.md'
        f = open(file_name, "w")
        print("#", self.name, "的周报", file=f)
        # print("##", self.name, "在本周共有", self.commit_tot, "次提交", file=f)
        print("## %s 在本周共有 %d 次提交" % (self.name, self.commit_tot), file=f)

        index = 1
        for commit in self.commits:
            print("%d. %s [%s] %s" % (index, commit['message'], commit['url'], commit['time']), file=f)
            index += 1
            print("---------", file=f)

        f.close