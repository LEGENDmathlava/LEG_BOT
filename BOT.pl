#!/usr/bin/perl
use utf8;

while(true){
  system("clear");
  system("./my_commands/LEG_commands/source.pl");
  system("./my_commands/LEG.pl");
  system("./my_commands/in_command.pl");
  system("./my_commands/regex_command.pl");
  system("./my_command.pl");
  system("./reaction_command.pl");
  system("mypy --strict-optional --disallow-untyped-defs --disallow-untyped-calls --warn-unreachable .");
  system("flake8 --ignore=E501,W503 .");
  system("python3.9 example_bot.py");
}