LLVM ?= 0

ifeq ($(PARAM_FILE), )
	ifeq ($(LLVM), 1)
		PARAM_FILE := ../../../platform/ss928v100_clang/smp/a55_linux/mpp/Makefile.param
		include $(PARAM_FILE)
	else
		PARAM_FILE := ../../../platform/ss928v100_gcc/smp/a55_linux/mpp/Makefile.param
		include $(PARAM_FILE)
	endif
endif

target=$(shell ls -d */ | sed "s;/;;g" | grep -v "thirdparty")

target_clean=$(addsuffix _clean,$(target))

.PHONY:clean all $(target) $(target_clean)

all:$(target)
	@echo "~~~~~~~~~~~~~~Build All Sample SUCCESS~~~~~~~~~~~~~~"
clean:$(target_clean)
	@echo "~~~~~~~~~~~~~~Clean All Sample SUCCESS~~~~~~~~~~~~~~"
$(target):
	@echo "~~~~~~~~~~Start build $@~~~~~~~~~~"
	@cd $@ && make
$(target_clean):
	@echo "~~~~~~~~~~Start clean $(subst _clean,,$@)~~~~~~~~~~"
	@cd $(subst _clean,,$@) && make clean
