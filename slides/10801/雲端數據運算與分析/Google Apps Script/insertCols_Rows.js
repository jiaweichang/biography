function doPost(e) {
  var params = e.parameter;
  var url = params.url;  
  var name = params.name;  
  
  var colIndex = (!params.colIndex)?0:params.colIndex; // 如果沒有 colIndex，就讓 colIndex=0
  var numCols = (!params.numCols)?1:params.numCols;    // 如果沒有 numCols，就讓 numCols=1
  var rowIndex = (!params.rowIndex)?0:params.rowIndex; // 如果沒有 rowIndex，就讓 rowIndex=0
  var numRows = (!params.numRows)?1:params.numRows;    // 如果沒有 numRows，就讓 numRows=1

  var SpreadSheet = SpreadsheetApp.openByUrl(url);
  var SheetName = SpreadSheet.getSheetByName(name)
  
  if(colIndex > 0 && numCols > 0)
    SheetName.insertColumns(colIndex,numCols);
  
  if(rowIndex > 0 && numRows > 0)
    SheetName.insertRows(rowIndex,numRows);
  
  return ContentService.createTextOutput("成功!");
}

function myFunction(e)
{
  doPost(e)
}
