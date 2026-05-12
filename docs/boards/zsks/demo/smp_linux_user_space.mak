MKDIRS := $(TARGET_PATH)
TARGET_NAME := $(patsubst %/,%,$(dir $(patsubst %/,%,$(TARGET_PATH))))

# target source
OBJS  := $(SMP_SRCS:%.c=%.o)
CXX_OBJS := $(CXX_SRCS:%.cpp=%.o)

CFLAGS += $(COMM_INC)

MPI_LIBS += $(REL_LIB)/libss_hdmi.a
MPI_LIBS += $(LIBS_LD_CFLAGS)

.PHONY : clean all

all: $(TARGET)

$(TARGET):$(COMM_OBJ) $(OBJS) $(CXX_OBJS) | $(MKDIRS)
	@echo ... ld $@
	@echo ... $(TARGET)
	@$(CC) $(CFLAGS) -lpthread -lm -o $(TARGET_PATH)/$@ $^ -Wl,--start-group $(MPI_LIBS) $(SDK_LIB) $(SENSOR_LIBS) $(INIPARSER_LIB) $(REL_LIB)/libsecurec.a -Wl,--end-group
	@echo =================  $(notdir $(TARGET_NAME)) build success  =================

$(COMM_OBJ): %.o : %.c
	@echo @@@ cc $^
	@$(CC) $(CFLAGS) -c $< -o $@

$(OBJS): %.o : %.c
	@echo @@@ cc $^
	@$(CC) $(CFLAGS) -c $< -o $@

$(CXX_OBJS): %.o : %.cpp
	@echo @@@ c++ $^
	@$(CXX) $(CFLAGS) -c $< -o $@

$(MKDIRS):
	@mkdir -p $(TARGET_PATH)

clean:
	@rm -rf $(TARGET_PATH)
	@rm -f $(OBJS)
	@rm -f $(COMM_OBJ)
	@rm -f $(CXX_OBJS)

cleanstream:
	@rm -f *.h264
	@rm -f *.h265
	@rm -f *.jpg
	@rm -f *.mjp
	@rm -f *.mp4
