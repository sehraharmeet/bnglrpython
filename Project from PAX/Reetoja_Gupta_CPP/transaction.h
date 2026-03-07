#ifndef TRANSACTION_H
#define TRANSACTION_H

#include <string>
#include <chrono>

enum class TransactionType
{
    Income,
    Expense
};

enum class Category
{
    Food,
    Travel,
    Salary,
    Rent,
    Investment,
    Utilities,
    Other
};

class Transaction
{
private:
    int id;
    double amount;
    Category category;
    TransactionType type;
    std::string description;
    std::chrono::system_clock::time_point timestamp;

public:
    Transaction(int id,
                double amount,
                Category category,
                TransactionType type,
                std::string description)
        : id(id),
          amount(amount),
          category(category),
          type(type),
          description(std::move(description)),
          timestamp(std::chrono::system_clock::now())
    {}

    int getId() const { return id; }

    double getAmount() const { return amount; }

    Category getCategory() const { return category; }

    TransactionType getType() const { return type; }

    const std::string& getDescription() const { return description; }

    std::chrono::system_clock::time_point getTimestamp() const
    {
        return timestamp;
    }
};

#endif