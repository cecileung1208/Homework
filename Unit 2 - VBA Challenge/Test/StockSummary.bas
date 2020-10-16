
Sub StockSummary():


Dim Ticker As String
Dim StartPrice As Double
Dim EndPrice As Double
Dim PriceChange As Double
Dim PercentChange As Double
Dim StockVolume As Double
Dim SummaryTableRow As Long
Dim StartRow As Long
Dim LastRow As Long
Dim SummaryLastRow As Long
Dim ws As Worksheet

For Each ws In ActiveWorkbook.Worksheets
ws.Activate

ws.Range("J1").Value = "Stock Ticker"
ws.Range("K1").Value = "Price Change"
ws.Range("L1").Value = "% Change"
ws.Range("M1").Value = "Stock Volume"

ws.Range("J1:M1").Font.Bold = True

StockVolume = 0
SummaryTableRow = 2
StartRow = 2
LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
StartPrice = 0
EndPrice = 0
PriceChange = 0
PercentChange = 0


For i = 2 To LastRow
    If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
        Ticker = ws.Cells(i, 1).Value
        StartPrice = StartPrice + ws.Cells(StartRow, 3).Value
        EndPrice = EndPrice + ws.Cells(i, 6).Value
        PriceChange = EndPrice - StartPrice
        
            If ws.Cells(i, 3) = 0 Then
            PercentChange = PriceChange / 1
        
            Else
            PercentChange = PriceChange / StartPrice
            End If
            
        StockVolume = StockVolume + ws.Cells(i, 7).Value
        
        ws.Range("J" & SummaryTableRow).Value = Ticker
        SummaryLastRow = ws.Cells(Rows.Count, 10).End(xlUp).Row
        
        ws.Range("K" & SummaryTableRow).Value = PriceChange
        
         For j = 2 To SummaryLastRow
         
            If ws.Cells(j, 11).Value > 0 Then
            ws.Cells(j, 11).Interior.ColorIndex = 4
            ElseIf ws.Cells(j, 11).Value < 0 Then
            ws.Cells(j, 11).Interior.ColorIndex = 3
            Else
            ws.Cells(j, 11).Interior.ColorIndex = 0
            End If
          Next j
        
        ws.Range("L" & SummaryTableRow).Value = PercentChange
        ws.Range("L" & SummaryTableRow).Value = FormatPercent(PercentChange, 2)
        ws.Range("M" & SummaryTableRow).Value = StockVolume
        
        SummaryTableRow = SummaryTableRow + 1
        StartRow = i + 1
        
        StartPrice = 0
        EndPrice = 0
        PriceChange = 0
        PercentChange = 0
        StockVolume = 0
        
    Else
    StockVolume = StockVolume + ws.Cells(i, 7).Value
    
    End If
    
    Next i
    
    Next ws
    
    
End Sub
