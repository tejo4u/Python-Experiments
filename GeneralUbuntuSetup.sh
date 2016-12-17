#Clear the Screen before Starting the Install
clear

#Change the server to main server for update
printf "Changing the Mirror Server to Main Server..."
sleep 3
sudo sed -i 's|http://in.|http://|g' /etc/apt/sources.list

#Enable Third Party Repos and Update the Repo List
printf "Enabling Third-Party Repos and Proceding for Repository Update...."
sleep 3
DISTRO=`cat /etc/*-release | grep DISTRIB_CODENAME | sed 's/.*=//g'`
sudo sed -i.bak 's/\(# \)\(deb .*ubuntu '${DISTRO}' partner\)/\2/g' /etc/apt/sources.list
sudo apt-get -y update

#Removing Unity Lens and realted dash Plugins.
printf "Removing Amazon Dash Plugins and Unity Dash lens for Amazon Services..."
sleep 3
sudo apt-get -y remove unity-lens-shopping
gsettings set com.canonical.Unity.Lenses disabled-scopes "['more_suggestions-amazon.scope', 'more_suggestions-u1ms.scope', 'more_suggestions-populartracks.scope', 'music-musicstore.scope', 'more_suggestions-ebay.scope', 'more_suggestions-ubuntushop.scope', 'more_suggestions-skimlinks.scope']"
gsettings set com.canonical.Unity.Lenses remote-content-search none
sudo rm /usr/share/applications/ubuntu-amazon-default.desktop
sudo apt-get -y -f install


printf "Proceding to Full System Update...."
sleep 3
sudo apt-get -y upgrade

#Installing the Resticted Extras and VLC Media Player
printf "Installing Restricted Extras.... (Audio and Video Plugins)"
sleep 3
sudo apt-get -y install ubuntu-restricted-extras
printf "Installing VLC Player..."
sleep 3
sudo apt-get -y install vlc

#Installing additional required Packages (Synaptic Package manager,Chromium,Unity Tweak Tool)
printf "Installing Addtional Software..."
printf "1.Synaptic Package manager\n2.Chromium Web Browser\n3.Unity Tweak Tool\n4."
