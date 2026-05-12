#!/bin/bash
# Translate remaining Chinese text in .en.md file using sed
cd /Users/arthurbetter/hi3403-build/hi3403-docs/docs/multimedia/mpp

# Set file to work on
FILE="13-proc调试信息-1316-1329.en.md"

# All translations - using sed for each
sed -i '' 's/Y：使能；/Y: Enable;/g' "$FILE"
sed -i '' 's/Y：使能。/Y: Enable./g' "$FILE"
sed -i '' 's/N：不使能；/N: Disable;/g' "$FILE"
sed -i '' 's/N：不使能。/N: Disable./g' "$FILE"
sed -i '' 's/Y：打开；/Y: On;/g' "$FILE"
sed -i '' 's/Y：打开。/Y: On./g' "$FILE"
sed -i '' 's/N：关闭；/N: Off;/g' "$FILE"
sed -i '' 's/N：关闭。/N: Off./g' "$FILE"
sed -i '' 's/0：不使能；/0: Disable;/g' "$FILE"
sed -i '' 's/1：使能。/1: Enable./g' "$FILE"
sed -i '' 's/0：不使用；/0: Not used;/g' "$FILE"
sed -i '' 's/1：使用。/1: Used./g' "$FILE"
sed -i '' 's/0：静音数据；/0: Mute data;/g' "$FILE"
sed -i '' 's/1：非静音数据。/1: Non-mute data./g' "$FILE"
sed -i '' 's/NULL：未占用；/NULL: Not occupied;/g' "$FILE"
sed -i '' 's/1：占用。/1: Occupied./g' "$FILE"
sed -i '' 's/通道ID号。/Channel ID number./g' "$FILE"
sed -i '' 's/通道状态。/Channel status./g' "$FILE"
sed -i '' 's/使能。/Enable./g' "$FILE"
sed -i '' 's/使能状态/enable status/g' "$FILE"
sed -i '' 's/Grp ID号。/Grp ID number./g' "$FILE"
sed -i '' 's/有效范围：/Valid range: /g' "$FILE"
sed -i '' 's/单位：像素/Unit: pixel/g' "$FILE"
sed -i '' 's/坐标类型。/Coordinate type./g' "$FILE"
sed -i '' 's/RAT：相对坐标；/RAT: Relative coordinate;/g' "$FILE"
sed -i '' 's/ABS：绝对坐标。/ABS: Absolute coordinate./g' "$FILE"
sed -i '' 's/通道模式。/Channel mode./g' "$FILE"
echo "Batch 1 complete"
