VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Sheet1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Sub GetStats()

' Declare Variables
Dim stockTicker As String
Dim openingPrice As Double
Dim closingPrice As Double
Dim totalStockVolume As Double
Dim recordTickerRow As Integer
Dim LastRow As Double
Dim WorksheetName As String



For Each ws In Worksheets

    WorksheetName = ws.Name
    
    'Initialize Variables
    openingPrice = 0
    closingPrice = 0
    totalStockVolume = 0
    recordTickerRow = 2
    
   'Add Stat Row Titles and 1st row values
   ws.Cells(1, 12).Value = "Ticker"
   ws.Cells(1, 13).Value = "Yearly Change"
   ws.Cells(1, 14).Value = "Percent Change"
   ws.Cells(1, 15).Value = "Total Stock Volume"
   
   openingPrice = ws.Cells(2, 3).Value
   totalStockVolume = ws.Cells(2, 7)

    LastRow = ws.Cells(Rows.Count, "A").End(xlUp).Row

    
    
    ' Loop through data to get opening/closing prices and stock volume for each ticker
    For MyRow = 2 To LastRow
        
        If ws.Cells(MyRow - 1, 1).Value <> ws.Cells(MyRow, 1).Value Then
        
            openingPrice = ws.Cells(MyRow, 3)
            totalStockVolume = ws.Cells(MyRow, 7)

        
            'Ticker value
            ws.Cells(recordTickerRow, 12).Value = ws.Cells(MyRow, 1).Value
            ws.Cells(recordTickerRow, 14).Value = openingPrice
            
       
            
            recordTickerRow = recordTickerRow + 1
            
       Else
            closingPrice = ws.Cells(MyRow, 6)
            totalStockVolume = totalStockVolume + ws.Cells(MyRow, 7)
            ws.Cells(recordTickerRow - 1, 13).Value = closingPrice - openingPrice
            ws.Cells(recordTickerRow - 1, 14).Value = (closingPrice - openingPrice) / openingPrice
            ws.Cells(recordTickerRow - 1, 14).NumberFormat = "0.00%"
            ws.Cells(recordTickerRow - 1, 15).Value = totalStockVolume

        End If
    
    
        
    Next MyRow
    
    
    
    
    ' Summarize Data
    Dim Rng As Range
    Dim Rng2 As Range
    Dim MaxRow As Long
    Dim MaxVal As Double
    Dim MinRow As Long
    Dim MinVal As Double
    Dim MaxTotalRow As Long
    Dim MaxTotalVal As Double
    Dim LastSummaryRow As Double
    
    Set Rng = ws.Range("N:N")
    MaxVal = WorksheetFunction.Max(Rng)
    MinVal = WorksheetFunction.Min(Rng)
    
    Set Rng2 = ws.Range("O:O")
    MaxTotalVal = WorksheetFunction.Max(Rng2)

    LastSummaryRow = ws.Cells(Rows.Count, "N").End(xlUp).Row

    '  Loop through stat rows and to calc highest/lowest increase and total stock volume
    For sumRow = 2 To LastSummaryRow
    
        If StrComp(ws.Range("N" & sumRow).Value, MaxVal, vbTextCompare) = 0 Then
            MaxRow = sumRow
        End If
        
        If StrComp(ws.Range("N" & sumRow).Value, MinVal, vbTextCompare) = 0 Then
            MinRow = sumRow
        End If
        
        If StrComp(ws.Range("O" & sumRow).Value, MaxTotalVal, vbTextCompare) = 0 Then
            MaxTotalRow = sumRow
        End If
        
        'format Yearly Change Column 13
        If ws.Cells(sumRow, 13).Value >= 0 Then
              ' Set the Cell Colors to Green
                ws.Cells(sumRow, 13).Interior.ColorIndex = 4
        Else
            ' Set the Cell Colors to Red
            ws.Cells(sumRow, 13).Interior.ColorIndex = 3
        End If


        'format Percent Change Column 14
        If ws.Cells(sumRow, 14).Value >= 0 Then
              ' Set the Cell Colors to Green
                ws.Cells(sumRow, 14).Interior.ColorIndex = 4
        Else
            ' Set the Cell Colors to Red
            ws.Cells(sumRow, 14).Interior.ColorIndex = 3
        End If

    
    Next sumRow
    
    ws.Cells(2, 18).Value = "Greatest % Increase"
    ws.Cells(3, 18).Value = "Greatest % Decrease"
    ws.Cells(4, 18).Value = "Greated Total Volume"
    
    'MsgBox "Max Value was " & Str(MaxVal)
    'MsgBox "Matching Row was " & Str(MatchingRow)
    
    ws.Cells(1, 19).Value = "Ticker"
    ws.Cells(1, 20).Value = "Value"


    ws.Cells(2, 19).Value = ws.Cells(MaxRow, 12).Value
    ws.Cells(2, 20).Value = MaxVal
    ws.Cells(2, 20).NumberFormat = "0.00%"
    
    ws.Cells(3, 19).Value = ws.Cells(MinRow, 12).Value
    ws.Cells(3, 20).Value = MinVal
    ws.Cells(3, 20).NumberFormat = "0.00%"
    
    ws.Cells(4, 19).Value = ws.Cells(MaxTotalRow, 12).Value
    ws.Cells(4, 20).Value = MaxTotalVal
    ws.Cells(4, 20).NumberFormat = "0"
    
    'Resize new Column widths
    ws.Columns("L:R").EntireColumn.AutoFit

    
    
    'MsgBox "Done with Worksheet " & WorksheetName

Next ws

    


End Sub


