#!/usr/bin/perl
use strict;
use warnings;
use utf8;
use open IN  => ":utf8";
use open OUT => ":utf8";
use open IO => ":utf8";

my @command_module_files = grep {$_ ne "reaction_commands/__init__.py"} (glob "reaction_commands/*.py");
my @functions;
my %func2str;
my %file2function;
foreach my $command_module_file (@command_module_files){
  open IN, '<', $command_module_file;
  my $functions_line = <IN>;
  $functions_line =~ s/\x0D?\x0A?$//;
  $functions_line =~ s/^# //;
  $file2function{$command_module_file} = $functions_line;
  my $str = <IN>;
  $str =~ s/\x0D?\x0A?$//;
  $str =~ s/^# //;
  $func2str{$functions_line} = $str;
  @functions = (@functions, $functions_line);
  close IN;
}
open FH, '>', "reaction_command.py";
print FH "import discord\nfrom typing import Union\n";
foreach my $command_module_file (@command_module_files){
  my $command_module = $command_module_file;
  $command_module =~ s/\//./g;
  $command_module =~ s/.py$//;
  print FH "from $command_module import $file2function{$command_module_file}\n";
}

print FH "\n\nasync def reaction_command(\n        reaction: discord.Reaction,\n        user: Union[discord.Member, discord.User]) -> None:\n";
foreach my $function (@functions){
  my $str2 = $func2str{$function};
  print FH "    if reaction.emoji == ${str2}:\n";
  print FH "        await ${function}(reaction, user)\n";

}
close FH;
print "complete" . __FILE__ ."\n"