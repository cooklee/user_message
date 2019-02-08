import argparse

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', help='User Login')
parser.add_argument('-p', '--password', help='User Password')
parser.add_argument('-n', '--new-pass', help='User New Password')
parser.add_argument('-l', '--list', help='Show all users')
parser.add_argument('-d', '--delete', help='User login to delete')
parser.add_argument('-e', '--edit', help='User Login to edit')
args = parser.parse_args()

#
# if u and p and not e and not d:
#     create_new_user_if_not_exist
# if u and p and e and n:
#     set_new_password
# if u and p and d:
#     delete_user
# if l:
#     show_all_user_name()
# else
#     show_help