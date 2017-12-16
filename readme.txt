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

To install vim
	sudo apt-get install vim

bluetooth work
	sudo apt-get install bluez python-bluez
	sudo vim /etc/bluetooth/main.conf
	add this line
		DisablePlugins = pnat
	To make your pi bluetooth Discoverable
		sudo hciconfig hci0 piscan
	[change your device name to something else you fancy]
		sudo hciconfig hci0 name 'ourbot' 

https://www.youtube.com/watch?v=DmtJBc229Rg