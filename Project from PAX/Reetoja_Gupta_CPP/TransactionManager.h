#ifndef TRANSACTION_MANAGER_H
#define TRANSACTION_MANAGER_H

#include <vector>
#include <memory>
#include <mutex>
#include <algorithm>

#include "../models/Transaction.h"

class TransactionManager
{
private:
    std::vector<std::shared_ptr<Transaction>> transactions;
    mutable std::mutex mtx;
    int nextId = 1;

public:

    int addTransaction(double amount,
                       Category category,
                       TransactionType type,
                       const std::string& description)
    {
        std::lock_guard<std::mutex> lock(mtx);

        auto transaction =
            std::make_shared<Transaction>(
                nextId++,
                amount,
                category,
                type,
                description);

        transactions.push_back(transaction);

        return transaction->getId();
    }

    void deleteTransaction(int id)
    {
        std::lock_guard<std::mutex> lock(mtx);

        transactions.erase(
            std::remove_if(
                transactions.begin(),
                transactions.end(),
                [id](const auto& t)
                {
                    return t->getId() == id;
                }),
            transactions.end());
    }

    std::vector<std::shared_ptr<Transaction>> getAll() const
    {
        std::lock_guard<std::mutex> lock(mtx);
        return transactions;
    }
};

#endif