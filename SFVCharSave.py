import os
import argparse
import shutil

def copyfiles(src_dir, dest_dir):
    src_files = os.listdir(src_dir)
    print("Copying: {}".format(src_files))
    for file_name in src_files:
        full_name = os.path.join(src_dir, file_name)
        if os.path.isfile(full_name):
            shutil.copy(full_name, dest_dir)

DEFAULT_DIR = os.path.expanduser('~\\SFVSaves\\')
SFV_SAVEDIR = os.path.expandvars('%LOCALAPPDATA%\\StreetFighterV\\Saved\\SaveGames\\')
print(SFV_SAVEDIR)

parser = argparse.ArgumentParser(description='Move Character files from SFV Saved game to somewhere somewhere useful')
parser.add_argument('-s', dest='save', help='Save the current character files under the given name')
parser.add_argument('-l', dest='load', help='Load the given character name (Will overwrite any current character)')
parser.add_argument('--location', dest='location', default=DEFAULT_DIR, help='Sets the default location to save character files to (Defaults to {})'.format(DEFAULT_DIR))
args = parser.parse_args()

if args.save:
    fullpath = os.path.join(args.location, args.save)
    print('Saving current character to {}'.format(fullpath))
    os.makedirs(fullpath, exist_ok=True)
    copyfiles(SFV_SAVEDIR, fullpath)
if args.load:
    fullpath = os.path.join(args.location, args.load)
    print('Loading character from {}'.format(fullpath))
    copyfiles(fullpath, SFV_SAVEDIR)
