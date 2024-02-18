module wire_and_or(A,B,C,D,E);
  input A, B;
  output C, D, E;
  wire An;
  wand D;
  wor E;
  
  //wire
  assign An = ~A;
  assign C = An & B;
  
  //wire-and
  assign D = A;
  assign D = B;
  
  //wire-or
  assign E = A;
  assign E = B;
  
endmodule