chmod +x memex.py
mv memex.py memex
mkdir -p ~/bin
cp memex ~/bin
echo 'export PATH=$PATH":$HOME/bin"' >> .profile

source .profile