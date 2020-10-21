function doPost(e) 
{ 
  var url = "https://docs.google.com/spreadsheets/d/17rOrO4bnvYjq0-AJbY0Y0OLdzGZPlN1DGCXehixfq9g/edit?usp=sharing";
  var SpreadSheet = SpreadsheetApp.openByUrl(url);
  var SheetName = SpreadSheet.getSheetByName('testSheet'); //工作表名稱
  
  var param = e.parameter;
  var row = param.row;
  var col = param.col;
  
  var replyMsg = SheetName.getSheetValues(row,col,1,1);   // 取得 A1 數值  
  return ContentService.createTextOutput(replyMsg);
}

function myFunction(e) {

  doPost(e)

}
