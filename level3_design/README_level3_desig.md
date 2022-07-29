# ALU Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes in 2  8-bit input (*A*,*B*), one 4-bit select line input *ALU-Sel* for selecting the operation and 2 output (*ALU_Out*, *CarryOut*)

The values are assigned to the input port using 
```
    dut.A.value = 20
    dut.B.value = 10
    dut.ALU_Sel.value = 1
```

The assert statement is used for comparing the ALU's outut to the expected value.

The following error is seen:
```
 assert dut.ALU_Out.value == A1-B1, "ALU Subtractor result is incorrect: {A1} - {B1} != {ALU_Out}, expected value={EXP}".format(A1=int(dut.A.value), 
 B1=int(dut.B.value), ALU_Out=int(dut.ALU_Out.value), EXP=A1-B1)
                     AssertionError: ALU Subtractor result is incorrect: 20 - 10 != 30, expected value=10

```
## Test Scenario **(Important)**
- Test Inputs: A=20 B = 10 sel=1
- Expected Output: out=10         -------subtraction should be done 
- Observed Output in the DUT dut.ALU_out=30    ------------addition happens 

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following by inserting a bug in the design  

```
   always @(*)
    begin
        case(ALU_Sel)
        4'b0000: // Addition
           ALU_Result = A + B ; 
        4'b0001: // Subtraction
           ALU_Result = A + B ;        ====> BUG: Subtraction should be A - B. But here it is A + B 
        4'b0010: // Multiplication
           ALU_Result = A * B;
        4'b0011: // Division
           ALU_Result = A/B;
        4'b0100: // Logical shift left
           ALU_Result = A<<1;
         4'b0101: // Logical shift right
           ALU_Result = A>>1;
         4'b0110: // Rotate left
           ALU_Result = {A[6:0],A[7]};
         4'b0111: // Rotate right
           ALU_Result = {A[0],A[7:1]};
          4'b1000: //  Logical and 
           ALU_Result = A & B;
          4'b1001: //  Logical or
           ALU_Result = A | B;
          4'b1010: //  Logical xor 
           ALU_Result = A ^ B;
          4'b1011: //  Logical nor
           ALU_Result = ~(A | B);
          4'b1100: // Logical nand 
           ALU_Result = ~(A & B);
          4'b1101: // Logical xnor
           ALU_Result = ~(A ^ B);
          4'b1110: // Greater comparison
           ALU_Result = (A>B)?8'd1:8'd0 ;
          4'b1111: // Equal comparison   
            ALU_Result = (A==B)?8'd1:8'd0 ;
          default: ALU_Result = A + B ; 
        endcase
     
      
                                            
     
```
For the ALU design, the case  ``4'b0001: // Subtraction ``include should be ` ALU_Result = A - B ;`` in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

```
     -.--ns INFO     cocotb.gpi                         ..mbed/gpi_embed.cpp:76   in set_program_name_in_venv        Did not detect Python virtual environment. Using system-wide Python interpreter
     -.--ns INFO     cocotb.gpi                         ../gpi/GpiCommon.cpp:99   in gpi_print_registered_impl       VPI registered
     0.00ns INFO     Running on Icarus Verilog version 11.0 (stable)
     0.00ns INFO     Running tests with cocotb v1.6.2 from /workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb
     0.00ns INFO     Seeding Python random module with 1658913681
     0.00ns WARNING  Pytest not found, assertion rewriting will not occur
     0.00ns INFO     Found test alu_test.alu_test
     0.00ns INFO     running alu_test (1/1)
     2.00ns INFO     alu_test passed
     2.00ns INFO     **************************************************************************************
                     ** TEST                          STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     **************************************************************************************
                     ** alu_test.alu_test              PASS           2.00           0.00       2950.02  **
                     **************************************************************************************
                     ** TESTS=1 PASS=1 FAIL=0 SKIP=0                  2.00           0.01        264.32  **
                     **************************************************************************************
                     
     make[1]: Leaving directory '/workspace/challenges-sameeryada/level3_design'
```

The updated design is checked in as alu.v


## Verification Strategy
 We correct the inserted bug A - B
## Is the verification complete ?
Yes
