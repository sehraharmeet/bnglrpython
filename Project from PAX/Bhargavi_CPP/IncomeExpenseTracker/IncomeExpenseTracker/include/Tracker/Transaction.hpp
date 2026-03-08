#ifndef TRANSACTION_HPP
#define TRANSACTION_HPP

#include <string>
#include <chrono>

enum class Type { Income, Expense };

struct Transaction {
    int id{};
    std::string title;
    double amount{};
    Type type{};
    std::string category;
    std::chrono::zoned_seconds timestamp;
};

#endif