function KEY(s) { return "\""s"\": " }
function VALUE(s) { return "\""s"\"," }
function REG(s) { gsub(/\"/, "\\\"", s); gsub(/\[/, "\\[", s); gsub(/\]/, "\\]", s); return s }

BEGIN{
   i=0

   reg[i]="szCountNo=[(.*)]"
   key[i++]="CountNo"

   reg[i]="Pan 1 = [(.*)]"
   key[i++]="Pan"

   reg[i]="MrchId = [(.*)]"
   key[i++]="MrchId"

   reg[i]="TermId = [(.*)]"
   key[i++]="TermId"

   reg[i]="Amount = [(.*)] DisAmount"
   key[i++]="Amount"

   reg[i]="RespCode = [(.*)]"
   key[i++]="RespCode"

   reg[i]="szRrn=[(.*)]"
   key[i++]="Rrn"

   reg[i]="Rrn = '(.*)'    AND ReversalFlag"
   key[i++]="Rrn"

   reg[i]="VoucherNo='(.*)'Result"
   key[i++]="VoucherNo"

   reg[i]="VoucherNo = '(.*)'    AND Rrn"
   key[i++]="VoucherNo"

   reg[i]="MisTraceNo ='(.*)'and CountNo"
   key[i++]="MisTraceNo"

   reg[i]="TransType[(.*)]"
   key[i++]="TransType"

   reg[i]="TransName[(.*)]"
   key[i++]="TransName"

   reg[i]="szBuf=[(.*)]"
   key[i++]="szBuf"

   reg[i]="TXN complete! [(.*)]"
   key[i++]="Result"

   reg[i]="PROC_MSG: AbcBatchNo=[(.*)],"
   key[i++]="abcbatchno"

   reg[i]=",AbcTraceNo=[(.*)],"
   key[i++]="abctraceno"

   reg[i]=",AbcVoucherNo=[(.*)]"
   key[i++]="abcvoucherno"

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
