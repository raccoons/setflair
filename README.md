setflair
========

Add flair templates automatically from CSS. (reddit.com)

Login is required, as you must be moderator of the subreddit.

**Usage:**
```
python  set_flair.py  css_file_path|from_ss  subreddit_name  [-options]
```

The CSS argument (`css_file_path|from_ss`) must be a valid file path or the string "from_ss". "from_ss" gets the CSS
from the current stylesheet of the specified subreddit.

**Options:**

`c` clear all existing templates.  
`e` check the box indicating that the user can edit their flair.

**Example:**  
Add flair templates to /r/pics, the styles of which have already been added to the current stylesheet, clear all flair
templates that already exist. 
```
python  set_flair.py  from_ss  pics -c
```
Add some extra flairs from a file (newFlairs.css) located in the CWD. These new flairs are added in addition to the existing
flairs (i.e. no `-c` option)
```
python  set_flair.py  newFlairs.css  pics
```
