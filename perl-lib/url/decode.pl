#!/usr/bin/perl
use strict;
use warnings;
use utf8;
use open IN  => ":utf8";
use open OUT => ":utf8";
use open IO => ":utf8";

while (my $line = <STDIN>) {
    $line =~ s/%([0-9a-fA-F]{2})/chr(hex($1))/eg if $line =~ m/^<https?:\/\/\S+\.\S+>/;
    print $line;
}