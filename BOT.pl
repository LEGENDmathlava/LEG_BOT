#!/usr/bin/perl
use utf8;

while(true){
  system("./my_commands/LEG.pl");
  system("./my_commands/in_command.pl");
  system("perl my_commands/regex_command.pl");
  system("./my_command.pl");
  system("perl reaction_command.pl"); #なぜか./で反応しない不具合
  system("mypy --strict-optional --disallow-untyped-defs --disallow-untyped-calls --warn-unreachable .");
  system("python3.9 example_bot.py");
}