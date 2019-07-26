function ltrim(s) { sub(/^[ \t\r\n]+/, "", s); return s }
function rtrim(s) { sub(/[ \t\r\n]+$/, "", s); return s }
function trim(s) { return rtrim(ltrim(s)); }

BEGIN{ FS="]|-" }
{
  if (!($2 ~/^$/))
  {
    pid=ltrim($2)
    if (pid ~/^[0-9]+$/) 
    {
       filename=outputdir"/"date"-"pid".txt"
       print $0 >> filename
    }
  }
}
