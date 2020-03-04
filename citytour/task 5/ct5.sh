curl 'https://firebasestorage.googleapis.com/v0/b/citytour-ca745.appspot.com/o/ctour.kml?alt=media' -o citytour.kml
open citytour.kml
while true
do
location=$(curl 'https://citytour-ca745.firebaseio.com/location.json')
information=$(curl 'https://citytour-ca745.firebaseio.com/information.json')
if [ "$location" != "$(<location.txt)" ]
then
    curl 'https://citytour-ca745.firebaseio.com/location.json' -o location.txt
    curl 'https://citytour-ca745.firebaseio.com/information.json' -o information.txt
    cd /tmp
    echo "search=$location">query.txt
    cat query.txt
    cd
fi
done
