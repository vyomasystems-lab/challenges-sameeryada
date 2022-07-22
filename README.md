# challenges-sameeryada
challenges-sameeryada created by GitHub Classroom
## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained.
The test drives inputs to the Design Under Test (mux module here) which takes in 2-bit inputs *inp30* (for input 31) and 5 bit select line *sel* (for select line) and gives 2-bit output *out*
The values are assigned to the input port using
```
dut.inp30.value = 2
dut.sel.value = 30

```
The assert statement is used for comparing the mux's outut to the expected value.
The following error is seen:
```

```
## Test Scenario **(Important)**

- Test Inputs: a=2 b=30
- Expected Output: out=2
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug

Based on the above test input and analysing the design, we see the following
```
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
      5'b11110: out = inp30;             ---> BUG: THIS CASE WAS NOT DEFINED 

      default: out = 0;
    endcase
  end
```
For the mux design, the logic should also include  5'b11110: out = inp30; in the design code

## Design Fix
Updating the design and re-running the test makes the test pass.

The updated design is checked in as mux_fix.v

## Verification Strategy

Including the missing case pass the test

## Is the verification complete ?
Yes

