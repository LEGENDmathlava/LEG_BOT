#!/usr/bin/perl
use utf8;

while(true){
  system("./my_commands/LEG.pl");
  system("./my_commands/in_command.pl");
  system("./my_commands/regex_command.pl");
  system("./my_command.pl");
  system("perl reaction_command.pl"); #なぜか./で反応しない不具合
  system("python3 example_bot.py");
}