Install Samba

	sudo apt-get update
	 
	sudo apt-get upgrade
	 
	sudo apt-get install samba samba-common-bin

	sudo apt-get install gedit

	sudo leafpad /etc/samba/smb.conf


	Add this into the smb.conf file

	[share]
		Comment = Pi shared folder
		Path = /
		Browseable = yes
		Writeable = Yes
		only guest = no
		create mask = 0777
		directory mask = 0777
		Public = yes
		Guest ok = yes
