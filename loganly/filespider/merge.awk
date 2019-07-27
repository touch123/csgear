function trimall(s) { gsub(/[ \t\r\n]+/, "", s); return s }
{
  if ( $0 ~/^\t.*$/ )
  {
     line=line""$0
  }
  else if ( $0 ~/^\}\].*$/ )
  {
     line=line""$0
  }
  else if ( $0 ~/^[0-9][0-9]:.*$/ )
  {
     match($0, /[0-9][0-9]:(.*)   \[/,a)
     line=line""trimall(a[1])
  }
  else
  {
     print line
     line=$0
  }
}
