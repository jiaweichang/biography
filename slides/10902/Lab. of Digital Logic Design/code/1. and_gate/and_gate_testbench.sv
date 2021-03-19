/*Settings
1. Aldec Riviera Pro 2020.04
2. Open EPWave after run if not
*/
`timescale 1ns/1ns
module and_test();
  // constants
  
  // general purpose registers
  reg A,B;
   
  // wires
  wire Out;

  // assign statements (if any)
  and_gate uut(
    .A(A),
    .B(B),
    .O(Out)
  );

  initial    
  begin
    A=1'b0; //A=0
    B=1'b0; //B=0
    #20;
    A=1'b0; //A=0
    B=1'b1; //B=1
    #20;
    A=1'b1; //A=1
    B=1'b0; //B=0
    #20;
    A=1'b1; //A=1
    B=1'b1; //B=1
  end 
    
  initial 
  begin
    $display("Starting Testbench...");
    #100;
    $finish();
  end

  initial 
  begin
    // Required to dump signals to EPWave
    $dumpfile("dump.vcd");
    $dumpvars(0);
  end
endmodule