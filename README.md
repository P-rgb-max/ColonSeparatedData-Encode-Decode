# ColonSeparatedData-Encode-Decode
My own file format .csd (colon-separated data), and decoder with encode with that.

[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://github.com/P-rgb-max/)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://buymeacoffee/Pdolki/)
<br>
<!-- ![Python](https://simpleicons.org/icons/python.svg)
![Bash](https://simpleicons.org/icons/gnubash.svg) -->
![Python](https://forthebadge.com/images/badges/made-with-python.svg)

To try it, run <code>git clone https://github.com/P-rgb-max/ColonSeparatedData-Encode-Decode.git</code>, then <code>cd ColonSeparatedData-Encode-Decode/</code>, and then <code>csd parse demo.csd</code>.<br>
But you may need to run <code>chmod 751 csd</code> after clone and cd to make possible run it.

The syntaxis is:
 - <code>!something[:oneMore Something[...]]</code> to make title of table
 - <code>#...</code> for comment
 - <code>something[:oneMore Something[...]]</code> to make row of table
 - <code>$...</code> to inline some envirollment variable to the cell of table
 - <code>%...</code> to inline result of some system command to the cell of table
 - <code>@...</code> to inline result of some Python code to the cell of table

Happy parsing!

Please, <a onclick='alert("Thanks!")' href='https://buymeacoffee.com/Pdolki'>Buy me a Pizza</a>!
