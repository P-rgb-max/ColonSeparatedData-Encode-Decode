
#!/bin/bash

export csdDataPath="/Users/dmitriymac/Documents/development/shell/csd-data"

case $1 in
    parse|decode|read|load)
	bash "$csdDataPath/parse.sh" $2
	;;
    type|encode|write|save)
	bash "$csdDataPath/type.sh" $2
	;;
    help|-h|-?|?)
	echo "Usage: `basename $0` parse|type <file>.csd|<file>.csv"
	exit
	;;
    troubleshoot|*)
	echo "Error: restart with option help"
	;;
esac
