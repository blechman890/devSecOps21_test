read name

if [ -z "$name" ]
then
echo "No name entered" >&2
exit 1
elif [ $name != "Ilya" ]
then echo entered $name
elif [ $name = "Ilya" ]
then printf "Ilya is the best!\n"

fi
