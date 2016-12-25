#!/bin/sh

# Author Gajesh Bhat
#Shell Scipt to Setup freshy Installed Ubuntu System.
#Clear the Screen before Starting the Install
clear

#Change the server to main server for update
printf "Changing the Local Mirror Server to Main Server..."
sudo sed -i 's|http://in.|http://|g' /etc/apt/sources.list

#Enable Third Party Repos and Update the Repo List
printf "Enabling Third-Party Repos..."
DISTRO=`cat /etc/*-release | grep DISTRIB_CODENAME | sed 's/.*=//g'`
sudo sed -i.bak 's/\(# \)\(deb .*ubuntu '${DISTRO}' partner\)/\2/g' /etc/apt/sources.list

#Removing Unity Lens and realted dash Plugins.
printf "Removing Amazon Dash Plugins and Unity Dash lens for Amazon Services..."
sudo apt-get -y remove unity-lens-shopping
gsettings set com.canonical.Unity.Lenses disabled-scopes "['more_suggestions-amazon.scope', 'more_suggestions-u1ms.scope', 'more_suggestions-populartracks.scope', 'music-musicstore.scope', 'more_suggestions-ebay.scope', 'more_suggestions-ubuntushop.scope', 'more_suggestions-skimlinks.scope']"
gsettings set com.canonical.Unity.Lenses remote-content-search none
sudo rm /usr/share/applications/ubuntu-amazon-default.desktop
sudo apt-get -y -f install


printf "Updating Software Repos and Proceding to Full System Update...."
sudo apt-get -y update
sudo apt-get -y upgrade

#Installing the Resticted Extras and VLC Media Player
printf "Installing Restricted Extras.... (Audio and Video Plugins)"
sudo apt-get -y install ubuntu-restricted-extras
printf "Installing VLC Player..."
sudo apt-get -y install vlc

#Installing additional required Packages (Synaptic Package manager,Chromium,Unity Tweak Tool)
printf "Installing Addtional Software..."
printf "1.Synaptic Package manager\n2.Chromium Web Browser\n3.Unity Tweak Tool\n4.GDebi Package Installer"
sudo apt-get -y install chromium-browser #Chromium Web Browser
sudo apt-get -y install synaptic # Synaptic Package manager
sudo apt-get -y install unity-tweak-tool #Unity Tweak Tool
sudo apt-get -y install gdebi #Gdebi Package Installer
