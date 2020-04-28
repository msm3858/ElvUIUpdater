import argparse

parser = argparse.ArgumentParser(description='ElvUI updater.')
parser.add_argument('-b', '--blizz_addon_path', help='Blizzard addons path.')
parser.add_argument('-e', '--extracted_elvui', help='Extracted elvui directory name.')

args = parser.parse_args()
