# Compiler and compiler flags
CXX = g++
CXXFLAGS-std=c++14 -Wall -Wextra -Werror -pedantic

#Directories
SRC_DIR= src
INC_DIR= include
BUILD_DIR= build

#Files
SRC_FILES = $(wildcard $(SRC_DIR)/*.cpp)
OBJ_FILES = $(patsubst $(SRC_DIR)/%.cpp, $(BUILD_DIR)/%.o, $(SRC_FILES))
TARGET= my_program

#Libraries
LIBS = -lboost_filesystem -lboost_system -ljpeg

#Build target
$(TARGET): $(OBJ_FILES)
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS)

#Build object files
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -I$(INC_DIR) -c -o $@ $<

#Clean up
clean:
	rm -f $(BUILD_DIR)/*.o $(TARGET)