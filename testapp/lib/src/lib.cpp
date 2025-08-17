#include "../include/lib.h"

#include <fmt/color.h>
#include <fmt/core.h>

void lib(const std::string_view& msg) {
  if (msg != "\n") {
    fmt::print(fmt::emphasis::bold | fmt::fg(fmt::color::yellow), "{}",
               __func__);
  }
  fmt::print(fmt::emphasis::faint | fmt::fg(fmt::color::gray), " {}", msg);
}