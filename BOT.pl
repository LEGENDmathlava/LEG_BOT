#!/usr/bin/perl
use utf8;
# perl BOT.pl | rotatelogs -e -n 10 ./log/log 1K
# bash logging_message.sh | rotatelogs -e -n 10 ./log/message_log 1M を 忘れずに 実行
while(true){
  system("clear");
  system("echo \"\"");
  system("date");
  system("./my_commands/LEG_commands/source.pl");
  system("./my_commands/LEG.pl");
  system("./my_commands/in_command.pl");
  system("./my_commands/regex_command.pl");
  system("./my_command.pl");
  system("./reaction_command.pl");
  system("mypy --strict-optional --disallow-untyped-defs --disallow-untyped-calls --warn-unreachable .");
  system("flake8 --ignore=E501,W503 .");
  system("python3.9 -u example_bot.py 2>&1");
  system("echo \"reboot LEG_BOT\"");
}