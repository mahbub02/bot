set pass "Hateyou12"
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install samba samba-common-bin
sudo apt-get install gedit

send "$pass"
send "$pass
hostname -I

sed -i '1 i\ [share]\nComment = Pi shared folder\nPath = \/share\nBrowseable = yes\nWriteable = Yes\nonly guest = no\ncreate mask = 0777\ndirectory mask = 0777\nPublic = yes\nGuest ok = yes\n ' haha.txt