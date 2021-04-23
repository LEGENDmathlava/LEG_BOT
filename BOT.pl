#!/usr/bin/perl
use utf8;
# perl BOT.pl | rotatelogs -e -n 10 ./log/log 1M
while(true){
  system("clear");
  system("echo \"\" | rotatelogs -e -n 10 ./log/log 1M");
  system("date | rotatelogs -e -n 10 ./log/log 1M");
  system("./my_commands/LEG_commands/source.pl | rotatelogs -e -n 10 ./log/log 1M");
  system("./my_commands/LEG.pl | rotatelogs -e -n 10 ./log/log 1M");
  system("./my_commands/in_command.pl | rotatelogs -e -n 10 ./log/log 1M");
  system("./my_commands/regex_command.pl | rotatelogs -e -n 10 ./log/log 1M");
  system("./my_command.pl | rotatelogs -e -n 10 ./log/log 1M");
  system("./reaction_command.pl | rotatelogs -e -n 10 ./log/log 1M");
  system("mypy --strict-optional --disallow-untyped-defs --disallow-untyped-calls --warn-unreachable . | rotatelogs -e -n 10 ./log/log 1M");
  system("flake8 --ignore=E501,W503 . | rotatelogs -e -n 10 ./log/log 1M");
  system("python3.9 -u example_bot.py | rotatelogs -e -n 10 ./log/log 1M");
  system("echo \"reboot LEG_BOT\" | rotatelogs -e -n 10 ./log/log 1M");
}