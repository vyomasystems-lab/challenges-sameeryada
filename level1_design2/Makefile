# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/seq_detect_1011_withoutbug.v

TOPLEVEL := seq_detect_1011_withoutbug # design
MODULE   := test_seq_detect_1011      # test

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
