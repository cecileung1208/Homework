
Sub Reset():

Dim ws As Worksheet

For Each ws In ActiveWorkbook.Worksheets
ws.Activate


  Range("J1:Q10000").Value = ""
  Range("K1:K10000").Interior.ColorIndex = 0
  

Next ws

End Sub
