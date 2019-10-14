function doPost(e) {
  var params = e.parameter;
  var url = params.url;  
  var name = params.name;  
  var range = params.range; 

  var SpreadSheet = SpreadsheetApp.openByUrl(url);
  var SheetName = SpreadSheet.getSheetByName(name)
  var range = SheetName.getRange(range);
  
  range.setValues([[1,2,3],[11,22,33],[111,222,333]]);
  
  return ContentService.createTextOutput("成功!");
}

function myFunction(e)
{
  doPost(e)
}
