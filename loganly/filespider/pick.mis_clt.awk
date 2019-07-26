function KEY(s) { return "\""s"\": " }
function VALUE(s) { return "\""s"\"," }
function REG(s) { gsub(/\"/, "\\\"", s); gsub(/\[/, "\\[", s); gsub(/\]/, "\\]", s); return s }

BEGIN{
   i=0
   reg[i]="(.*) : test Connect"
   key[i++]="timepid"

   reg[i]="test Connect(.*)"
   key[i++]="test"

   reg[i]="connect(.*)"
   key[i++]="connect"


}
{
   for ( idx in reg ){
     a[1]=""
     if ( match($0, REG(reg[idx]), a) )
       print KEY(key[idx]) VALUE(a[1]) 
   } 

}
END{
   print "\"FileName\":\""FILENAME"\""
}
