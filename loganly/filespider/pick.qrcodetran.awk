function KEY(s) { return "\""s"\": " }
function VALUE(s) { return "\""s"\"," }
function REG(s) { gsub(/\"/, "\\\"", s); gsub(/\[/, "\\[", s); gsub(/\]/, "\\]", s); return s }

BEGIN{
   i=0
   reg[i]="ChannelNo:(.*)"
   key[i++]="ChannelNo"

   reg[i]="CountNo=[(.*)]"
   key[i++]="CountNo"

   reg[i]="TermId=[(.*)]"
   key[i++]="TermId"

   reg[i]="金额[(.*)]"
   key[i++]="Amount"

#   reg[i]="\"auth_code\":\t*\"(.*)\","   ## TODO 更精确
#   key[i++]="AuthCode"

#   reg[i]="\"orderid\":\t*\"(.*)\","   ## TODO 更精确
#   key[i++]="OrderId"

}
{
   for ( idx in reg ){
     a[1]=""
     if ( match($0, REG(reg[idx]), a) )
       print KEY(key[idx]) VALUE(a[1]) 
   } 
   if ( match($0, /buf\[{(.*)}\]/,a))
   {
     print a[1]","
   }

   if ( match($0, /TransType\[(.*)\].*TransName\[(.*)\]/,a))
   {
     print KEY("TransType") VALUE(a[1]) 
     print KEY("TransName") VALUE(a[2]) 
   }

   if ( match($0, /RespCode = '(.*)' Result = '(.*)'AbcTraceNo = '([0-9]*)'.*AbcBatchNo = '([0-9]*)'.*AbcVoucherNo = '([0-9]*)'/, a))
   {
     i=1
     print KEY("RespCode") VALUE(a[i++]) 
     print KEY("Result") VALUE(a[i++]) 
     print KEY("AbcTraceNo") VALUE(a[i++]) 
     print KEY("AbcBatchNo") VALUE(a[i++]) 
     print KEY("AbcVoucherNo") VALUE(a[i++]) 
   }

}
END{
   print "\"FileName\":\""FILENAME"\""
}
