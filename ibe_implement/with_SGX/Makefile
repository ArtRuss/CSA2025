# Copyright (C) 2023 Gramine contributors
# SPDX-License-Identifier: BSD-3-Clause

ARCH_LIBDIR ?= /home/kfox24/miniconda3/envs/ibe/lib

ifeq ($(DEBUG),1)
GRAMINE_LOG_LEVEL = debug
else
GRAMINE_LOG_LEVEL = error
endif

.PHONY: all
all: basicident.manifest
ifeq ($(SGX),1)
all: basicident.manifest.sgx basicident.sig
endif

RA_TYPE ?= dcap

basicident.manifest: basicident.manifest.template
	gramine-manifest \
		-Dlog_level=$(GRAMINE_LOG_LEVEL) \
		-Darch_libdir=$(ARCH_LIBDIR) \
		-Dentrypoint=$(realpath $(shell which python)) \
		-Dra_type=$(RA_TYPE) \
		basicident.manifest.template > basicident.manifest

basicident.manifest.sgx basicident.sig : basicident.manifest
	gramine-sgx-sign \
		--manifest $< \
		--output $<.sgx

.PHONY:	run-direct
run-direct:
	gramine-direct basicident /home/kfox24/miniconda3/envs/ibe/bin/python3.11 basicident.py

.PHONY: clean
clean:
	$(RM) *.manifest *.manifest.sgx *.sig OUTPUT* *.PID TEST_STDOUT TEST_STDERR
	$(RM) -r scripts/__pycache__

.PHONY: run-strace
run-strace:
	@echo "Running with strace, this may take a moment... Output will be in strace_output.txt"
	gramine-strace basicident /home/kfox24/miniconda3/envs/ibe/bin/python3.11 basicident.py > strace_output.txt 2>&1

.PHONY: distclean
distclean: clean
