#!/usr/bin/perl
use strict;
use warnings;
use utf8;
use open IN  => ":utf8";
use open OUT => ":utf8";
use open IO => ":utf8";

my @command_module_files = grep {$_ ne "my_commands/__init__.py"} (glob "my_commands/*.py");
my @functions;
my %file2modules;
foreach my $command_module_file (@command_module_files){
  open IN, '<', $command_module_file;
  my $functions_line = <IN>;
  $functions_line =~ s/\x0D?\x0A?$//;
  my @temp = split / /, (substr $functions_line, 1, ((length $functions_line) - 1));
  $file2modules{$command_module_file} = join(', ', @temp);
  @functions = (@functions, @temp);
  close IN;
}

open FH, '>', "my_command.py";
print FH "import discord\n";
foreach my $command_module_file (@command_module_files){
  my $command_module = $command_module_file;
  $command_module =~ s/\//./g;
  $command_module =~ s/.py$//;
  print FH "from $command_module import ";
  print FH $file2modules{$command_module_file};
  print FH "\n";
}

print FH "async def my_command(message:discord.Message)->None:\n    m = message.content.split()\n    if len(m) == 0:\n        return\n    if (m[0] in globals()) and (str(globals()[m[0]])[:9] == '<function'):\n        await globals()[m[0]](m, message)\n    await in_command(message)\n    await regex_command(message)\n";
close FH;