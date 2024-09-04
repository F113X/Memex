# Memex
A program to optimize reviewing and active learning using the Ebbinghaus forgetting curve

## Usage

**Currently only macos is supported because I don't have the ability to test it on other OS's**

**For mac**
1. Download the latest release from github (latest 0.1.0), and uncompress the zip file. 
2. Put the uncompressed folder into your home directory
3. Open the 'subjects.txt' file and enter in the subjects with no whitespace and a new line for each subject
4. Open the 'memex.py' file and replace the areas that say 'YOURHOMEDIR' with your own home directory name
5. Open the 'setup.sh' file and replace the areas that say 'YOURHOMEDIR' with your own home directory name
6. Open the Terminal app to setup the program
7. Change directory to the memex directory with the command
`cd memex`
8. Run the setup bash code using command
`bash setup.sh`
9. cd out of the current directory with command
`cd`
or restart the Terminal
10. To further learn how to use memex, type in the command
`memex -h`
or 
`memex --help`

**Note: Scheduled run is not available yet because I have not figured out how to make it**

**DO NOT CHANGE OR DELETE THE DATE IN EACH NOTE FILE OR THE FILENAMES AS IT WILL BREAK THE PROGRAM**