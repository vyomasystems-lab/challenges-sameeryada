# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random


@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    A_inp30 = 2
    B_sel = 30
# input driving
    dut.inp30.value = A_inp30
    dut.sel.value = B_sel
    await Timer(2, units='ns')
    #assert dut.out.value == A_inp30, "MUX result is incorrect: {A_inp30} != {OUT}, expected value={EXP}".format(A_inp30=int(dut.inp30.value),B_sel=int(dut.sel.value), OUT=int(dut.out.value), EXP=A_inp30) 
    #AssertionError: MUX result is incorrect: 2 != 0, expected value=2
    assert dut.out.value == A_inp30, "MUX result is incorrect: {A_inp30} != {OUT}, expected value={EXP}".format(A_inp30=int(dut.inp30.value), B_sel=int(dut.sel.value), OUT=int(dut.out.value), EXP=A_inp30)
    cocotb.log.info('##### CTB: Develop your test here ########')
