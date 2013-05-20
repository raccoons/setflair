# Setting Flair Templates
import praw
import re
from getpass import getpass
from sys import argv, exit

def set_flair(css_file, sub_name, clear=False, can_edit=False): 
	r = praw.Reddit(user_agent='Setting flair for /r/%s' % sub_name)
	print 'Setting flair for /r/%s' % sub_name
	r.login(raw_input('User name: ').strip(), getpass('Password: ').strip())
	sub = r.get_subreddit(sub_name)

	if clear:
		print "Clearing all existing flair templates"
		sub.clear_flair_templates()

	if css_file.strip() == 'from_ss':
		css = str(sub.get_stylesheet()['stylesheet'])
	else:
		css = open(css_file).read()

	css_classes = set(re.findall(r'\.flair-([\w-]+)', css))
	for i in css_classes:
		sub.add_flair_template(text_editable=can_edit, css_class=i)
		print 'Flair template added:', i

if __name__ == '__main__':
	try:
		css_file = argv[1]  # can also be string 'from_ss'
		sub_name = argv[2]
		if argv[3:4]: 
			options = argv[3]
		else:
			options = ''
		clear = True if 'c' in options else False
		can_edit = True if 'e' in options else False
	except IndexError:
		print '\nUSAGE: python\tset_flair.py\tcss_file_path|from_ss\tsubreddit_name\t[-options]\n'
		print 'options: c\tclear all existing templates.' 
		print '         e\tcheck the box indicating that the user can edit thier flair.\n'
		print 'CSS can be from a file or from the current subreddit \
stylesheet by putting "from_ss" instead of a file path.\n'
		exit(0)
	
	set_flair(css_file, sub_name, clear, can_edit)
	