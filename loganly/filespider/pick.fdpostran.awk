function KEY(s) { return "\""s"\": " }
function VALUE(s) { return "\""s"\"," }
function REG(s) { gsub(/\"/, "\\\"", s); gsub(/\[/, "\\[", s); gsub(/\]/, "\\]", s); return s }

BEGIN{
   i=0

   reg[i]="nMsgType = [(.*)]"
   key[i++]="msgtype"

   reg[i]="cOriginal = [(.*)]"
   key[i++]="original"

   reg[i]="RN = (.*)"
   key[i++]="room"

   reg[i]="DA = (.*)"
   key[i++]="date"

   reg[i]="TI = (.*)"
   key[i++]="transtime"

   reg[i]="WS = (.*)"
   key[i++]="workid"

   reg[i]="WorkId=[(.*)],Trans->szPinpadIp"
   key[i++]="workid"

   reg[i]="AbcMrchId =[(.*)],"
   key[i++]="mrchid"

   reg[i]="AbcTermId =[(.*)]"
   key[i++]="termid"

   reg[i]="begin pack DE 2:(.*)"
   key[i++]="pan"

   reg[i]="Amount = (.*) where"
   key[i++]="amount"

   reg[i]="RespCode =[(.*)],"
   key[i++]="respcode"

   reg[i]="complete ... [(.*)]"
   key[i++]="result"
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
