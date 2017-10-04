#!/bin/bash

# Where images are dropped
INBOX='inbox'
mkdir -p processed

# Find all the non-raw images
IMAGES="$(find $INBOX -type f -printf %f\\n | grep -v PLACEHOLDER | egrep -iv '.raw$')"

# Loop through all the non-raw images
while read -r line; do

  # Get the SHA of the non-raw image
  filename=$(basename "$line")
  extension="${filename##*.}"
  filename="${filename%.*}"
  SHA="$(sha1sum "$(echo $INBOX/$line)" | awk '{print $1}')"

  cp -v "$INBOX/$line" processed/$SHA.$extension
  RAW_IMAGES="$(find $inbox -name "$filename*" -type f -printf %f\\n | egrep -i '.raw$')"

  while read -r line; do
    if [ $line ] ; then 
      filename=$(basename "$line")
      extension="${filename##*.}"
      filename="${filename%.*}"
      cp -v "$INBOX/$line" processed/$SHA.$extension
    fi
  done <<< "$RAW_IMAGES"

done <<< "$IMAGES"


#TODO

  # Sort images into folders by date
  # Upload the s3 with never expire header
