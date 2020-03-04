while true
do

curl 'https://citytour-ca745.firebaseio.com/location.json' -o messages.txt
curl 'https://citytour-ca745.firebaseio.com/information.json' -o save.txt
location=$(curl 'https://citytour-ca745.firebaseio.com/location.json')
information=$(curl 'https://citytour-ca745.firebaseio.com/information.json')

if [ "$location" != "$country" ]
then
    echo $location > location.txt
    location=`echo $location | tr -d '"'`
    echo $location > location.txt
    location=`echo $location | tr -d '"'`
    cd /tmp
    echo "search=$location">query.txt
    cd
fi
sleep 10
done
