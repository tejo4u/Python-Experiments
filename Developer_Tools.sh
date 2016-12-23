#!/bin/sh

# Author Gajesh Bhat
# Shell Script to Install basic Dev Tools in Ubuntu or its Derivatives.

#Clear the Screen before Starting the Install
clear

#Updating the Software Repos and Uprading the System
printf "Preparing the System for installation..."
sleep 3

sudo apt-get -y update
sudo apt-get -y upgrade

printf "Installing Developer Tools..."
sleep 3

#Build Essentials
sudo apt-get -y install build-essential

#Clang Support
sudo apt-get -y install clang

#Installing Git
sudo apt-get -y install git

#Configure git
printf "Github Basic Account Info Setup...\n1.Enter Your Account User Name\n"
read git_username
git config --global user.name git_username
printf "\n2.Enter Your Account Email Id\n"
read git_useremail
git config --global user.email git_useremail

#Install C++14 Support for g++ and gcc
sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y
sudo apt-get -y update
sudo apt-get -y install g++-4.9
# set g++4.9 as default compiler, the symlink in has to be updated:
sudo ln -f -s /usr/bin/g++-4.9 /usr/bin/g++

#Install Python tools
sudo apt-get -y install python3
sudo apt-get -y install python-pip

#Install Java ,JDK and JRE
sudo apt-get -y install default-jre
sudo apt-get -y install default-jdk

#Install Atom Text Editor
sudo add-apt-repository ppa:webupd8team/atom -y
sudo apt-get -y update
sudo apt-get -y install atom

#Install haskell
sudo apt-get -y install haskell-platform
