chmod +x memex.py
mv memex.py memex
mkdir -p ~/bin
cp -av memex ~/bin

echo 'export PATH=$PATH":$HOME/bin"' >> Users/felix/.zprofile

source Users/felix/.zprofile