import sys
commit_message_list = sys.argv[1::]
if("CI" in commit_message_list):
    idx = commit_message_list.index("CI")
    for i in range(idx+1, len(commit_message_list)):
        print(commit_message_list[i], end=" ")
