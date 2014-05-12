__author__ = 'youngsoul'
import subprocess
import cmd

repo_path = "/Users/youngsoul/Documents/Development/GitProject/testrepo/testrepo"
repo_url = 'git@github.com:youngsoul/testrepo.git'
key_file = open('/Users/youngsoul/.ssh/id_rsa')


class GitCommandProcessor(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)

    def do_version(self, line):
        command = "git describe --tags"
        process = subprocess.Popen(command.split(), cwd=repo_path, stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print "Current Tag Version: " + output


    def do_all_tags(self,line):
        command = "git ls-remote --tags"
        process = subprocess.Popen(command.split(), cwd=repo_path, stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print "All Tag Version: \n" + output



    def do_fetch_all(self,line):
        command = "git fetch origin"
        process = subprocess.Popen(command.split(), cwd=repo_path, stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print "FetchAll: \n" + output


    def do_checkout_tag(self,line):
        command = "git checkout " +line
        process = subprocess.Popen(command.split(), cwd=repo_path, stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print "Checkout Tag: \n" + output


    def do_EOF(self,line):
        return True