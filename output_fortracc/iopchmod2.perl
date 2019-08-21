#!/usr/bin/perl 

#use Cwd;

  open (FR, "./file.list");


  while (<FR>) {

   chomp;
   $fname = $_; 
print "fname is $fname\n\n";
print "=======================\n";

#    $chdircmd = "cd ".$dirname;
#    print "chdircmd is $chdircmd \n\n";
#    system("$chdircmd"); 

    system("/bin/pwd");

#   if !($haveyydir) {
   if ($haveyydir == 0) {
    $chmodcmd = "/bin/chmod 664 ".$fname;
    print "chmodcmd is -->$chmodcmd<-- \n\n";
#    system("$chmodcmd"); 
   }

#   system("/bin/sleep 30");

    $chdircmd = "cd ..";
    print "chdircmd is $chdircmd \n\n";
    system("$chdircmd");


  }

