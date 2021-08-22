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
  my @temp = split / /, (substr $functions_line, 2, ((length $functions_line) - 1));
  $file2modules{$command_module_file} = join(', ', @temp);
  @functions = (@functions, @temp);
  close IN;
}

@functions = grep {$_ =~ /^(?!.*_command$).*$/} @functions;

open FH, '>', "my_command.py";
print FH "import discord\nimport subprocess\nfrom typing import List, Dict, Callable, Coroutine, Any\n";
foreach my $command_module_file (@command_module_files){
  my $command_module = $command_module_file;
  $command_module =~ s/\//./g;
  $command_module =~ s/.py$//;
  print FH "from $command_module import ";
  print FH $file2modules{$command_module_file};
  print FH "\n";
}

print FH "\ncommands_dict: Dict[str, Callable[[List[str], discord.Message], Coroutine[Any, Any, None]]] = {\n";
foreach my $function (@functions){
  print FH "    '$function': $function,\n";
}
print FH "}\n";

print FH "\n\nasync def my_command(message: discord.Message) -> None:\n    p = subprocess.Popen(['./perl-lib/discord/mention_to_id.pl'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)\n    out, error = p.communicate(input=message.content.encode('utf-8'))\n    message.content = out.decode('utf-8')\n    m = message.content.split()\n    if len(m) == 0:\n        return\n    if m[0] in commands_dict:\n        await commands_dict[m[0]](m, message)\n    await in_command(message)\n    await regex_command(message)\n";
close FH;
print "complete" . __FILE__ ."\n"