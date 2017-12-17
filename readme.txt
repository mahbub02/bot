Install Samba

	sudo apt-get update
	 
	sudo apt-get upgrade
	 
	sudo apt-get install samba samba-common-bin

	sudo apt-get install gedit

	Edit the smb.conf file and add these following lines

		sudo leafpad /etc/samba/smb.conf
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

bluetooth work
	sudo apt-get install bluez python-bluez
	
	Edit bluetooth/main.conf file 
		sudo vim /etc/bluetooth/main.conf
			add this line
			DisablePlugins = pnat
	Edit /lib/systemd/system/bluetooth.service
		add '-C' after 'bluetoothd'. 
	Load serial port
		sudo sdptool add SP
	Reboot the raspberry pi
		sudo reboot
		
	To make your pi bluetooth Discoverable
		sudo hciconfig hci0 piscan
	[change your device name to something else you fancy]
		sudo hciconfig hci0 name 'ourbot' 

https://www.youtube.com/watch?v=DmtJBc229Rg