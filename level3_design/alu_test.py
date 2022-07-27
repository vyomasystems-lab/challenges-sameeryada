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
    dut.ALU_Sel.value = SEL1

    await Timer(2, units='ns')

    #assert dut.ALU_Result.value == A1+B1, f"Subtractor result is incorrect: {dut.X.value} != 10"
    #assert dut.ALU_Out.value == A1+B1, "ALU Subtractor result is incorrect: {A_inp30} != {OUT}, expected value={EXP}".format(A_inp30=int(dut.inp30.value), B_sel=int(dut.sel.value), OUT=int(dut.out.value), EXP=A_inp30)
    assert dut.ALU_Out.value == A1-B1, "ALU Subtractor result is incorrect: {A1} - {B1} != {ALU_Out}, expected value={EXP}".format(A1=int(dut.A.value), B1=int(dut.B.value), ALU_Out=int(dut.ALU_Out.value), EXP=A1-B1)