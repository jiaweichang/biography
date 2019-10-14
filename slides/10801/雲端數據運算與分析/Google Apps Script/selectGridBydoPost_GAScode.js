function doPost(e) {
  var params = e.parameter;
  var url = params.url;  
  var name = params.name;  
  var startRow = params.startRow; 
  var startColumn = params.startColumn; 
  var endRow = (!params.endRow)?1:params.endRow; // 如果沒有 endRow，就讓 endRow=1
  var endColumn = (!params.endRow)?1:params.endColumn;  // 如果沒有 endColumn，就讓 endColumn=1
  var SpreadSheet = SpreadsheetApp.openByUrl(url);
  var SheetName = SpreadSheet.getSheetByName(name);
  var data = SheetName.getSheetValues(startRow,startColumn,endRow,endColumn);
  //Logger.log(data);
  return ContentService.createTextOutput(data); // 將資料透過 ContentService 拋出
}

function myFunction(e)
{
  doPost(e)
}
