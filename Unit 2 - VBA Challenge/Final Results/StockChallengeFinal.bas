Sub StockChallange():

Dim MaxPercentTicker As String
Dim MinPercentTicker As String
Dim MaxVolumeTicker As String
Dim MaxPercentValue As Double
Dim MinPercentValue As Double
Dim MaxStockVolume As Double
Dim SummaryLastRow As Long
Dim ws As Worksheet

For Each ws In ActiveWorkbook.Worksheets
ws.Activate

ws.Range("P1").Value = "Ticker"
ws.Range("Q1").Value = "Value"
ws.Range("O2").Value = "Maximum % Change"
ws.Range("O3").Value = "Minimum % Change"
ws.Range("O4").Value = "Maximum Stock Volume"


ws.Range("P1:Q1").Font.Bold = True
ws.Range("O2:O4").Font.Bold = True

MaxPercentTicker = ws.Cells(2, 10).Value
MinPercentTicker = ws.Cells(2, 10).Value
MaxVolumeTicker = ws.Cells(2, 10).Value
MaxPercentValue = ws.Cells(2, 12).Value
MinPercentValue = ws.Cells(2, 12).Value
MaxStockVolume = ws.Cells(2, 13).Value
SummaryLastRow = ws.Cells(Rows.Count, 10).End(xlUp).Row


  For k = 2 To SummaryLastRow
  
        
        If ws.Cells(k, 12) > MaxPercentValue Then
        MaxPercentValue = ws.Cells(k, 12).Value
        MaxPercentTicker = ws.Cells(k, 10).Value

        ElseIf ws.Cells(k, 12) < MinPercentValue Then
        MinPercentValue = ws.Cells(k, 12).Value
        MinPercentTicker = ws.Cells(k, 10).Value
        End If

        If ws.Cells(k, 13) > MaxStockVolume Then
        MaxStockVolume = ws.Cells(k, 13).Value
        MaxVolumeTicker = ws.Cells(k, 10).Value
        

    End If
    
    
    ws.Range("P2").Value = MaxPercentTicker
    ws.Range("Q2").Value = MaxPercentValue
    ws.Range("Q2").Value = FormatPercent(MaxPercentValue, 2)
    ws.Range("P3").Value = MinPercentTicker
    ws.Range("Q3") = MinPercentValue
    ws.Range("Q3").Value = FormatPercent(MinPercentValue, 2)
    ws.Range("P4") = MaxVolumeTicker
    ws.Range("Q4") = MaxStockVolume
    
Next k
Next ws
    
End Sub

