function doPost(e) {
  var params = e.parameter;
  var url = params.url;
  var name = params.name;
  var SpreadSheet = SpreadsheetApp.openByUrl(url);
  var SheetName = SpreadSheet.getSheetByName(name);
  var d = params.data;   // 原始 data，字串格式
  var row = params.row;  // 由原始 data 判斷需要插入幾列
  var column = params.column; // 由原始 data 判斷每一列有幾欄
  var insertType = params.insertType;  // 插入在上方，或插入在下方
  var lastRow = SheetName.getLastRow();  // 讀取最後一列的列數
  var range, data, arr;

  if(d.indexOf(',')!=-1){
    arr = d.split(','); // 把原始資料用 , 分割成陣列
    data=[];
    for(var i=0; i<row; i++){
      data[i]=[];
      for(var j=0; j<column; j++){
        data[i].push(arr[i*column+j]); // 藉由 row 和 column 變成二維陣列
      }
    }
  }else{
    data = [[d]];
  }

  if(insertType=='top'){
    SheetName.insertRowsBefore(1,row);
    range = SheetName.getRange(1,1,row,column);
  }else if(insertType=='bottom'){
    range = SheetName.getRange(lastRow+1,1,row,column);
  }

  range.setValues(data);

  return ContentService.createTextOutput(true);
}

function myFunction(e) {
  doPost(e)
}
