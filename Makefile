APP_NAME = b4buy
SOURCES = main.c
CURRENT_DIR=$(shell pwd)
INCLUDES = -I$(CURRENT_DIR)/includes/
LIBS = -L$(CURRENT_DIR)/lib
LDFLAGS = -llog

default:
	$(CC) $(SOURCES) -o $(APP_NAME) $(INCLUDES) $(LIBS) $(LDFLAGS)
