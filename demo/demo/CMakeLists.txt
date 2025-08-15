add_executable(demo src/main.cpp) # Add your Source Files here
#@add_target_link_libraries Warning: Do not remove this line
target_link_libraries(demo PRIVATE raylib fmt::fmt)