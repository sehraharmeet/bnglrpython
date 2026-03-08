#include "Tracker/Tracker.hpp"
#include <algorithm>
#include <chrono>
#include <vector>
#include <format>

void Tracker::addTransaction() {
    std::string title, category;
    double amount;
    int typeChoice;

    std::cout << "Enter Title: ";
    std::getline(std::cin, title);

    std::cout << "Enter Amount: ";
    std::cin >> amount;
    std::cin.ignore();

    std::cout << "1. Income  2. Expense: ";
    std::cin >> typeChoice;
    std::cin.ignore();

    std::cout << "Enter Category: ";
    std::getline(std::cin, category);

    emplaceTransaction(title, amount,
        (typeChoice == 1) ? Type::Income : Type::Expense,
        category);
}

void Tracker::showAll() const {
    for (const auto& txn : records) {
        std::cout << txn->id << " | "
            << txn->title << " | "
            << txn->amount << " | "
            << txn->category << " | "
            << (txn->type == Type::Income ? "Income" : "Expense") << '\n';
    }
}

void Tracker::showSummary() const {
    double income = calculateTotal(records,
        [](const std::unique_ptr<Transaction>& txn) -> double {
            return (txn->type == Type::Income) ? txn->amount : 0.0;
        });

    double expense = calculateTotal(records,
        [](const std::unique_ptr<Transaction>& txn) -> double {
            return (txn->type == Type::Expense) ? txn->amount : 0.0;
        });

    std::cout << "\nTotal Income: " << income
        << "\nTotal Expense: " << expense
        << "\nBalance: " << (income - expense) << '\n';
}

void Tracker::showByCategory() const {
    std::string cat;
    std::cout << "Enter category: ";
    std::getline(std::cin, cat);

    std::vector<const Transaction*> filtered;

    std::copy_if(records.begin(), records.end(), std::back_inserter(filtered),
        [&cat](const std::unique_ptr<Transaction>& up) {
            return up->category == cat;
        });

    if (filtered.empty()) {
        std::cout << "No transactions in category: " << cat << '\n';
        return;
    }

    std::cout << "Transactions in " << cat << ":\n";
    for (const auto* t : filtered) {
        std::cout << t->id << " | " << t->title << " | " << t->amount
            << " | " << (t->type == Type::Income ? "Income" : "Expense") << '\n';
    }
}

template<typename... Args>
void Tracker::emplaceTransaction(Args&&... args) {
    auto now = std::chrono::zoned_seconds(
        std::chrono::current_zone(),
        std::chrono::floor<std::chrono::seconds>(std::chrono::system_clock::now())
    );

    auto txn = std::make_unique<Transaction>(std::forward<Args>(args)..., now);
    txn->id = nextId++;
    records.push_back(std::move(txn));
    std::cout << "Transaction emplaced\n";
}

std::optional<std::reference_wrapper<const Transaction>> Tracker::findById(int id) const {
    auto it = std::find_if(records.begin(), records.end(),
        [id](const auto& up) { return up->id == id; });
    if (it != records.end()) {
        return std::ref(**it);
    }
    return std::nullopt;
}

void Tracker::showSummaryThreaded() const {
    double inc = 0.0, exp = 0.0;

    std::thread t1([this, &inc]() {
        inc = calculateTotal(records,
            [](const auto& p) { return p->type == Type::Income ? p->amount : 0.0; });
        });

    std::thread t2([this, &exp]() {
        exp = calculateTotal(records,
            [](const auto& p) { return p->type == Type::Expense ? p->amount : 0.0; });
        });

    t1.join();
    t2.join();

    std::cout << "\nIncome: " << inc << "\nExpense: " << exp
        << "\nBalance: " << (inc - exp) << '\n';
}

void Tracker::showWithDate() const {
    for (const auto& up : records) {
        const auto& ts = up->timestamp;
        const auto local_time = ts.get_local_time();
        const auto days = std::chrono::floor<std::chrono::days>(local_time);
        const auto ymd = std::chrono::year_month_day{ days };

        std::cout << std::format("{}-{:02}-{:02} {} | {:.2f} | {}\n",
            static_cast<int>(ymd.year()),
            static_cast<unsigned>(ymd.month()),
            static_cast<unsigned>(ymd.day()),
            up->title, up->amount, up->category);
    }
}