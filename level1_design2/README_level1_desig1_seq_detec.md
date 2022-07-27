# Sequence Detector Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (seq_detect_1011 module here) which takes in 1-bit input (*inp_bit*), *reset*, *clk* and gives 1 when sequence is seen using signal (*seq_seen*)

The values are assigned in testbench to the input port using 
```
Sequence Test Case- 1  = 11011
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
 Sequence Test Case- 2 = 101011
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)

```

The assert statement is used for comparing the sequence detector's (1011) outut to the expected value.

The following error is seen:
For Sequence Test Case- 1  = 11011
```
                     Traceback (most recent call last):
                       File "/workspace/challenges-sameeryada/level1_design2/test_seq_detect_1011.py", line 54, in test_seq_bug1
                         assert dut.seq_seen.value == 1, f'Sequence must be detected but is not detected. Given sequence = 11011. Model Output: {dut.seq_seen.value} Expected Ouput: 1'
                     AssertionError: Sequence must be detected but is not detected. Given sequence = 11011. Model Output: 0 Expected Ouput: 1
 65000.00ns INFO     ********************************************************************************************
                     ** TEST                                STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     ********************************************************************************************
                     ** test_seq_detect_1011.test_seq_bug1   FAIL       65000.00           0.00   20366783.52  **
                     ********************************************************************************************
                     ** TESTS=1 PASS=0 FAIL=1 SKIP=0                    65000.00           0.02    3325807.75  **
                     ********************************************************************************************

```
For Sequence Test Case- 2  = 101011
```
 75000.00ns INFO     test_seq_bug1 failed
                     Traceback (most recent call last):
                       File "/workspace/challenges-sameeryada/level1_design2/test_seq_detect_1011.py", line 54, in test_seq_bug1
                         assert dut.seq_seen.value == 1, f'Sequence must be detected but is not detected. Given sequence = 101011. Model Output: {dut.seq_seen.value} Expected Ouput: 1'
                     AssertionError: Sequence must be detected but is not detected. Given sequence = 101011. Model Output: 0 Expected Ouput: 1
 75000.00ns INFO     ********************************************************************************************
                     ** TEST                                STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     ********************************************************************************************
                     ** test_seq_detect_1011.test_seq_bug1   FAIL       75000.00           0.00   28144654.58  **
                     ********************************************************************************************
                     ** TESTS=1 PASS=0 FAIL=1 SKIP=0                    75000.00           0.02    3973885.85  **
                     ********************************************************************************************
                     
make[1]: Leaving directory '/workspace/challenges-sameeryada/level1_design2'
```
## Test Scenario **(Important)**
- Test Inputs: case-1 ===> 11011  , case-2 ===> 101011
- Expected Output: case-1 ===> seq_seen= 1, case-2 ===> seq_seen= 1
- Observed Output in the DUT case-1 ===> dut.seq_seen.value = 0, case-2 ===> dut.seq_seen.value = 0

Output sequence mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

that for overlapping sequence the seq_detect_1011 is unable to give detect output
```

 
     
     
                                              ====> BUG: for overlapping sequence the seq_detect_1011 is unable to give detect output
      
```

## Design Fix
Updating the design by including overlapping case and re-running the test makes the test pass.
For Sequence Test Case- 1  = 11011
```
    0.00ns WARNING  Pytest not found, assertion rewriting will not occur
     0.00ns INFO     Found test test_seq_detect_1011.test_seq_bug1
     0.00ns INFO     running test_seq_bug1 (1/1)
 15000.00ns INFO     Input bit: z
 15000.00ns INFO     #### CTB: Develop your test here! ######
 65000.00ns INFO     test_seq_bug1 passed
 65000.00ns INFO     ********************************************************************************************
                     ** TEST                                STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     ********************************************************************************************
                     ** test_seq_detect_1011.test_seq_bug1   PASS       65000.00           0.00   32815330.31  **
                     ********************************************************************************************
                     ** TESTS=1 PASS=1 FAIL=0 SKIP=0                    65000.00           0.01    4829066.25  **
                     ********************************************************************************************
                     
make[1]: Leaving directory '/workspace/challenges-sameeryada/level1_design2'
```
For Sequence Test Case- 2  = 101011
```
 0.00ns WARNING  Pytest not found, assertion rewriting will not occur
     0.00ns INFO     Found test test_seq_detect_1011.test_seq_bug1
     0.00ns INFO     running test_seq_bug1 (1/1)
 15000.00ns INFO     Input bit: z
 15000.00ns INFO     #### CTB: Develop your test here! ######
 75000.00ns INFO     test_seq_bug1 passed
 75000.00ns INFO     ********************************************************************************************
                     ** TEST                                STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     ********************************************************************************************
                     ** test_seq_detect_1011.test_seq_bug1   PASS       75000.00           0.00   33095508.07  **
                     ********************************************************************************************
                     ** TESTS=1 PASS=1 FAIL=0 SKIP=0                    75000.00           0.01    5597580.06  **
                     ********************************************************************************************
                     
make[1]: Leaving directory '/workspace/challenges-sameeryada/level1_design2'
```
The updated design is checked in as seq_detect_1011_withoutbug.v

## Verification Strategy
 We change the code by including case for overlapping sequence.
## Is the verification complete ?
Yes
