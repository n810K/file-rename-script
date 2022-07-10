# file-rename-script
A quick tool to rename files within a directory and subdirectories written in Python

## Usage

This script takes in 
1. Directory 
2. Phrase
3. Replacement Phrase

Follow the prompts

## Example:

`01. Song Name .flac` to `01. Song Name.flac` within `\Music\Album\Artist\Artist - Album (Year)`

Following the prompts, input the phrase to be replaced, in this case " .flac", then input the replacement phrase, ".flac".

Then input the "root" directory, `\Music\Album\Artist\` 

All files, including those in subdirectories will be renamed if the file contains the phrase " .flac", replacing it with ".flac"
