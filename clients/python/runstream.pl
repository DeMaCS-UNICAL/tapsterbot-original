
while(<>)
{
   chomp;	
   
   print "GOT $_\n";
   if (/COORD: (.*)/)
   {
        print "EXEC $1\n";
        print qx{python client.py --url http://127.0.0.1 --light 'swipe $1'};
   }
}
