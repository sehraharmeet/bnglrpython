#ifndef TRACKER_HPP
#define TRACKER_HPP

#include "Transaction.hpp"
#include "utils.hpp"
#include <vector>
#include <memory>
#include <iostream>
#include <string>
#include <optional>
#include <variant>
#include <concepts>
#include <chrono>
#include <format>
#include <thread>
#include <mutex>
#include <chrono>

class Tracker {
private:
    std::vector<std::unique_ptr<Transaction>> records;
    int nextId = 1;
    std::mutex mtx;

public:
    void addTransaction();
    void showAll() const;
    void showSummary() const;
    void showByCategory() const;
    std::optional<std::reference_wrapper<const Transaction>> findById(int id) const;
    template<typename... Args> void emplaceTransaction(Args&&... args);
    void showSummaryThreaded() const;
    void showWithDate() const;
};

#endif