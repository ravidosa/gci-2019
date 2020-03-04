mkdir ~/.backgroundLiquidGalaxy
cd ~/.backgroundLiquidGalaxy
curl -L -o backgroundLiquidGalaxy.zip https://www.dropbox.com/s/z5fr38c9a3drc9b/backgroundLiquidGalaxy.zip
unzip backgroundLiquidGalaxy.zip
echo -e "[Desktop Entry]\nName=background Liquid Galaxy\nExec=eog --fullscreen --slide-show "$HOME"/.backgroundLiquidGalaxy\nType=Application" > $HOME"/.config/autostart/backgroundLiquidGalaxy.desktop"
echo "Rebooting, please wait"
sudo reboot