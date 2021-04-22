#!/usr/bin/perl
use strict;
use warnings;
use utf8;
use open IN  => ":utf8";
use open OUT => ":utf8";
use open IO => ":utf8";

open FH, '>', "my_commands/LEG_commands/source.py";
print FH "# source";
close FH;

my @command_module_files = grep {$_ ne "my_commands/LEG_commands/__init__.py" and $_ ne "my_commands/LEG_commands/source.py"} (glob "my_commands/LEG_commands/*.py");
my @functions;
my %function2file;

foreach my $command_module_file (@command_module_files) {
  open IN, '<', $command_module_file;
  my $functions_line = <IN>;
  $functions_line =~ s/\x0D?\x0A?$//;
  my @temp = split / /, (substr $functions_line, 2, ((length $functions_line) - 1));
  foreach my $function (@temp) {
      $function2file{$function} = $command_module_file;
  }
  @functions = (@functions, @temp);
  close IN;
}

open FH, '>', "my_commands/LEG_commands/source.py";
print FH "# source\nimport discord\nfrom typing import Dict, List\nfunction2file: Dict[str, str] = {\n";
foreach my $function  (@functions) {
    print FH "    '$function': '$function2file{$function}',\n";
}
print FH "    'source': 'my_commands/LEG_commands/source.pl',\n";
print FH "}\n\n\nasync def source(m: List[str], message: discord.Message) -> None:\n    if len(m) == 2 or m[2] not in function2file:\n        await message.channel.send('https://github.com/LEGENDmathlava/LEG_BOT')\n    else:\n        await message.channel.send('https://github.com/LEGENDmathlava/LEG_BOT/blob/master/' + function2file[m[2]])\n";
close FH;
print "complete" . __FILE__ ."\n"