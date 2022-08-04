# MKV BULK SUBS

## What is it?

> It's a simple script to automate adding subtitles to movies or series in MKV format using SRT files.

## Whats requided?

- python
- mkvmerge (mkvtoolnix-cli)
- rm

## How it work?

### In your terminal

```
git clone https://www.github.com/WulffenSec/mkv-bulk-subs.git
cd mkv-bulk-subs
python mkv-bulk-subs.py
```

The script will check for MKV and SRT files in the script folder, ask you to check if the MKV and SRT names are similar.

When Yes is given it's going to create subs free files (this is helpful if your mkv had other SRT files loaded) it going to use those files to create the new subtitled files and remove the "no sub" files to clean up.
