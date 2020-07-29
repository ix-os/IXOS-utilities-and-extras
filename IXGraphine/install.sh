
echo "Installing IXGraphine"
#cd dev 
#pip3 install -r requirements.txt &&
#npm install . 
mkdir /etc/IXGraphite
cp -P dev /etc/IXGraphite
echo "Creating shortcut"
chmod u+x /etc/IXGraphite/IXGrapite.desktop
cp -P dev/IXGraphite.desktop ~/Desktop
