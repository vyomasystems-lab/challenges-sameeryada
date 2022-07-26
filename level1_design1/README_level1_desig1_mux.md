# Adder Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*

![](https://i.imgur.com/miWGA1o.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes in 2-bit input *inp0-inp30* and 5-bit select line *sel* and gives 2-bit output *out* based on select line *sel*

The values are assigned to the input port using 
```
dut.inp30.value = 2
dut.sel.value = 30
```

The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
```
 assert dut.out.value == A_inp30, "MUX result is incorrect: {A_inp30} != {OUT}, expected value={EXP}".format(A_inp30=int(dut.inp30.value), 
 B_sel=int(dut.sel.value), OUT=int(dut.out.value), EXP=A_inp30)
     AssertionError: MUX result is incorrect: 2 != 0, expected value=2

```
## Test Scenario **(Important)**
- Test Inputs: inp30=2 sel=30
- Expected Output: out=2
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 always @(a or b) 
  begin
    sum = a - b;             ====> BUG
  end
  begin
    case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12;
      5'b01101: out = inp13;
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
                                              ====> BUG: No case defined for input 30 so default case is running i.e 0 output
      default: out = 0;
    endcase
```
For the mux design, the case include should be ``5'b11110: out = inp30;`` in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

```
 -.--ns INFO     cocotb.gpi                         ..mbed/gpi_embed.cpp:76   in set_program_name_in_venv        Did not detect Python virtual environment. Using system-wide Python interpreter
     -.--ns INFO     cocotb.gpi                         ../gpi/GpiCommon.cpp:99   in gpi_print_registered_impl       VPI registered
     0.00ns INFO     Running on Icarus Verilog version 11.0 (stable)
     0.00ns INFO     Running tests with cocotb v1.6.2 from /workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb
     0.00ns INFO     Seeding Python random module with 1658823175
     0.00ns WARNING  Pytest not found, assertion rewriting will not occur
     0.00ns INFO     Found test test_mux.test_mux
     0.00ns INFO     running test_mux (1/1)
     2.00ns INFO     ##### CTB: Develop your test here ########
     2.00ns INFO     test_mux passed
     2.00ns INFO     **************************************************************************************
                     ** TEST                          STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     **************************************************************************************
                     ** test_mux.test_mux              PASS           2.00           0.00       3755.17  **
                     **************************************************************************************
                     ** TESTS=1 PASS=1 FAIL=0 SKIP=0                  2.00           0.01        307.86  **
                     **************************************************************************************
                     
make[1]: Leaving directory '/workspace/challenges-sameeryada/level1_design1'
```

The updated design is checked in as mux_withoutbuggy.v

## Verification Strategy
 We include the missing test case and mux perfrom as expected
## Is the verification complete ?
Yes
