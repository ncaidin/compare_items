__author__ = 'nealcaidin'

# import easygui as eg

# msg=None, title=None, default='*', filetypes=None

# default="/Users/nealcaidin/Documents/Sakai/JiraGen/"
# file_path = default
filetypes = ["*.txt" ]

# assigned_tix = eg.fileopenbox("Pick file of previously assigned tickets", "Assigned tix", default, filetypes)

# print "path is ", path

default="/Users/nealcaidin/Documents/Sakai/JiraDiff/"

file_one = default + "with_reviewed.txt"
file_two = default + "with_compared.txt"

# file_path = "/Users/nealcaidin/Documents/Sakai/"
# file_one = "/Users/nealcaidin/Documents/Sakai/" + "qa01_jiras.txt"
# file_two = "/Users/nealcaidin/Documents/Sakai/JiraPython/" + "jira_issues_filter_13763.txt"
# security_stuff = file_path + "security_issues.txt"

in_both = open(default + "in_both.txt", "w")
in_first_only = open(default + "in_first.txt", "w")
in_second_only = open(default + "in_second.txt", "w")
line_no = 1

first_file = [jira for jira in open(file_one)]
second_file = [jira for jira in open(file_two)]

ff = set(first_file)
sf = set(second_file)

inboth_sets = ff.intersection(sf)
firstonly_set = ff.difference(sf)
secondonly_set = sf.difference(ff)

inboth_size = len(inboth_sets)
firstonly_size = len(firstonly_set)
secondonly_size = len(secondonly_set)
first_file_size = len(first_file)
second_file_size = len(second_file)

print "The number of items in file 1 is " + str(first_file_size)
print "The number of items in file 2 is " + str(second_file_size)

print "The number of items that appear in both files is " + str(inboth_size)
print "The number only in file 1 is " + str(firstonly_size)
print "The number only in file 2 is " + str(secondonly_size)
for issue in inboth_sets:
    print >>in_both, issue,

for issue in firstonly_set:
    print >>in_first_only, issue,

for issue in secondonly_set:
    print >>in_second_only, issue,


if ff.issubset(sf):
    print "file 1 is a subset of file 2"
else:
    count_both = len(inboth_sets)
    count_first = len(ff)
    ratio = round((float(count_both) / float(count_first)) * 100,2)
    print str(ratio) + "% of file 1 is also in file 2"
