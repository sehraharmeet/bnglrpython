#ifndef UTILS_HPP
#define UTILS_HPP

#include <numeric>
#include <functional>
#include <iterator>

template <typename Container, typename Proj = std::identity>
auto calculateTotal(const Container& cont, Proj proj = {})
-> decltype(std::declval<Proj>()(*std::begin(cont))) {
    using value_type = decltype(std::declval<Proj>()(*std::begin(cont)));
    return std::accumulate(
        std::begin(cont),
        std::end(cont),
        value_type{ 0 },
        [proj](value_type sum, const auto& item) {
            return sum + std::invoke(proj, item);
        }
    );
}

#endif