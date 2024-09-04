chmod +x memex.py
mv memex.py memex
mkdir -p ~/bin
cp -av memex ~/bin

echo 'export PATH=$PATH":$HOME/bin"' >> Users/YOURHOMEDIR/.zprofile

source Users/YOURHOMEDIR/.zprofile