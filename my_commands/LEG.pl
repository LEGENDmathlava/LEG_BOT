#!/usr/bin/perl
use strict;
use warnings;
use utf8;
use open IN  => ":utf8";
use open OUT => ":utf8";
use open IO => ":utf8";

my @command_module_files = grep {$_ ne "my_commands/LEG_commands/__init__.py"} (glob "my_commands/LEG_commands/*.py");
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

open FH, '>', "my_commands/LEG.py";
print FH "#LEG\nimport discord\nfrom typing import List\n";
foreach my $command_module_file (@command_module_files){
  my $command_module = $command_module_file;
  $command_module =~ s/\//./g;
  $command_module =~ s/.py$//;
  print FH "from $command_module import ";
  print FH $file2modules{$command_module_file};
  print FH "\n";
}

print FH "\nasync def LEG(m:List[str], message:discord.Message)->None:\n    if (len(m) > 1) and (m[1] in globals()) and (str(globals()[m[1]])[:9] == '<function'):\n        await globals()[m[1]](m, message)";
close FH;