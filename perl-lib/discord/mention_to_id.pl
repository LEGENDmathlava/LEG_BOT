#!/usr/bin/perl
use strict;
use warnings;
use utf8;
use open IN  => ":utf8";
use open OUT => ":utf8";
use open IO => ":utf8";

while (my $line = <STDIN>) {
    $line =~ s/<@!?(\d+)>/$1/eg;
    print $line;
}