add_library(lib src/lib.cpp) # Add your Source Files here
#@add_target_link_libraries Warning: Do not remove this line
target_link_libraries(lib PRIVATE fmt::fmt)