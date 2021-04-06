/*Settings
1. Aldec Riviera Pro 2020.04
2. Open EPWave after run if not
*/
`timescale 1ns/1ns
module wire_and_or_test();
  // constants
  
  // general purpose registers
  reg A,B;
   
  // wires
  wire COut;
  wire DOut;
  wire EOut;

  // assign statements (if any)
  wire_and_or uut(
    .A(A),
    .B(B),
    .C(COut),
    .D(DOut),
    .E(EOut)
  );

  initial    
  begin
    A=1'b0; //A=0
    B=1'b0; //B=0
    #100;
    A=1'b1; //A=0
    B=1'b0; //B=1
    #100;
    A=1'b0; //A=1
    B=1'b1; //B=0
    #100;
    A=1'b1; //A=1
    B=1'b1; //B=1
  end 
    
  initial 
  begin
    $display("Starting Testbench...");
    #500;
    $stop;
    $finish();
  end

  initial 
  begin
    // Required to dump signals to EPWave
    $dumpfile("dump.vcd");
    $dumpvars(0);
  end
endmodule