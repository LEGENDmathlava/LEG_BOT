#!/bin/bash
trap "exit 0" 3 # QUITシグナルで停止

# --formatで"ディレクトリ ファイル名 イベント"の形式で出力するように指定
inotifywait -e CLOSE_WRITE -m ECHO_FLOWER --format "%w %f %e" | \
while read LINE; do
  cat ECHO_FLOWER
  echo -e "\n"
done