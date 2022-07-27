# See LICENSE.cocotb for details
# See LICENSE.vyoma for details

# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def alu_test(dut):
    """Test for 20 - 10"""

    A1 = 20
    B1 = 10
    SEL1 = 1

    # input driving
    dut.A.value = A1
    dut.B.value = B1
    dut.ALU_Sel.value = B1

    await Timer(2, units='ns')

    assert dut.ALU_Result.value == A1+B1, f"Subtractor result is incorrect: {dut.X.value} != 10"
