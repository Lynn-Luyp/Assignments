VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "SuperSheets"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Sub Sdelete(str As String)
Dim sht As Worksheet
    For Each sht In Sheets
        If sht.Name = str Then
            Application.DisplayAlerts = False
            sht.Delete
            Application.DisplayAlerts = True
        End If
    Next
End Sub


Sub Sadd(str As String)
Dim sht, sht1 As Worksheet
    For Each sht In Sheets
        If sht.Name = str Then
            k = k + 1
        End If
    Next
    
    If k = 0 Then
        Set sht1 = Sheets.Add
        sht1.Name = str
    End If

End Sub


Sub Add()

Sheets.Add after:=Sheets(Sheets.Count)



End Sub


Property Get Scount()

Scount = Sheets.Count
End Property



